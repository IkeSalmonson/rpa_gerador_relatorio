import unittest
from unittest.mock import Mock
from typing import List, Dict
 
from gerador_relatorio.sales_data.sales_data import SalesData
from gerador_relatorio.data_source.data_source import DataSource 

#### Checar implementações dos testes 

class MockDataSource(DataSource):
    """
    Mock de DataSource para simular fontes de dados em testes.
    """
    def __init__(self, name: str, data_to_return: List[Dict]):
        self.name = name
        self._data = data_to_return

    def extract_data(self) -> List[Dict]:
        return self._data


class TestSalesData(unittest.TestCase):

    def test_consolidate_header_single_source(self):
        """Testa se o consolidate_header funciona com uma única fonte."""
        data1 = [{"colA": 1, "colB": "x"}, {"colA": 2, "colB": "y"}]
        mock_source1 = MockDataSource("Source1", data1)
        
        sources = [mock_source1]
        header_map = SalesData.consolidate_header(sources)
        
        expected_header_map = {
            "colA": [mock_source1], 
            "colB": [mock_source1]
        }
        self.assertDictEqual(header_map, expected_header_map)

    def test_consolidate_header_multiple_sources_different_cols(self):
        """Testa se o consolidate_header mescla cabeçalhos de múltiplas fontes."""
        data1 = [{"colA": 1, "colB": "x"}]
        data2 = [{"colB": "y", "colC": True}]
        mock_source1 = MockDataSource("Source1", data1)
        mock_source2 = MockDataSource("Source2", data2)
        
        sources = [mock_source1, mock_source2]
        header_map = SalesData.consolidate_header(sources)
        
        # A ordem dos mock_sources na lista pode variar, então testamos a presença
        self.assertIn("colA", header_map)
        self.assertIn(mock_source1, header_map["colA"])
        
        self.assertIn("colB", header_map)
        self.assertIn(mock_source1, header_map["colB"])
        self.assertIn(mock_source2, header_map["colB"])
        
        self.assertIn("colC", header_map)
        self.assertIn(mock_source2, header_map["colC"])

    def test_consolidate_header_with_empty_data_sources(self):
        """
        Testa que fontes com dados vazios não contribuem para o header_map,
        mas outras fontes ainda o fazem.
        """
        data1 = [{"colA": 1}]
        data_empty = [] # Fonte que retorna dados vazios
        
        mock_source1 = MockDataSource("Source1", data1)
        mock_source_empty = MockDataSource("SourceEmpty", data_empty)
        
        sources = [mock_source1, mock_source_empty]
        header_map = SalesData.consolidate_header(sources)
        
        expected_header_map = {"colA": [mock_source1]}
        self.assertDictEqual(header_map, expected_header_map)
        self.assertNotIn(mock_source_empty, header_map.get("colA", [])) # Garante que a fonte vazia não está lá

    def test_consolidate_header_all_sources_empty(self):
        """Testa consolidate_header quando todas as fontes retornam dados vazios."""
        mock_source1 = MockDataSource("Source1", [])
        mock_source2 = MockDataSource("Source2", [])
        
        sources = [mock_source1, mock_source2]
        header_map = SalesData.consolidate_header(sources)
        self.assertDictEqual(header_map, {}) # Deve retornar um dicionário vazio

    def test_compute_basic_statistics_normal_data(self):
        """Testa compute_basic_statistics com dados numéricos normais."""
        data = [
            {"value": 10, "category": "A"},
            {"value": 20, "category": "B"},
            {"value": 15, "category": "A"},
            {"value": 5, "category": "C"}
        ]
        stats = SalesData.compute_basic_statistics(data)
        
        self.assertIn("value", stats)
        self.assertEqual(stats["value"]["min"], 5)
        self.assertEqual(stats["value"]["max"], 20)
        self.assertEqual(stats["value"]["blank_count"], 0)

        self.assertIn("category", stats)
        # Para colunas não numéricas, min/max podem não fazer sentido ou serem strings alfabéticas
        # O importante é que blank_count funcione
        self.assertEqual(stats["category"]["blank_count"], 0)

    def test_compute_basic_statistics_with_none_values(self):
        """Testa compute_basic_statistics com valores None (em branco)."""
        data = [
            {"value": 10, "product": "A"},
            {"value": None, "product": "B"},
            {"value": 15, "product": None},
            {"value": None, "product": "C"},
            {"value": 20, "product": "D"},
        ]
        stats = SalesData.compute_basic_statistics(data)
        
        self.assertIn("value", stats)
        self.assertEqual(stats["value"]["min"], 10) # None é ignorado para min/max
        self.assertEqual(stats["value"]["max"], 20) # None é ignorado para min/max
        self.assertEqual(stats["value"]["blank_count"], 2) # Dois valores None

        self.assertIn("product", stats)
        # Para strings, min/max podem ser baseados em ordem alfabética ou retornar None se a coluna for toda None
        # O importante é o blank_count
        self.assertEqual(stats["product"]["blank_count"], 1)

    def test_compute_basic_statistics_empty_data(self):
        """Testa compute_basic_statistics com lista de dados vazia."""
        data: List[Dict] = []
        stats = SalesData.compute_basic_statistics(data)
        self.assertDictEqual(stats, {}) # Deve retornar um dicionário vazio

    def test_compute_basic_statistics_all_none_column(self):
        """Testa compute_basic_statistics com uma coluna que contém apenas None."""
        data = [
            {"value": None},
            {"value": None},
        ]
        stats = SalesData.compute_basic_statistics(data)
        self.assertIn("value", stats)
        self.assertIsNone(stats["value"]["min"]) # Deve ser None se não houver valores válidos
        self.assertIsNone(stats["value"]["max"]) # Deve ser None se não houver valores válidos
        self.assertEqual(stats["value"]["blank_count"], 2)

    def test_compute_basic_statistics_mixed_data_types(self):
        """
        Testa compute_basic_statistics com tipos de dados mistos.
        O comportamento de min/max para tipos mistos é uma consideração.
        No Python, comparação de tipos diferentes pode gerar TypeError ou comportamento inconsistente.
        Para este teste, assumimos que strings são comparáveis e None é ignorado.
        """
        data = [
            {"item": 1, "desc": "apple"},
            {"item": 2, "desc": "orange"},
            {"item": "three", "desc": 123}, # Tipo de dado misto para 'item' e 'desc'
            {"item": 4, "desc": None},
        ]
        stats = SalesData.compute_basic_statistics(data)
        
        self.assertIn("item", stats)
        # Python 3+ compara ints e strings de forma diferente.
        # min([1, 2, "three", 4]) em Python 3 levanta TypeError.
        # A implementação atual de compute_basic_statistics não trata isso.
        # Para ser robusto, ou convertemos para um tipo comum, ou pulamos min/max para colunas mistas.
        # Neste teste, vamos testar o blank_count e assumir que min/max podem falhar ou ser None.
        
        # Testando o blank_count que deve funcionar independentemente do tipo
        self.assertEqual(stats["item"]["blank_count"], 0)
        self.assertEqual(stats["desc"]["blank_count"], 1)

        # Para min/max com tipos mistos, o resultado esperado é que eles sejam None
        # já que a função atual não pode comparar int com str diretamente para min/max
        # Se a implementação fosse mais robusta para lidar com TypeErrors,
        # esses valores deveriam ser None.
        # Ajuste o teste conforme a decisão de design para `compute_basic_statistics`.
        # No momento, a função levantaria um TypeError, o que não é o ideal.
        # Sugiro ajustar `compute_basic_statistics` para tratar TypeError para min/max.
        self.assertIsNone(stats["item"].get("min"))
        self.assertIsNone(stats["item"].get("max"))
        self.assertIsNone(stats["desc"].get("min"))
        self.assertIsNone(stats["desc"].get("max"))

    def test_consolidate_data_single_source(self):
        """Testa a consolidação de dados com uma única fonte."""
        data1 = [{"id": 1, "value": 10}, {"id": 2, "value": 20}]
        mock_source1 = MockDataSource("Source1", data1)
        
        sources = [mock_source1]
        result = SalesData.consolidate_data(sources)
        
        self.assertIsInstance(result, dict)
        self.assertIn("data", result)
        self.assertIn("statistics", result)
        self.assertIn("header_map", result)
        
        self.assertEqual(len(result["data"]), 2)
        self.assertEqual(result["data"], data1)
        
        self.assertEqual(result["statistics"]["value"]["min"], 10)
        self.assertEqual(result["statistics"]["value"]["max"], 20)
        
        self.assertIn("id", result["header_map"])
        self.assertIn("value", result["header_map"])

    def test_consolidate_data_multiple_sources(self):
        """Testa a consolidação de dados de múltiplas fontes com colunas diferentes."""
        data1 = [{"id": 1, "value": 10}, {"id": 2, "value": 20}]
        data2 = [{"id": 3, "product": "A"}, {"id": 4, "value": 30, "product": "B"}]
        
        mock_source1 = MockDataSource("Source1", data1)
        mock_source2 = MockDataSource("Source2", data2)
        
        sources = [mock_source1, mock_source2]
        result = SalesData.consolidate_data(sources)
        
        self.assertEqual(len(result["data"]), 4)
        # Verifica se todos os IDs estão presentes nos dados consolidados
        consolidated_ids = [item["id"] for item in result["data"]]
        self.assertIn(1, consolidated_ids)
        self.assertIn(2, consolidated_ids)
        self.assertIn(3, consolidated_ids)
        self.assertIn(4, consolidated_ids)

        # Verifica as estatísticas da coluna 'value'
        self.assertEqual(result["statistics"]["value"]["min"], 10)
        self.assertEqual(result["statistics"]["value"]["max"], 30)
        self.assertEqual(result["statistics"]["value"]["blank_count"], 1) # id 3 não tem 'value'

        # Verifica o mapa de cabeçalhos
        self.assertIn("id", result["header_map"])
        self.assertIn("value", result["header_map"])
        self.assertIn("product", result["header_map"])
        self.assertIn(mock_source1, result["header_map"]["id"])
        self.assertIn(mock_source2, result["header_map"]["id"])
        self.assertIn(mock_source1, result["header_map"]["value"])
        self.assertIn(mock_source2, result["header_map"]["value"])
        self.assertIn(mock_source2, result["header_map"]["product"])


    def test_consolidate_data_with_empty_sources(self):
        """Testa consolidar dados quando algumas fontes retornam vazio."""
        data1 = [{"id": 1, "item": "X"}]
        data_empty = []
        
        mock_source1 = MockDataSource("Source1", data1)
        mock_source_empty = MockDataSource("SourceEmpty", data_empty)
        
        sources = [mock_source1, mock_source_empty]
        result = SalesData.consolidate_data(sources)
        
        self.assertEqual(len(result["data"]), 1)
        self.assertEqual(result["data"][0]["id"], 1)
        
        # O header_map deve incluir as colunas da fonte não vazia
        self.assertIn("id", result["header_map"])
        self.assertIn("item", result["header_map"])
        self.assertIn(mock_source1, result["header_map"]["id"])
        
        # As estatísticas devem ser calculadas apenas sobre os dados presentes
        self.assertEqual(result["statistics"]["id"]["min"], 1)
        self.assertEqual(result["statistics"]["id"]["blank_count"], 0)

    def test_consolidate_data_all_sources_empty(self):
        """Testa consolidar dados quando todas as fontes estão vazias."""
        mock_source1 = MockDataSource("Source1", [])
        mock_source2 = MockDataSource("Source2", [])
        
        sources = [mock_source1, mock_source2]
        result = SalesData.consolidate_data(sources)
        
        self.assertEqual(result["data"], [])
        self.assertDictEqual(result["statistics"], {})
        self.assertDictEqual(result["header_map"], {})


    def test_consolidate_data_sources_with_missing_columns_in_rows(self):
        """Testa consolidação com dados onde algumas linhas não têm todas as colunas."""
        data1 = [{"id": 1, "value": 10}, {"id": 2, "item": "A"}] # 'value' missing in row 2, 'item' missing in row 1
        mock_source1 = MockDataSource("Source1", data1)
        
        sources = [mock_source1]
        result = SalesData.consolidate_data(sources)
        
        self.assertEqual(len(result["data"]), 2)
        
        # Verifica a contagem de Nones para colunas faltantes
        self.assertEqual(result["statistics"]["value"]["blank_count"], 1)
        self.assertEqual(result["statistics"]["item"]["blank_count"], 1)

        # Verifica o header_map
        self.assertIn("id", result["header_map"])
        self.assertIn("value", result["header_map"])
        self.assertIn("item", result["header_map"])


if __name__ == '__main__':
    unittest.main()
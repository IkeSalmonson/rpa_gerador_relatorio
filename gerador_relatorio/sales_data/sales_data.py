"""
Este módulo define a classe SalesData para armazenar e consolidar
os dados de vendas extraídos das diferentes fontes de dados.
"""

from typing import List, Dict, Any, Optional
from collections import defaultdict
import numbers
from gerador_relatorio.data_source.data_source import DataSource


class SalesData:
    """
    Classe para representar os dados de vendas extraídos das fontes de dados.

    Atributos:
        data (List[Dict[str, Any]]): Uma lista de dicionários, onde cada dicionário
                                     representa uma venda.
        available_columns (List[str]): Uma lista das colunas disponíveis nos dados.
    """

    def __init__(self, data: List[Dict[str, Any]], available_columns: List[str]) -> None:
        """
        Inicializa uma nova instância de SalesData.

        Args:
            data (List[Dict[str, Any]]): A lista inicial de dados de vendas.
            available_columns (List[str]): As colunas disponíveis nos dados.
        """
        self.data = data
        self.available_columns = available_columns

    @staticmethod
    def consolidate_header(sources: List[DataSource]) -> Dict[str, List[DataSource]]:
        header_map: Dict[str, List[DataSource]] = defaultdict(list)
        for source in sources:
            data = source.extract_data()
            if data:  # Check if data is not empty
                source_columns = set().union(*(row.keys() for row in data))
                for column in source_columns:
                    if source not in header_map[column]:
                        header_map[column].append(source)
        return dict(header_map)
 
    @staticmethod
    def compute_basic_statistics(data: List[Dict]) -> Dict[str, Dict[str, Any]]:
        """
        Calcula estatísticas básicas para cada coluna nos dados,
        lidando com tipos de dados mistos e strings numéricas.
        """
        statistics: Dict[str, Dict[str, Any]] = {}
        if not data:
            return statistics
    
        all_columns = set().union(*(row.keys() for row in data))
    
        for column in all_columns:
            values = [row.get(column) for row in data]
            
            # Filtra os valores não nulos e tenta convertê-los para números
            numeric_values = []
            for v in values:
                if v is not None:
                    try:
                        # Tenta converter para float
                        numeric_values.append(float(v))
                    except (ValueError, TypeError):
                        # Ignora valores que não são numéricos
                        pass
                    
            non_null_values = [v for v in values if v is not None]
    
            col_min = None
            col_max = None
            
            if numeric_values:
                col_min = min(numeric_values)
                col_max = max(numeric_values)
            
            statistics[column] = {
                "min": col_min,
                "max": col_max,
                "blank_count": sum(1 for v in values if v is None),
            }
        return statistics        
    
    
    
    

    
    
    

    
    

    
    

        
    

    
    
    
    
    

    
    
    
    
    
    
 



    @staticmethod
    def consolidate_data(sources: List[DataSource]) -> Dict[str, Any]:
        """
        Consolida os dados de vendas de diferentes fontes de dados,
        lidando com diferentes conjuntos de colunas.

        Args:
            sources (List[DataSource]): Uma lista de objetos DataSource
                                        representando as fontes de dados.

        Returns:
            SalesData: Uma instância de SalesData com os dados consolidados.
        """
        all_data: List[Dict] = []
        has_data = False
        for source in sources:
            data = source.extract_data()
            if isinstance(data, list) and data:
                all_data.extend(data)
                has_data = True
            elif isinstance(data, list) and not data:
                print(f"Aviso: {source} retornou uma lista de dados vazia.")
            else:
                print(f"Aviso: extract_data de {source} não retornou uma lista.")

        header_map = {}
        if has_data:
            header_map = SalesData.consolidate_header(sources)

        statistics = SalesData.compute_basic_statistics(all_data)
        return {"data": all_data, "statistics": statistics, "header_map": header_map}
    
    def get_data_by_columns(self, columns: List[str]) -> List[Dict[str, Any]]:
        """
        Retorna os dados apenas com as colunas especificadas.

        Args:
            columns (List[str]): A lista de colunas a serem incluídas nos dados retornados.

        Returns:
            List[Dict[str, Any]]: Uma nova lista de dicionários contendo apenas as colunas especificadas.
        """
        filtered_data = []
        for row in self.data:
            new_row = {col: row[col] for col in columns if col in row}
            filtered_data.append(new_row)
        return filtered_data
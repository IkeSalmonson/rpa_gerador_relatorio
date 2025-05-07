"""
Este módulo define a classe SalesData para armazenar e consolidar
os dados de vendas extraídos das diferentes fontes de dados.
"""

from typing import List, Dict, Any, Optional
from collections import defaultdict

from gerador_relatorios.data_source.data_source import DataSource


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

    @classmethod
    def consolidate_data(cls, sources: List[DataSource]) -> 'SalesData':
        """
        Consolida os dados de vendas de diferentes fontes de dados,
        lidando com diferentes conjuntos de colunas.

        Args:
            sources (List[DataSource]): Uma lista de objetos DataSource
                                        representando as fontes de dados.

        Returns:
            SalesData: Uma instância de SalesData com os dados consolidados.
        """
        all_data: List[Dict[str, Any]] = []
        all_columns: set[str] = set() # Usar um set para colunas únicas

        for source in sources:
            data = source.extract_data()
            if data:  # Certificar que data não é vazio
                all_data.extend(data)
                for row in data:
                    all_columns.update(row.keys()) # Adiciona todas as colunas do row ao set

        available_columns = sorted(list(all_columns)) # Ordena as colunas
        
        # Preencher dados faltantes com None
        consolidated_data: List[Dict[str, Optional[Any]]] = []
        for row in all_data:
            new_row: Dict[str, Optional[Any]] = {}
            for col in available_columns:
                new_row[col] = row.get(col, None) # Usar .get() para evitar KeyError
            consolidated_data.append(new_row)

        return cls(consolidated_data, available_columns)

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
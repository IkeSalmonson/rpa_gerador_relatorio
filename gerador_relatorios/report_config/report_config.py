"""
Este módulo define a classe ReportConfig para carregar e armazenar
a configuração do relatório, incluindo as fontes de dados.
"""

import json
from typing import List

from gerador_relatorios.data_source.data_source import DataSource


class ReportConfig:
    """
    Classe para representar a configuração do relatório,
    incluindo as fontes de dados a serem utilizadas.

    Atributos:
        sources (List[DataSource]): Uma lista de objetos DataSource
                                    representando as fontes de dados.
    """

    def __init__(self, sources: List[DataSource]) -> None:
        """
        Inicializa uma nova instância de ReportConfig.

        Args:
            sources (List[DataSource]): Uma lista de objetos DataSource.
        """
        self.sources = sources

    @classmethod
    def load_config(cls, config_file: str) -> 'ReportConfig':
        """
        Carrega a configuração do relatório de um arquivo JSON.

        Args:
            config_file (str): O caminho para o arquivo JSON de configuração.

        Returns:
            ReportConfig: Uma instância de ReportConfig com as fontes de dados
                          carregadas do arquivo JSON.

        Raises:
            FileNotFoundError: Se o arquivo de configuração não for encontrado.
            json.JSONDecodeError: Se o arquivo de configuração não for um JSON válido.
        """
        try:
            with open(config_file, 'r') as f:
                config_data = json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"Arquivo de configuração não encontrado: {config_file}")
        except json.JSONDecodeError:
            raise json.JSONDecodeError(f"Arquivo de configuração inválido: {config_file}", '', 0)

        sources = []
        for source_data in config_data.get('sources', []):  # Usar .get() para evitar KeyError
            source_type = source_data.get('type')
            source_location = source_data.get('location')
            source_credentials = source_data.get('credentials')

            if source_type == 'web':
                sources.append(DataSource(type=source_type, location=source_location, credentials=source_credentials))  # Corrigido
            elif source_type == 'local':
                sources.append(DataSource(type=source_type, location=source_location))  # Corrigido
            else:
                print(f"Tipo de fonte de dados desconhecido: {source_type}. Ignorando.")

        return cls(sources)
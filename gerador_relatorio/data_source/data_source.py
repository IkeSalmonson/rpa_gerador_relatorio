"""
Este módulo define a classe base DataSource e suas subclasses
WebDataSource e LocalDataSource para representar diferentes fontes de dados.
"""

from abc import ABC, abstractmethod


class DataSource(ABC):
    """
    Classe base abstrata para representar uma fonte de dados.

    Atributos:
        type (str): O tipo da fonte de dados ("web" ou "local").
        location (str): A localização da fonte de dados (URL, diretório, etc.).
        credentials (dict, opcional): Credenciais de acesso (login, senha, etc.).
    """

    def __init__(self, type: str, location: str, credentials: dict = None) -> None:
        """
        Inicializa uma nova instância de DataSource.

        Args:
            type (str): O tipo da fonte de dados.
            location (str): A localização da fonte de dados.
            credentials (dict, opcional): Credenciais de acesso, se necessário.
        """
        self.type = type
        self.location = location
        self.credentials = credentials

    @abstractmethod
    def extract_data(self) -> list:
        """
        Método abstrato para extrair dados da fonte de dados.
        Deve ser implementado pelas subclasses.

        Returns:
            list: Uma lista de dicionários representando os dados extraídos.
        """
        pass  # Método abstrato, não faz nada na classe base


class WebDataSource(DataSource):
    """
    Classe para representar uma fonte de dados web.
    Herda da classe DataSource.
    """

    def __init__(self, location: str, credentials: dict = None) -> None:
        """
        Inicializa uma nova instância de WebDataSource.

        Args:
            location (str): A URL da fonte de dados web.
            credentials (dict, opcional): Credenciais de acesso, se necessário.
        """
        super().__init__(type="web", location=location, credentials=credentials)

    def extract_data(self) -> list:
        """
        Extrai dados da fonte de dados web.
        (Implementação a ser adicionada)

        Returns:
            list: Uma lista de dicionários representando os dados extraídos.
        """
        # Implementação da extração de dados web (usando Puppeteer)
        return []  # Por enquanto, retorna uma lista vazia


#### Mover para o cabecalho do arquivo
import csv
from typing import List, Dict
#from gerador_relatorios.data_source.data_source import DataSource, DataSourceError  # DataSourceError deve ser definido em algum lugar
# Definindo a exceção DataSourceError
class DataSourceError(Exception):
    """
    Exceção personalizada para erros relacionados à fonte de dados.
    """
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message
    # Implementação da exceção local       
    

class LocalDataSource(DataSource):
    """
    Classe para representar uma fonte de dados local.
    Herda da classe DataSource.
    """

    def __init__(self, location: str) -> None:
        """
        Inicializa uma nova instância de LocalDataSource.

        Args:
            location (str): O caminho para o arquivo local.
        """
        #self.location = location
        super().__init__(type="local", location=location)
        


    def extract_data(self) -> list:
        """
        Extrai dados da fonte de dados local.
        (Implementação a ser adicionada)

        Returns:
            list: Uma lista de dicionários representando os dados extraídos.
        """
        # Implementação da leitura de dados de arquivos locais (CSV, etc.)    def extract_data(self) -> List[Dict]:
        data = []
        try:
            with open(self.location, 'r', encoding='utf-8') as file:  # Ajuste a codificação se necessário
                reader = csv.DictReader(file)
                for row in reader:
                    data.append(dict(row))  # Converte OrderedDict para dict
        except FileNotFoundError:
            raise DataSourceError(f"Arquivo não encontrado: {self.location}")
        except csv.Error as e:
            raise DataSourceError(f"Erro ao ler o arquivo CSV: {e}")
        return data
     
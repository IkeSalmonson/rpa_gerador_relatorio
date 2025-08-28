"""
Este módulo define a classe base DataSource e suas subclasses
WebDataSource e LocalDataSource para representar diferentes fontes de dados.
"""

from abc import ABC, abstractmethod
import os
import sys
from pathlib import Path

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
        try:
            base_dir = Path(os.getcwd())
            
            # 2. Combinar o caminho base com o caminho relativo do arquivo de dados
            full_path = base_dir.joinpath(self.location)
            
            # 3. Verificar se o arquivo existe
            if not full_path.exists():
                raise DataSourceError(f"Arquivo não encontrado: {full_path}")
                
            # 4. Ler o arquivo CSV
            data = []
            with open(full_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    data.append(dict(row))
        except FileNotFoundError:
            raise DataSourceError(f"Arquivo não encontrado: {self.location}")
        except csv.Error as e:
            raise DataSourceError(f"Erro ao ler o arquivo CSV: {e}")
        except UnicodeDecodeError as e:
            raise DataSourceError(f"Erro de encoding ao ler o arquivo CSV: {e}")
        
        return data
     
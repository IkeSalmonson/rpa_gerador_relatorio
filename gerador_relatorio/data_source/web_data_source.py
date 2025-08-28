import requests
from typing import List, Dict, Any
from .data_source import DataSource

class WebDataSource(DataSource):
    """
    Uma classe que implementa a interface DataSource para extrair
    dados de uma fonte web.

    Esta implementação assume que a URL retorna um JSON com uma chave
    específica contendo a lista de dados.
    """

    def __init__(self, name: str, location: str, data_key: str, credentials: Dict[str, Any] = None):
        """
        Inicializa o WebDataSource.

        Args:
            name (str): O nome da fonte de dados.
            location (str): A URL da fonte de dados.
            data_key (str): A chave no JSON que contém a lista de dados.
            credentials (Dict[str, Any], optional): Credenciais, se necessário (ex: API key).
        """
        self.name = name
        self.location = location
        self.data_key = data_key
        self.credentials = credentials or {}

    def extract_data(self) -> List[Dict]:
        """
        Extrai os dados da fonte web, fazendo uma requisição GET para a URL.

        Returns:
            List[Dict]: Uma lista de dicionários com os dados.
        """
        try:
            print(f"Extraindo dados da fonte web: {self.location}")
            
            response = requests.get(self.location, timeout=10)
            response.raise_for_status()

            # Acessa a chave correta no JSON retornado
            data_dict = response.json()
            data_list = data_dict.get(self.data_key, [])
            
            if not isinstance(data_list, list):
                print(f"A chave '{self.data_key}' não contém uma lista. Retornando lista vazia.")
                return []
                
            return data_list

        except requests.exceptions.RequestException as e:
            print(f"Erro ao extrair dados da URL {self.location}: {e}")
            return []
        except (json.JSONDecodeError, KeyError) as e:
            print(f"Erro ao decodificar JSON ou acessar a chave '{self.data_key}': {e}")
            return []
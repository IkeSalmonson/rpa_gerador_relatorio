import pytest
from gerador_relatorios.data_source.data_source import LocalDataSource, DataSourceError
import csv
from typing import List, Dict

def create_csv_file(filename: str, data: List[Dict]):
    """Helper function to create a CSV file for testing."""
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        if data:
            fieldnames = data[0].keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)

def test_extract_data_valid(tmp_path):
    """Testa a extração de dados de um arquivo CSV válido."""
    test_data = [{'col1': 'val1', 'col2': 'val2'}, {'col1': 'val3', 'col2': 'val4'}]
    csv_file = tmp_path / "test_data.csv"
    create_csv_file(csv_file, test_data)

    data_source = LocalDataSource(str(csv_file))
    extracted_data = data_source.extract_data()
    assert extracted_data == test_data

def test_extract_data_empty(tmp_path):
    """Testa a extração de dados de um arquivo CSV vazio."""
    csv_file = tmp_path / "test_data_empty.csv"
    create_csv_file(csv_file, [])  # Cria um arquivo CSV vazio
    data_source = LocalDataSource(str(csv_file))
    extracted_data = data_source.extract_data()
    assert extracted_data == []

def test_extract_data_missing_file():
    """Testa a exceção FileNotFoundError quando o arquivo não existe."""
    data_source = LocalDataSource("non_existent_file.csv")
    with pytest.raises(DataSourceError) as exc_info:
        data_source.extract_data()
    assert "Arquivo não encontrado:" in str(exc_info.value)

def test_extract_data_invalid_format(tmp_path):
    """Testa a exceção csv.Error para um arquivo CSV inválido."""
    csv_file = tmp_path / "test_data_invalid.csv"
    with open(csv_file, 'w') as f:
        f.write("invalid,csv,data")  # Escreve dados inválidos
    data_source = LocalDataSource(str(csv_file))
    with pytest.raises(DataSourceError) as exc_info:
        data_source.extract_data()
    assert "Erro ao ler o arquivo CSV:" in str(exc_info.value)
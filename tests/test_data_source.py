import pytest
from gerador_relatorio.data_source.data_source import LocalDataSource, DataSourceError
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

def test_extract_data_invalid_enconding(tmp_path):
    """Testa a exceção de enconding para um arquivo com enconding incompativel."""
    csv_file = tmp_path / "test_data_invalid.csv"
    with open(csv_file, 'w', encoding ='utf-16') as f:
        f.write("invalid,csv,data" )  # Escreve dados inválidos
    data_source = LocalDataSource(str(csv_file))
    with pytest.raises(DataSourceError) as exc_info:
        data_source.extract_data()
    assert "Erro de encoding ao ler o arquivo CSV:" in str(exc_info.value)


'''
 Testes com a exceção csv.Error precisam se uma situação bem especifica para ocorrer e preciso forçar isso. 
'''
def test_extract_data_invalid_format_field_limit(tmp_path):
    """Testa csv.Error com um campo que excede o field_size_limit."""
    csv_file = tmp_path / "test_data_field_limit.csv"

    # Define um limite de campo bem pequeno (ex: 10 caracteres)
    # O padrão é 128KB, então precisamos alterá-lo no teste.
    original_limit = csv.field_size_limit()
    csv.field_size_limit(10) # Define um limite baixo para o teste

    try:
        # Uma linha com um campo muito longo
        invalid_data = "header1,AAAAAAAAAAAAAAAAAAAA,header3" 

        with open(csv_file, 'w', encoding='utf-8', newline='') as f:
            f.write(invalid_data)

        data_source = LocalDataSource(str(csv_file))

        with pytest.raises(DataSourceError) as exc_info:
            data_source.extract_data()

        assert "Erro ao ler o arquivo CSV:" in str(exc_info.value)
        assert "field larger than field limit" in str(exc_info.value)
    finally:
        # Sempre restaura o limite original após o teste
        csv.field_size_limit(original_limit)

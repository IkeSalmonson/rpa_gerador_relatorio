# tests/test_report_formatter.py

import pytest
import os
import csv
import io
from typing import Dict, Any, List

# Assumindo que o seu arquivo está em gerador_relatorios/sales_report/csv_report_formatter.py
from gerador_relatorio.sales_report.csv_report_formatter import CSVReportFormatter

# Fixture para fornecer dados consolidados de exemplo para os testes
@pytest.fixture
def sample_consolidated_data() -> Dict[str, Any]:
    """Retorna um dicionário de dados consolidados de exemplo."""
    return {
        "data": [
            {"id": 1, "product": "Laptop", "price": 1200.00},
            {"id": 2, "product": "Mouse", "price": 25.50},
            {"id": 3, "product": "Monitor", "price": 300.00},
            {"id": 4, "product": "Keyboard", "price": None}
        ],
        "statistics": {
            "id": {"min": 1, "max": 4, "blank_count": 0},
            "product": {"blank_count": 0},
            "price": {"min": 25.50, "max": 1200.00, "blank_count": 1}
        },
        "header_map": {
            "id": ["source1"],
            "product": ["source1"],
            "price": ["source1"]
        }
    }

# Fixture para dados com colunas fora de ordem
@pytest.fixture
def out_of_order_consolidated_data() -> Dict[str, Any]:
    """
    Retorna dados consolidados com as colunas em uma ordem diferente
    para garantir que a lógica de ordenação (ou não ordenação) funcione.
    """
    return {
        "data": [
            {"price": 1200.00, "product": "Laptop", "id": 1},
            {"price": 25.50, "product": "Mouse", "id": 2},
        ],
        "statistics": {},
        "header_map": {
            "price": ["source1"],
            "product": ["source1"],
            "id": ["source1"]
        }
    }

def test_format_report_writes_correct_data(sample_consolidated_data: Dict[str, Any]):
    """Verifica se o formatador escreve o conteúdo CSV corretamente."""
    formatter = CSVReportFormatter()
    csv_string = formatter.format_report(sample_consolidated_data)
    
    # Usar io.StringIO para ler a string como se fosse um arquivo
    csv_reader = csv.DictReader(io.StringIO(csv_string))
    rows = list(csv_reader)
    
    # Verifica o cabeçalho (que deve seguir a ordem natural das chaves)
    expected_headers = ['id', 'product', 'price']
    assert csv_reader.fieldnames == expected_headers

    # Verifica o número de linhas
    assert len(rows) == len(sample_consolidated_data['data'])

    # Verifica o conteúdo das linhas (csv.DictReader lê tudo como string)
    assert rows[0] == {'id': '1', 'product': 'Laptop', 'price': '1200.0'}
    assert rows[1] == {'id': '2', 'product': 'Mouse', 'price': '25.5'}
    assert rows[2] == {'id': '3', 'product': 'Monitor', 'price': '300.0'}
    assert rows[3] == {'id': '4', 'product': 'Keyboard', 'price': ''} # None se torna uma string vazia

def test_format_report_out_of_order_columns(out_of_order_consolidated_data: Dict[str, Any]):
    """
    Verifica se a ordem das colunas no CSV final corresponde à ordem
    das chaves em 'header_map', conforme sua intenção.
    """
    formatter = CSVReportFormatter()
    csv_string = formatter.format_report(out_of_order_consolidated_data)
    
    csv_reader = csv.DictReader(io.StringIO(csv_string))
    rows = list(csv_reader)
    
    expected_headers = ['price', 'product', 'id']
    assert csv_reader.fieldnames == expected_headers
    
    assert rows[0] == {'price': '1200.0', 'product': 'Laptop', 'id': '1'}
    assert rows[1] == {'price': '25.5', 'product': 'Mouse', 'id': '2'}
    
def test_format_report_with_empty_data():
    """Testa se o formatador lança um erro com dados de entrada vazios."""
    formatter = CSVReportFormatter()
    empty_consolidated_data = {
        "data": [],
        "statistics": {},
        "header_map": {}
    }
    with pytest.raises(ValueError, match="Não há dados para gerar o relatório CSV."):
        formatter.format_report(empty_consolidated_data)

def test_format_report_missing_columns_in_some_rows(sample_consolidated_data: Dict[str, Any]):
    """
    Verifica se o formatador lida corretamente com colunas que estão faltando em
    algumas linhas, mas existem em 'header_map'.
    """
    # Cria uma cópia para evitar modificar a fixture original
    data = sample_consolidated_data.copy()
    
    # Adiciona uma nova coluna 'product_id' em apenas uma linha
    data['data'][0]['product_id'] = 'SKU-001'
    data['header_map']['product_id'] = ['source1']
    
    formatter = CSVReportFormatter()
    csv_string = formatter.format_report(data)
    
    csv_reader = csv.DictReader(io.StringIO(csv_string))
    rows = list(csv_reader)
    
    # Verifica se a nova coluna foi incluída no cabeçalho
    expected_headers = ['id', 'product', 'price', 'product_id']
    assert csv_reader.fieldnames == expected_headers

    # A linha 1 deve ter o valor, e as outras devem ter a string vazia
    assert rows[0]['product_id'] == 'SKU-001'
    assert rows[1]['product_id'] == ''
    assert rows[2]['product_id'] == ''
    assert rows[3]['product_id'] == ''
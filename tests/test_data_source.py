# tests/test_data_source.py

import pytest
import os
import json
import requests_mock
from typing import Dict, Any, List

from gerador_relatorio.data_source.data_source import DataSource, LocalDataSource
from gerador_relatorio.data_source.web_data_source import WebDataSource
from gerador_relatorio.sales_data.sales_data import SalesData
from gerador_relatorio.sales_report.csv_report_formatter import CSVReportFormatter
from gerador_relatorio.sales_report.html_report_formatter import HTMLReportFormatter
from gerador_relatorio.sales_report.text_report_formatter import TextReportFormatter

# --- Fixture para dados de teste unificados ---
@pytest.fixture
def mock_consolidated_data() -> Dict[str, Any]:
    """
    Cria um dicionário de dados consolidados com dados de vendas e estatísticas.
    """
    data = [
        {"product_name": "Laptop", "quantity": "10", "price": "1200"},
        {"product_name": "Mouse", "quantity": "50", "price": "25.50"},
        {"product_name": "Keyboard", "quantity": "30", "price": "75.00"},
    ]
    
    statistics = {
        "product_name": {"min": None, "max": None, "blank_count": 0},
        "quantity": {"min": 10.0, "max": 50.0, "blank_count": 0},
        "price": {"min": 25.50, "max": 1200.0, "blank_count": 0},
    }
    
    header_map = {
        "product_name": "Nome do Produto",
        "quantity": "Quantidade",
        "price": "Preço"
    }

    return {
        "data": data,
        "statistics": statistics,
        "header_map": header_map
    }

# --- Testes para WebDataSource (FR012) ---
def test_web_data_source_extracts_data_successfully():
    """
    Testa a extração de dados de uma API web que retorna um JSON com uma chave específica.
    """
    mock_api_response = {
        "products": [
            {"id": 1, "title": "Produto A"},
            {"id": 2, "title": "Produto B"}
        ],
        "total": 2
    }
    with requests_mock.Mocker() as m:
        test_url = "http://api.example.com/products"
        m.get(test_url, json=mock_api_response)
        
        web_source = WebDataSource(name="TestAPI", location=test_url, data_key="products")
        data = web_source.extract_data()

        assert isinstance(data, list)
        assert len(data) == 2
        assert data[0]["title"] == "Produto A"

def test_web_data_source_handles_http_error():
    """
    Testa se o WebDataSource retorna uma lista vazia em caso de erro HTTP.
    """
    with requests_mock.Mocker() as m:
        test_url = "http://api.example.com/nonexistent"
        m.get(test_url, status_code=404)
        
        web_source = WebDataSource(name="ErrorAPI", location=test_url, data_key="data")
        data = web_source.extract_data()
        assert data == []

# --- Testes para SalesData (Refatoração de Estatísticas) ---
def test_sales_data_computes_statistics_with_strings():
    """
    Testa se o compute_basic_statistics lida corretamente com strings numéricas.
    """
    data = [
        {"A": "100", "B": "50", "C": "abc"},
        {"A": "200", "B": "30", "C": None},
        {"A": "150", "B": "80", "C": ""},
    ]
    stats = SalesData.compute_basic_statistics(data)
    
    # A coluna 'A' deve ter min/max corretos
    assert stats["A"]["min"] == 100.0
    assert stats["A"]["max"] == 200.0
    assert stats["A"]["blank_count"] == 0

    # A coluna 'C' deve ter 'N/A' para min/max e contagem correta de nulos
    assert stats["C"]["min"] is None
    assert stats["C"]["max"] is None
    assert stats["C"]["blank_count"] == 1

# --- Testes para ReportFormatters com Estatísticas (FR011) ---

def test_csv_report_formatter_includes_statistics(mock_consolidated_data):
    """
    Testa se o CSVReportFormatter gera dois arquivos: um para dados e um para estatísticas.
    """
    formatter = CSVReportFormatter()
    data_report, stats_report = formatter.format_report(mock_consolidated_data)
    
    # Verifica o relatório de dados
    assert "product_name,quantity,price" in data_report
    assert "Laptop,10,1200" in data_report
    
    # Verifica o relatório de estatísticas
    assert "metric,min,max,blank_count" in stats_report
    assert "quantity,10.0,50.0,0" in stats_report
    assert "price,25.5,1200.0,0" in stats_report

def test_html_report_formatter_includes_statistics(mock_consolidated_data):
    """
    Testa se o HTMLReportFormatter gera um relatório que contém a tabela de dados e de estatísticas.
    """
    formatter = HTMLReportFormatter()
    report = formatter.format_report(mock_consolidated_data)
    
    # Verifica se a tabela de dados está presente
    assert "<h1>Relatório de Vendas</h1>" in report
    assert "<h2>Dados de Vendas</h2>" in report
    assert "<th>product_name</th>" in report
    assert "<td>Laptop</td>" in report
    
    # Verifica se a tabela de estatísticas está presente
    assert "<h2>Estatísticas</h2>" in report
    assert "<th>Mínimo</th>" in report
    assert "<th>Máximo</th>" in report
    assert "<td>10.0</td>" in report
    assert "<td>1200.0</td>" in report

def test_text_report_formatter_includes_statistics(mock_consolidated_data):
    """
    Testa se o TextReportFormatter gera um relatório com as seções de dados e estatísticas.
    """
    formatter = TextReportFormatter()
    report = formatter.format_report(mock_consolidated_data)

    # Verifica se o relatório contém os dados e estatísticas em texto
    assert "Relatório de Vendas" in report
    assert "Dados de Vendas:" in report
    assert "Laptop | 10 | 1200" in report
    assert "Estatísticas:" in report
    assert "  - Coluna: quantity" in report
    assert "    Mínimo: 10.0" in report
    assert "    Máximo: 50.0" in report
    assert "    Nulos: 0" in report
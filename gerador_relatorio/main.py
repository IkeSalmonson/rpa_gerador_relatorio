"""
Este módulo contém o ponto de entrada principal da POC para gerar relatórios de vendas.
Ele orquestra o fluxo de trabalho, desde a leitura da configuração até a geração do relatório.
"""

import json
import sys
from pathlib import Path
from typing import List
import os

from gerador_relatorio.data_source.data_source import DataSource, LocalDataSource
from gerador_relatorio.data_source.web_data_source import WebDataSource
from gerador_relatorio.sales_data.sales_data import SalesData
from gerador_relatorio.sales_report.sales_report import SalesReport
from gerador_relatorio.sales_report.html_report_formatter import HTMLReportFormatter
from gerador_relatorio.sales_report.text_report_formatter import TextReportFormatter
from gerador_relatorio.sales_report.csv_report_formatter import CSVReportFormatter

def main():
    """
    Função principal para executar a POC de geração de relatórios de vendas.
    """
    # 1. Carregar a Configuração
    config_data = None
    
    # Verifica se o programa está rodando como um executável do PyInstaller
    if getattr(sys, 'frozen', False):
        # Caminho base é o diretório temporário do PyInstaller
        base_path = sys._MEIPASS
        config_path = os.path.join(base_path, 'config.json')
        print(f"Executável do PyInstaller detectado. Procurando config.json em: {config_path}")
        
        # Adicionando uma verificação extra para o caso de o arquivo estar na raiz do executável.
        if not os.path.exists(config_path):
            base_path = os.path.dirname(sys.executable)
            config_path = os.path.join(base_path, 'config.json')
            print(f"Config não encontrada em _MEIPASS, tentando o diretório do executável: {config_path}")
    
    else:
        # Caminho para ambiente de desenvolvimento normal
        base_path = os.path.dirname(os.path.abspath(__file__))
        possible_paths = [
            Path(os.path.join(base_path, 'config.json')),
            Path(os.path.join(base_path, '../config.json'))
        ]
        config_path = None
        for path in possible_paths:
            if path.exists():
                config_path = path
                break
        if not config_path:
            print("Erro: Arquivo de configuração 'config.json' não encontrado em ambiente de desenvolvimento.")
            return
    
    try:
        if not config_path:
            raise FileNotFoundError("Não foi possível encontrar o arquivo de configuração.")
        
        print(f"Arquivo de configuração final: {config_path}")
        with open(config_path, 'r') as f:
            config_data = json.load(f)
        
    except FileNotFoundError as e:
        print(f"Erro: {e}")
        return
    except json.JSONDecodeError:
        print("Erro: Arquivo de configuração 'config.json' inválido.")
        return
    sources: List[DataSource] = []
    for source_data in config_data.get('sources', []):
        source_type = source_data.get('type')
        source_location = source_data.get('location')
        source_credentials = source_data.get('credentials')
        source_name = source_data.get('name')

        if source_type == 'web':
            source_data_key = source_data.get('data_key')
            if not source_data_key:
                print(f"Erro: 'data_key' não especificado para a fonte web {source_name}. Ignorando.")
                continue
            sources.append(WebDataSource(name=source_name , location=source_location, data_key = source_data_key ,credentials=source_credentials))

        elif source_type == 'local':
            sources.append(LocalDataSource(location=source_location))
        else:
            print(f"Tipo de fonte de dados desconhecido: {source_type}. Ignorando.")

    # 2. Consolidar os Dados
    sales_data = SalesData.consolidate_data(sources)

    # 3. Gerar o Relatório
    # Escolher o formatador (pode ser configurado também)
    html_formatter = HTMLReportFormatter()
    text_formatter = TextReportFormatter()

    html_report = SalesReport(sales_data, html_formatter)
    text_report = SalesReport(sales_data, text_formatter)

    #print("Relatório HTML:\n", html_report.generate_report())
    print("\nRelatório Texto:\n", text_report.generate_report())

    csv_formatter = CSVReportFormatter()
    csv_report_string, csv_statistics_string  = csv_formatter.format_report(sales_data)


    output_dir = "output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    output_path_report = os.path.join(output_dir, "relatorio_vendas.csv")
    output_path_statistics = os.path.join(output_dir, "relatorio_vendas_estatisticas.csv")
    # Instanciar e usar o formatador
    # Salvar o relatório em um arquivo
    with open(output_path_report, "w", newline="", encoding="utf-8") as file:
        file.write(csv_report_string)
    print(f"Relatório final salvo em: {output_dir}")
    with open(output_path_statistics, "w", newline="", encoding="utf-8") as file:
        file.write(csv_statistics_string)
    

if __name__ == "__main__":
    main()
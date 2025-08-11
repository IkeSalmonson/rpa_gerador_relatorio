"""
Este módulo define a classe CSVReportFormatter para formatar relatórios em CSV.
"""
import csv
import io
from typing import Dict, Any, List

from gerador_relatorio.sales_report.report_formatter import ReportFormatter

class CSVReportFormatter(ReportFormatter):
    """
    Formatador de relatório para o formato CSV.
    """

    def format_report(self, consolidated_data: Dict[str, Any]) -> str:
        """
        Formata os dados de vendas consolidados em um relatório CSV.

        Args:
            consolidated_data (Dict[str, Any]): Dicionário com os dados consolidados,
                                                incluindo 'data' e 'header_map'.

        Returns:
            str: O relatório em formato CSV.
        """
        if not consolidated_data.get('data'):
            raise ValueError("Não há dados para gerar o relatório CSV.")

        # Usa io.StringIO para simular um arquivo na memória
        output = io.StringIO()

        # Extrai os nomes das colunas de forma segura
        columns = list(consolidated_data['header_map'].keys())

        # Usa csv.DictWriter que é ideal para listas de dicionários
        # Isso lida com o cabeçalho e com as linhas automaticamente
        writer = csv.DictWriter(output, fieldnames=columns)

        # Escreve o cabeçalho
        writer.writeheader()

        # Escreve os dados. O DictWriter preenche colunas ausentes com vazio por padrão.
        for sale in consolidated_data['data']:
            row_to_write = {col: sale.get(col, '') for col in columns}
            writer.writerow(row_to_write)

        # Retorna o valor do buffer como uma string
        return output.getvalue()
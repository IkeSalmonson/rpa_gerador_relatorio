"""
Este módulo define a classe TextReportFormatter para formatar relatórios em texto.
"""

from gerador_relatorio.sales_report.report_formatter import ReportFormatter
from gerador_relatorio.sales_data.sales_data import SalesData
from typing import Dict, Any, List


class TextReportFormatter(ReportFormatter):
    """
    Formatador de relatório para texto simples.
    """

    def format_report(self, data: SalesData) -> str:
        """
        Formata os dados de vendas em um relatório de texto simples.

        Args:
            data (SalesData): Os dados de vendas a serem formatados.

        Returns:
            str: O relatório em formato de texto.
        """
        report = "--- Relatório de Vendas ---\n\n"

        # Obter as colunas disponíveis
        columns =  data['header_map'].keys()

        # Criar o cabeçalho
        header = " | ".join(columns)
        report += header + "\n"
        report += "-" * len(header) + "\n"

        # Adicionar os dados
        start_index = 1 if data['data'] and self._is_header_row(data['data'][0]) else 0  # Nova linha
        for i in range(start_index, len(data['data'])):                               # Nova linha
            sale = data['data'][i]                                                    # Nova linha
            row = " | ".join(str(sale.get(col, 'N/A')) for col in columns)
            report += row + "\n"
        return report

    def _is_header_row(self, row: Dict[str, Any]) -> bool:                        # Nova função
        """
        Verifica se uma linha é uma linha de cabeçalho (todos os valores são strings).

        Args:
            row (Dict[str, Any]): A linha a ser verificada.

        Returns:
            bool: True se a linha for um cabeçalho, False caso contrário.
        """
        return all(isinstance(value, str) for value in row.values())               # Nova linha
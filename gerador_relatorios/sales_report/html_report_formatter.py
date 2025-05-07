"""
Este módulo define a classe HTMLReportFormatter para formatar relatórios em HTML.
"""

from gerador_relatorios.sales_report.report_formatter import ReportFormatter
from gerador_relatorios.sales_data.sales_data import SalesData
from typing import Dict, Any, List


class HTMLReportFormatter(ReportFormatter):
    """
    Formatador de relatório para HTML.
    """

    def format_report(self, data: SalesData) -> str:
        """
        Formata os dados de vendas em um relatório HTML.

        Args:
            data (SalesData): Os dados de vendas a serem formatados.

        Returns:
            str: O relatório em formato HTML.
        """
        report = "<html><body><h1>Relatório de Vendas</h1><table>"

        # Obter as colunas disponíveis
        columns = data.available_columns

        # Criar o cabeçalho
        report += "<tr>"
        for col in columns:
            report += f"<th>{col}</th>"
        report += "</tr>"

        # Adicionar os dados
        start_index = 1 if data.data and self._is_header_row(data.data[0]) else 0  # Nova linha
        for i in range(start_index, len(data.data)):                               # Nova linha
            sale = data.data[i]                                                    # Nova linha
            report += "<tr>"
            for col in columns:
                report += f"<td>{str(sale.get(col, 'N/A'))}</td>"
            report += "</tr>"

        report += "</table></body></html>"
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
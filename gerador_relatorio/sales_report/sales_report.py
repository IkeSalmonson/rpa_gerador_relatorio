"""
Este módulo define a classe SalesReport para gerar relatórios de vendas
a partir dos dados consolidados.
"""

from gerador_relatorio.sales_data.sales_data import SalesData
from gerador_relatorio.sales_report.report_formatter import ReportFormatter


class SalesReport:
    """
    Classe para gerar relatórios de vendas.

    Atributos:
        data (SalesData): Os dados de vendas a serem incluídos no relatório.
        formatter (ReportFormatter): O formatador de relatório a ser usado.
    """

    def __init__(self, data: SalesData, formatter: ReportFormatter) -> None:
        """
        Inicializa uma nova instância de SalesReport.

        Args:
            data (SalesData): Os dados de vendas.
            formatter (ReportFormatter): O formatador de relatório.
        """
        self.data = data
        self.formatter = formatter

    def generate_report(self) -> str:
        """
        Gera o relatório de vendas usando o formatador especificado.

        Returns:
            str: O relatório gerado como uma string.
        """
        return self.formatter.format_report(self.data)
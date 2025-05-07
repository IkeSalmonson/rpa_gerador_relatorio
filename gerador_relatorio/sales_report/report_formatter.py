"""
Este módulo define a interface abstrata ReportFormatter para formatar relatórios.
"""

from abc import ABC, abstractmethod
from gerador_relatorio.sales_data.sales_data import SalesData
from typing import Dict, Any, List


class ReportFormatter(ABC):
    """
    Interface abstrata para formatadores de relatório.
    """

    @abstractmethod
    def format_report(self, data: SalesData) -> str:
        """
        Formata os dados de vendas em um relatório.

        Args:
            data (SalesData): Os dados de vendas a serem formatados.

        Returns:
            str: O relatório formatado como uma string.
        """
        pass
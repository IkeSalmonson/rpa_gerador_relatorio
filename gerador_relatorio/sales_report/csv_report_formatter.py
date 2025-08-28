# gerador_relatorio/sales_report/csv_report_formatter.py

import csv
import io
from typing import Dict, Any, List, Tuple
from gerador_relatorio.sales_report.report_formatter import ReportFormatter

class CSVReportFormatter(ReportFormatter):
    """
    Formatador de relatório para o formato CSV.
    """

    def format_report(self, consolidated_data: Dict[str, Any]) -> Tuple[str, str]:
        """
        Formata os dados de vendas consolidados e as estatísticas em relatórios CSV.

        Args:
            consolidated_data (Dict[str, Any]): Dicionário com os dados consolidados,
                                                incluindo 'data', 'statistics' e 'header_map'.

        Returns:
            Tuple[str, str]: Uma tupla contendo a string do relatório de dados e a 
                             string do relatório de estatísticas.
        """
        data_report = self.format_data(consolidated_data)
        statistics_report = self.format_statistics(consolidated_data)
        return data_report, statistics_report

    def format_data(self, consolidated_data: Dict[str, Any]) -> str:
        """
        Gera a string CSV para os dados de vendas.
        """
        data = consolidated_data.get('data')
        if not data:
            raise ValueError("Não há dados para gerar o relatório CSV.")
        
        output = io.StringIO()
        columns = list(consolidated_data['header_map'].keys())
        
        writer = csv.DictWriter(output, fieldnames=columns)
        writer.writeheader()

        for row in data:
            row_to_write = {col: row.get(col, '') for col in columns}
            writer.writerow(row_to_write)
        
        return output.getvalue()

    def format_statistics(self, consolidated_data: Dict[str, Any]) -> str:
        """
        Gera a string CSV para as estatísticas de vendas.
        """
        statistics = consolidated_data.get('statistics')
        if not statistics:
            return "" # Retorna string vazia se não houver estatísticas

        output = io.StringIO()
        fieldnames = ["metric", "min", "max", "blank_count"]
        writer = csv.DictWriter(output, fieldnames=fieldnames)
        writer.writeheader()

        for column, metrics in statistics.items():
            row = {
                "metric": column,
                "min": metrics.get("min", ""),
                "max": metrics.get("max", ""),
                "blank_count": metrics.get("blank_count", 0),
            }
            writer.writerow(row)

        return output.getvalue()
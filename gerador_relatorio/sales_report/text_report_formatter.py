"""
Este módulo define a classe TextReportFormatter para formatar relatórios em texto simples.
"""

from typing import Dict, Any, List
from gerador_relatorio.sales_report.report_formatter import ReportFormatter

class TextReportFormatter(ReportFormatter):
    """
    Formatador de relatório para texto simples.
    """

    def format_report(self, consolidated_data: Dict[str, Any]) -> str:
        """
        Formata os dados e as estatísticas de vendas em um relatório de texto completo.

        Args:
            consolidated_data (Dict[str, Any]): Dicionário com os dados consolidados,
                                                incluindo 'data', 'statistics' e 'header_map'.

        Returns:
            str: O relatório em formato de texto.
        """
        report_parts = [
            "====================== Relatório de Vendas ======================\n",
            self._format_data_section(consolidated_data),
            "\n" + "=" * 59,
            "\n" + self._format_statistics_section(consolidated_data)
        ]
        
        return "".join(report_parts)

    def _format_data_section(self, consolidated_data: Dict[str, Any]) -> str:
        """Gera a seção de dados do relatório de texto."""
        data = consolidated_data.get("data", [])
        header_map = consolidated_data.get("header_map", {})
        
        if not data:
            return "Nenhum dado de vendas disponível.\n"

        columns = list(header_map.keys())
        
        # Cria o cabeçalho
        data_text = ["Dados de Vendas:\n"]
        header_line = " | ".join(columns)
        data_text.append(header_line)
        data_text.append("-" * len(header_line))

        # Adiciona as linhas de dados
        for row in data:
            row_values = [str(row.get(col, '')) for col in columns]
            data_text.append(" | ".join(row_values))
        
        return "\n".join(data_text)

    def _format_statistics_section(self, consolidated_data: Dict[str, Any]) -> str:
        """Gera a seção de estatísticas do relatório de texto."""
        statistics = consolidated_data.get("statistics", {})

        if not statistics:
            return "Nenhuma estatística disponível.\n"
        
        stats_text = ["Estatísticas:\n"]
        for column, metrics in statistics.items():
            stats_text.append(f"  - Coluna: {column}")
            min_val = metrics.get('min')
            max_val = metrics.get('max')
            blank_count = metrics.get('blank_count')

            stats_text.append(f"    Mínimo: {min_val if min_val is not None else 'N/A'}")
            stats_text.append(f"    Máximo: {max_val if max_val is not None else 'N/A'}")
            stats_text.append(f"    Nulos: {blank_count if blank_count is not None else 0}")
            stats_text.append("")  # Linha em branco para separar as métricas

        return "\n".join(stats_text)
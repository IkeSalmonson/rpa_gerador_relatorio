# gerador_relatorio/sales_report/html_report_formatter.py

"""
Este módulo define a classe HTMLReportFormatter para formatar relatórios em HTML.
"""

from typing import Dict, Any, List
from gerador_relatorio.sales_report.report_formatter import ReportFormatter

class HTMLReportFormatter(ReportFormatter):
    """
    Formatador de relatório para HTML.
    """

    def format_report(self, consolidated_data: Dict[str, Any]) -> str:
        """
        Formata os dados e as estatísticas de vendas em um relatório HTML completo.

        Args:
            consolidated_data (Dict[str, Any]): Dicionário com os dados consolidados,
                                                incluindo 'data', 'statistics' e 'header_map'.

        Returns:
            str: O relatório em formato HTML.
        """
        html_content = [
            "<!DOCTYPE html>",
            "<html lang='pt-BR'>",
            "<head>",
            "    <meta charset='UTF-8'>",
            "    <title>Relatório de Vendas</title>",
            "    <style>",
            "        body { font-family: sans-serif; margin: 20px; }",
            "        h1, h2 { color: #333; }",
            "        table { width: 100%; border-collapse: collapse; margin-top: 20px; }",
            "        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }",
            "        th { background-color: #f2f2f2; }",
            "        .statistics-section { margin-top: 40px; }",
            "        .statistics-table { width: auto; }",
            "    </style>",
            "</head>",
            "<body>",
            "    <h1>Relatório de Vendas</h1>",
            self._format_data_table(consolidated_data),
            self._format_statistics_section(consolidated_data),
            "</body>",
            "</html>"
        ]
        return "\n".join(html_content)

    def _format_data_table(self, consolidated_data: Dict[str, Any]) -> str:
        """Gera a tabela de dados HTML."""
        data = consolidated_data.get("data", [])
        header_map = consolidated_data.get("header_map", {})
        
        if not data:
            return "<p>Nenhum dado de vendas disponível.</p>"

        columns = list(header_map.keys())
        table_html = ["    <h2>Dados de Vendas</h2>", "    <table>"]
        
        # Cabeçalho da tabela
        table_html.append("        <thead>")
        table_html.append("            <tr>")
        for col in columns:
            table_html.append(f"                <th>{col}</th>")
        table_html.append("            </tr>")
        table_html.append("        </thead>")
        
        # Corpo da tabela
        table_html.append("        <tbody>")
        for row in data:
            table_html.append("            <tr>")
            for col in columns:
                value = row.get(col, '')
                table_html.append(f"                <td>{value}</td>")
            table_html.append("            </tr>")
        table_html.append("        </tbody>")
        
        table_html.append("    </table>")
        return "\n".join(table_html)
    
    def _format_statistics_section(self, consolidated_data: Dict[str, Any]) -> str:
        """Gera a seção de estatísticas HTML."""
        statistics = consolidated_data.get("statistics", {})

        if not statistics:
            return "<p class='statistics-section'>Nenhuma estatística disponível.</p>"

        stats_html = ["    <div class='statistics-section'>", "        <h2>Estatísticas</h2>", "        <table class='statistics-table'>", "            <thead>", "                <tr>", "                    <th>Métrica</th>", "                    <th>Mínimo</th>", "                    <th>Máximo</th>", "                    <th>Contagem de Nulos</th>", "                </tr>", "            </thead>", "            <tbody>"]

        for column, metrics in statistics.items():
            min_val = metrics.get('min', 'N/A')
            max_val = metrics.get('max', 'N/A')
            blank_count = metrics.get('blank_count', 0)
            
            stats_html.append("                <tr>")
            stats_html.append(f"                    <td>{column}</td>")
            stats_html.append(f"                    <td>{min_val}</td>")
            stats_html.append(f"                    <td>{max_val}</td>")
            stats_html.append(f"                    <td>{blank_count}</td>")
            stats_html.append("                </tr>")
        
        stats_html.append("            </tbody>")
        stats_html.append("        </table>")
        stats_html.append("    </div>")

        return "\n".join(stats_html)
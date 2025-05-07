import json
from unittest.mock import mock_open, patch
 
from gerador_relatorios.main import main
import io  # Para capturar stdout

def test_config_file_not_found(capsys):
    with patch("builtins.open", side_effect=FileNotFoundError):
        main()
        captured = capsys.readouterr()
        assert "Erro: Arquivo de configuração 'config.json' não encontrado." in captured.out

def test_config_file_invalid_json(capsys):
    with patch("builtins.open", mock_open(read_data="invalid json")):
        with patch("json.load", side_effect=json.JSONDecodeError("msg", "doc", 0)):
            main()
            captured = capsys.readouterr()
            assert "Erro: Arquivo de configuração 'config.json' inválido." in captured.out

def test_config_file_valid(capsys):
    valid_config = {"sources": [{"type": "local", "location": "test.csv"}]}  # Configuração válida
    with patch("builtins.open", mock_open(read_data=json.dumps(valid_config))):
        with patch("json.load", return_value=valid_config):
            with patch("gerador_relatorios.data_source.data_source.LocalDataSource.extract_data", return_value=[{"col1": "val1"}]):  # Mock extract_data
                main()
                captured = capsys.readouterr()
                assert "Relatório HTML:" in captured.out
                assert "Relatório Texto:" in captured.out
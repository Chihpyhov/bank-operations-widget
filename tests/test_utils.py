import json
from unittest.mock import patch, mock_open
from src.utils import read_json_file

def test_read_json_file_returns_list(tmp_path):
    file = tmp_path / "test.json"
    file.write_text(json.dumps([{"id": 1}, {"id": 2}]), encoding="utf-8")
    assert read_json_file(str(file)) == [{"id": 1}, {"id": 2}]

def test_read_json_file_not_list(tmp_path):
    file = tmp_path / "test.json"
    file.write_text(json.dumps({"not": "list"}), encoding="utf-8")
    assert read_json_file(str(file)) == []

def test_read_json_file_empty(tmp_path):
    file = tmp_path / "test.json"
    file.write_text("", encoding="utf-8")
    assert read_json_file(str(file)) == []

def test_read_json_file_not_found():
    assert read_json_file("nonexistent.json") == []

def test_read_json_file_mock_open():
    with patch("builtins.open", mock_open(read_data='[{"id": 1}]')) as mocked_open:
        result = read_json_file("dummy.json")
        assert result == [{"id": 1}]
        mocked_open.assert_called_once_with("dummy.json", "r", encoding="utf-8")

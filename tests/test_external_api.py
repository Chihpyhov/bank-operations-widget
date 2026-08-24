from unittest.mock import patch, Mock
from src.external_api import convert_to_rub

def test_convert_to_rub_rub():
    transaction = {
        "operationAmount": {
            "amount": "100.50",
            "currency": {"code": "RUB"}
        }
    }
    assert convert_to_rub(transaction) == 100.50

@patch("src.external_api.requests.get")
def test_convert_to_rub_usd(mock_get):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"result": 7500.75}
    mock_get.return_value = mock_response

    transaction = {
        "operationAmount": {
            "amount": "100.0",
            "currency": {"code": "USD"}
        }
    }
    assert convert_to_rub(transaction) == 7500.75
    mock_get.assert_called_once()

@patch("src.external_api.requests.get")
def test_convert_to_rub_eur(mock_get):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"result": 9000.0}
    mock_get.return_value = mock_response

    transaction = {
        "operationAmount": {
            "amount": "100.0",
            "currency": {"code": "EUR"}
        }
    }
    assert convert_to_rub(transaction) == 9000.0

@patch("src.external_api.requests.get")
def test_convert_to_rub_api_error(mock_get):
    mock_response = Mock()
    mock_response.status_code = 404
    mock_get.return_value = mock_response

    transaction = {
        "operationAmount": {
            "amount": "50.0",
            "currency": {"code": "USD"}
        }
    }
    assert convert_to_rub(transaction) == 0.0

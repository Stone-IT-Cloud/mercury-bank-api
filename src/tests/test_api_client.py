# nosec B101
"""
Mercury Bank API Testing Module

This module contains unit tests for the Mercury Bank API client implementation.
It tests various functionalities of the API client including:
- Account operations (get accounts, get account by ID)
- Card operations (get cards)
- Transaction operations (get/create transactions)
- Statement operations (get statements)
- Money transfer operations (send money requests)

The tests use pytest and mock external API calls using unittest.mock.
Environment variables are loaded from .env file for test configuration.

Dependencies:
    - pytest
    - python-dotenv
    - requests
    - mercury_api (local package)

Environment Variables:
    TEST_MERCURY_API_TOKEN: API token for Mercury Bank test environment
"""

import os
from datetime import date
from unittest.mock import MagicMock, patch

import pytest
from dotenv import load_dotenv

from mercury_api.api_client import MercuryApiClient
from mercury_api.transactions_data_models import (
    NewTransactionPayload,
    TransactionParams,
)

# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
load_dotenv()
TOKEN = os.getenv("TEST_MERCURY_API_TOKEN")


@pytest.fixture
def client():
    """Return a configured MercuryApiClient instance.

    The client is initialized with a predefined TOKEN for authentication.

    Returns:
        MercuryApiClient: A configured API client instance ready to make requests to Mercury's API.
    """
    return MercuryApiClient(token=TOKEN)


@patch("mercury_api.api_client.requests.get")
def test_get_accounts(mock_get, api_client):
    """Test the get_accounts method of the API client.

    This test verifies that the client's get_accounts method correctly processes
    the API response and returns a list of account objects with proper attributes.
    """
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "accounts": [{"id": "1", "name": "Test Account"}]
    }
    mock_get.return_value = mock_response

    accounts = api_client.get_accounts()
    assert len(accounts) == 1
    assert accounts[0].id == "1"
    assert accounts[0].name == "Test Account"


@patch("mercury_api.api_client.requests.get")
def test_get_account_by_id(mock_get, api_client):
    """Test retrieving an account by its ID.

    This test verifies that the get_account_by_id method correctly retrieves
    an account when given a valid account ID.
    """
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "accounts": [{"id": "1", "name": "Test Account"}]
    }
    mock_get.return_value = mock_response

    api_client.get_accounts()
    account = api_client.get_account_by_id("1")
    assert account is not None
    assert account.id == "1"


@patch("mercury_api.api_client.requests.get")
def test_get_cards(mock_get, api_client):
    """Test the get_cards method of the API client.

    This test verifies that the get_cards method correctly processes the API response
    and returns a list of Card objects with the expected properties.
    """
    mock_response = MagicMock()
    mock_response.json.return_value = {"cards": [{"id": "1", "name": "Test Card"}]}
    mock_get.return_value = mock_response

    cards = api_client.get_cards("1")
    assert len(cards) == 1
    assert cards[0].id == "1"
    assert cards[0].name == "Test Card"


@patch("mercury_api.api_client.requests.get")
def test_get_transactions(mock_get, api_client):
    """Test the get_transactions method of the Mercury API client.

    This test verifies that the API client correctly retrieves and parses transaction data
    from the Mercury API. It mocks the HTTP GET request and checks if the response is
    properly converted into Transaction objects.
    """
    mock_response = MagicMock()
    mock_response.json.return_value = {"transactions": [{"id": "1", "amount": 100}]}
    mock_get.return_value = mock_response

    params = TransactionParams(
        limit=10,
        offset=0,
        status="completed",
        start=date.today(),
        end=date.today(),
        search="",
    )
    transactions = api_client.get_transactions("1", params)
    assert len(transactions) == 1
    assert transactions[0].id == "1"
    assert transactions[0].amount == 100


@patch("mercury_api.api_client.requests.get")
def test_get_transaction_by_id(mock_get, api_client):
    """Test the get_transaction_by_id method of the API client.

    This test verifies that the get_transaction_by_id method correctly retrieves
    and parses a transaction from the API response.
    """
    mock_response = MagicMock()
    mock_response.json.return_value = {"id": "1", "amount": 100}
    mock_get.return_value = mock_response

    transaction = api_client.get_transaction_by_id("1", "1")
    assert transaction is not None
    assert transaction.id == "1"
    assert transaction.amount == 100


@patch("mercury_api.api_client.requests.get")
def test_get_statements(mock_get, api_client):
    """Test the get_statements method of the Mercury API client.

    This test verifies that the client correctly retrieves account statements
    within a specified date range and processes the response data.
    """
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "statements": [
            {"id": "1", "period_start": "2023-01-01", "period_end": "2023-01-31"}
        ]
    }
    mock_get.return_value = mock_response

    statements = api_client.get_statements(
        "1", start=date(2023, 1, 1), end=date(2023, 1, 31)
    )
    assert len(statements) == 1
    assert statements[0].id == "1"


@patch("mercury_api.api_client.requests.post")
def test_create_transaction(mock_post, api_client):
    """Test create_transaction method of API client.

    This test verifies that the create_transaction method correctly creates a new transaction
    with the given payload and returns the expected Transaction object.
    """
    mock_response = MagicMock()
    mock_response.json.return_value = {"id": "1", "amount": 100}
    mock_post.return_value = mock_response

    payload = NewTransactionPayload(amount=100, description="Test Transaction")
    transaction = api_client.create_transaction("1", payload)
    assert transaction is not None
    assert transaction.id == "1"
    assert transaction.amount == 100


@patch("mercury_api.api_client.requests.post")
def test_request_send_money(mock_post, api_client):
    """Test the request_send_money method of the API client.

    This test verifies that the request_send_money method correctly processes the API response
    and returns the expected Transaction object.
    """
    mock_response = MagicMock()
    mock_response.json.return_value = {"id": "1", "amount": 100}
    mock_post.return_value = mock_response

    payload = NewTransactionPayload(amount=100, description="Send Money")
    transaction = api_client.request_send_money("1", payload)
    assert transaction is not None
    assert transaction.id == "1"
    assert transaction.amount == 100

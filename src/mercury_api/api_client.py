"""
This module provides a client for interacting with the Mercury API.

Classes:
    MercuryApiClient: A client for making requests to the Mercury API.

Usage example:
    client = MercuryApiClient(token="your_api_token")
    accounts = client.get_account()

Dependencies:
    requests: HTTP library for making requests.
    mercury_api.data_models: Contains data models for the API responses.
"""

from datetime import date
from typing import List, Literal

import requests
from requests.models import Response

from mercury_api.transactions_data_models import (
    Account,
    AccountsResponse,
    Card,
    NewTransaction,
    NewTransactionPayload,
    Statement,
    Transaction,
    TransactionApprovalRequest,
    TransactionParams,
)


class MercuryApiClient:
    """MercuryApiClient is a client for interacting with the Mercury API.

    Attributes:
        _token (str): The authentication token for the API.
        accounts (List[Account]): A list of Account objects retrieved from the API.
        base_url (str): The base URL for the Mercury API.

    Methods:
        __init__(self, token, base_url=None):
            Initializes the MercuryApiClient with the provided token and optional base URL.

        _make_request(self, url: str, timeout: int = 10) -> Response:
            Makes a GET request to the specified URL with the provided timeout.

        get_accounts(self) -> AccountsResponse:

        get_account_by_id(self, account_id: str) -> Account:
            Retrieves account information for a specific account ID from the API.

        get_cards(self, account_id: str) -> List[Card]:

        get_transactions(
            start: date = None,
            end: date = None,
            Retrieves a list of transactions for a specific account.

        get_transaction_by_id(self, account_id: str, transaction_id: str) -> Transaction:
            Retrieves a specific transaction for a given account.

        get_statements(self, account_id: str, start: date = None, end: date = None) -> List[Statement]:
            Retrieves account statements for a given account ID within a specified date range.
    """

    _token = None
    accounts: List[Account] = []
    base_url = "https://api.mercury.com"

    def __init__(self, token, base_url=None):
        self._token = token
        if base_url:
            self.base_url = base_url

    def _make_request(
        self,
        url: str,
        timeout: int = 10,
        request_type: Literal["get", "post"] = "get",
        payload: any = None,
    ) -> Response:
        headers = {
            "Authorization": f"Bearer {self._token}",
            "accept": "application/json",
        }
        if request_type == "get":
            resp = requests.get(url, headers=headers, timeout=timeout)
            return resp

        if not payload or not payload.__dict__:
            raise ValueError(
                "Payload is required for POST requests and cannot be empty."
            )

        resp = requests.post(
            url, headers=headers, timeout=timeout, json=payload.__dict__
        )

        return resp

    def get_accounts(self) -> AccountsResponse:
        """
        Retrieves account information from the API.

        Makes a GET request to the accounts endpoint of the API and parses the response
        into an AccountsResponse object.

        Returns:
            AccountsResponse: An object containing the account information retrieved from the API.
        """
        if len(self.accounts) > 0:
            return self.accounts

        url = f"{self.base_url}/api/v1/accounts"
        response = self._make_request(url).json()
        for account in response["accounts"]:
            account = Account(**account)
            self.accounts.append(account)
        return self.accounts

    def get_account_by_id(self, account_id: str) -> Account:
        """
        Retrieves account information from the API.

        Makes a GET request to the accounts endpoint of the API and parses the response
        into an Account object.

        Returns:
            Account: An object containing the account information retrieved from the API.
        """
        if len(self.accounts) == 0:
            accounts = self.get_accounts()
            if len(accounts) == 0:
                return None

        for account in self.accounts:
            if account.id == account_id:
                return account
        return None

    def get_cards(self, account_id: str) -> List[Card]:
        """
        Retrieves card information for a specific account from the API.

        Makes a GET request to the cards endpoint of the API for a specific account
        and parses the response into a list of Card objects.

        Args:
            account_id (str): The ID of the account for which to retrieve card information.

        Returns:
            List[Card]: A list of Card objects containing the card information for the account.
        """
        url = f"{self.base_url}/api/v1/account/{account_id}/cards"
        response = self._make_request(url).json()
        print(response)
        cards: List[Card] = [Card(**card) for card in response["cards"]]
        return cards

    def get_transactions(
        self,
        account_id: str,
        params: TransactionParams,
    ) -> List[Transaction]:
        """
        Retrieve a list of transactions for a specific account.

        Args:
            account_id (str): The ID of the account to retrieve transactions for.
            params (TransactionParams): A TransactionParams object containing the query parameters

        Returns:
            List[Transaction]: A list of Transaction objects retrieved from the account.

        Raises:
            HTTPError: If the request to the API fails.
        """
        url = f"{self.base_url}/api/v1/account/{account_id}/transactions?"
        query_params = {
            "limit": params.limit,
            "offset": params.offset,
            "status": params.status,
            "start": params.start,
            "end": params.end,
            "search": params.search,
        }
        for key, value in query_params.items():
            if value:
                url += f"&{key}={value}"
        url = url.replace("?&", "?")
        response = self._make_request(url).json()
        print(url, response)
        transactions: List[Transaction] = [
            Transaction(**transaction) for transaction in response["transactions"]
        ]
        return transactions

    def get_transaction_by_id(
        self, account_id: str, transaction_id: str
    ) -> Transaction:
        """
        Retrieve a specific transaction for a given account.

        Args:
            account_id (str): The ID of the account to retrieve the transaction from.
            transaction_id (str): The ID of the transaction to retrieve.

        Returns:
            Transaction: The Transaction object representing the requested transaction.
        """
        url = (
            f"{self.base_url}/api/v1/account/{account_id}/transaction/{transaction_id}"
        )
        response = self._make_request(url).json()
        transaction = Transaction(**response)
        return transaction

    def get_statements(
        self, account_id: str, start: date = None, end: date = None
    ) -> List[Statement]:
        """
        Retrieve account statements for a given account ID within a specified date range.
        Args:
            account_id (str): The ID of the account to retrieve statements for.
            start (date, optional): The start date for the statements. Defaults to None.
            end (date, optional): The end date for the statements. Defaults to None.
        Returns:
            List[Statement]: A list of Statement objects representing the account statements.
        Raises:
            HTTPError: If the request to the API fails.
        """

        url = f"{self.base_url}/api/v1/account/{account_id}/statements?"
        if start:
            url += f"&start={start}"
        if end:
            url += f"&end={end}"
        url = url.replace("?&", "?")
        if not start and not end:
            url = url.replace("?", "")

        response = self._make_request(url).json()
        statements: List[Statement] = [
            Statement(**statement) for statement in response["statements"]
        ]
        return statements

    def create_transaction(
        self, account_id: str, transaction: NewTransactionPayload
    ) -> NewTransaction:
        """
        Create a new transaction for a given account.

        Args:
            account_id (str): The ID of the account to create the transaction for.
            transaction (Transaction): The Transaction object representing the new transaction.

        Returns:
            Transaction: The Transaction object representing the created transaction.
        """
        url = f"{self.base_url}/api/v1/account/{account_id}/transactions"
        response = self._make_request(
            url, request_type="post", payload=transaction
        ).json()
        return Transaction(**response)

    def request_send_money(
        self, account_id: str, transaction: NewTransactionPayload
    ) -> TransactionApprovalRequest:
        """
        Request to send money to a specific account. Only ACH is supported

        Args:
            account_id (str): The ID of the account to send money to.
            transaction (Transaction): The Transaction object representing the transaction.

        Returns:
            Transaction: The Transaction object representing the requested transaction.
        """
        url = f"{self.base_url}/api/v1/account/{account_id}/send_money"
        response = self._make_request(
            url, request_type="post", payload=transaction
        ).json()
        return Transaction(**response)

"""
Mercury API package initializer.

This module initializes the mercury_api package by importing the necessary
submodules and defining the package's version and public API.

Submodules:
    api_client: Handles API client functionality.
    data_models: Contains data models used by the API.

Attributes:
    __version__ (str): The version of the mercury_api package.
    __all__ (list): A list of public objects of the mercury_api package.
"""

from . import api_client, transactions_data_models

# mercury_api/__init__.py

__version__ = "0.1.0"


__all__ = ["api_client", "transactions_data_models"]

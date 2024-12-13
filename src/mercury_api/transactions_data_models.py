# pylint: disable=C0103,C0301,R0902,R0903
# flake8: noqa: E501
"""
This module defines data models for transactions and related entities in the Mercury Bank API.

Classes:
    Account: Represents a bank account with various attributes.
    AccountsResponse: Represents a response containing a list of accounts.
    Card: Represents a card with various attributes.
    CardsResponse: Represents a response containing a list of cards.
    Address: Represents an address with optional fields.
    DomesticWireRoutingInfo: Represents domestic wire routing information.
    ElectronicRoutingInfo: Represents electronic routing information.
    CorrespondentInfo: Represents correspondent bank information.
    BankDetails: Represents bank details including name, city/state, and country.
    InternationalWireRoutingInfo: Represents international wire routing information.
    DebitCardInfo: Represents debit card information.
    CreditCardInfo: Represents credit card information.
    CurrencyExchangeInfo: Represents currency exchange information.
    Attachment: Represents an attachment with a file name, URL, and type.
    Details: Represents detailed information for a transaction.
    TransactionParams: Represents parameters for querying transactions.
    Transaction: Represents a transaction with various attributes.
    TransactionsResponse: Represents a response containing a list of transactions.
    CompanyLegalAddress: Represents a company's legal address.
    StatementTransaction: Represents a transaction within a statement.
    Statement: Represents a bank statement with various attributes.
    StatementsResponse: Represents a response containing a list of statements.
    AddressDetail: Represents detailed address information.
    InternationalAddressDetail: Represents detailed international address information.
    DomesticWireRoutingInfoDetail: Represents detailed domestic wire routing information.
    ElectronicRoutingInfoDetail: Represents detailed electronic routing information.
    CorrespondentInfoDetail: Represents detailed correspondent bank information.
    BankDetailsDetail: Represents detailed bank information.
    CountrySpecificDataCanada: Represents country-specific data for Canada.
    CountrySpecificDataAustralia: Represents country-specific data for Australia.
    CountrySpecificDataIndia: Represents country-specific data for India.
    CountrySpecificDataRussia: Represents country-specific data for Russia.
    CountrySpecificDataPhilippines: Represents country-specific data for the Philippines.
    CountrySpecificDataSouthAfrica: Represents country-specific data for South Africa.
    CountrySpecificDataDetail: Represents detailed country-specific data.
    InternationalWireRoutingInfoDetail: Represents detailed international wire routing information.
    DetailsDetail: Represents detailed information for a new transaction.
    NewTransaction: Represents a new transaction with various attributes.
    NewTransactionPayload: Represents the payload for creating a new transaction.
    TransactionApprovalRequest: Represents a request for transaction approval.
"""

from dataclasses import dataclass
from datetime import date, datetime
from typing import List, Literal, Optional


@dataclass
class Account:
    """
    Represents a bank account with various attributes.

    Attributes:
        accountNumber (str): The account number of the bank account.
        availableBalance (float): The available balance in the account.
        createdAt (datetime): The date and time when the account was created.
        currentBalance (float): The current balance in the account.
        id (str): The unique identifier for the account.
        kind (str): The kind of account.
        name (str): The name associated with the account.
        routingNumber (str): The routing number of the bank account.
        status (Literal["active", "deleted", "pending", "archived"]): The status of the account.
        type (Literal["mercury", "external", "recipient"]): The type of account.
        legalBusinessName (str): The legal business name associated with the account.
        dashboardLink (str): The link to the account's dashboard.
        canReceiveTransactions (Optional[bool]): Indicates if the account can receive transactions. Defaults to None.
        nickname (Optional[str]): The nickname for the account. Defaults to None.
    """

    accountNumber: str
    availableBalance: float
    createdAt: datetime
    currentBalance: float
    id: str
    kind: str
    name: str
    routingNumber: str
    status: Literal["active", "deleted", "pending", "archived"]
    type: Literal["mercury", "external", "recipient"]
    legalBusinessName: str
    dashboardLink: str
    canReceiveTransactions: Optional[bool] = None
    nickname: Optional[str] = None


@dataclass
class AccountsResponse:
    """
    A response model that contains a list of accounts.

    Attributes:
        accounts (List[Account]): A list of Account objects.
    """

    accounts: List[Account]


@dataclass
class Card:
    """
    Represents a Credit Card query.

    Attributes:
        cardId (str): The unique identifier for the card.
        createdAt (datetime): The date and time when the card was created.
        lastFourDigits (str): The last four digits of the card number.
        nameOnCard (str): The name printed on the card.
        network (Literal["visa", "mastercard"]): The card network, either 'visa' or 'mastercard'.
        status (Literal["active", "frozen", "cancelled", "inactive", "locked", "expired"]): The current status of the card.
        physicalCardStatus (Optional[Literal["active", "inactive", "locked"]]): The status of the physical card, if applicable. Defaults to None.
    """

    cardId: str
    createdAt: datetime
    lastFourDigits: str
    nameOnCard: str
    network: Literal["visa", "mastercard"]
    status: Literal["active", "frozen", "cancelled", "inactive", "locked", "expired"]
    physicalCardStatus: Optional[Literal["active", "inactive", "locked"]] = None


@dataclass
class CardsResponse:
    """
    CardsResponse is a data model representing the response containing a list of cards.

    Attributes:
        cards (List[Card]): A list of Card objects.
    """

    cards: List[Card]


@dataclass
class Address:
    """
    Represents a physical address.

    Attributes:
        address1 (str): The primary address line.
        address2 (Optional[str]): The secondary address line (e.g., apartment, suite, unit, building, floor, etc.).
        city (str): The city of the address.
        state (Optional[str]): The state or province of the address.
        postalCode (str): The postal code of the address.
    """

    address1: str
    address2: Optional[str]
    city: str
    state: Optional[str]
    postalCode: str


@dataclass
class DomesticWireRoutingInfo:
    """
    Represents the routing information for a domestic wire transfer.

    Attributes:
        bankName (Optional[str]): The name of the bank.
        accountNumber (str): The account number for the wire transfer.
        routingNumber (str): The routing number for the wire transfer.
        address (Optional[Address]): The address associated with the bank account.
    """

    bankName: Optional[str]
    accountNumber: str
    routingNumber: str
    address: Optional[Address]


@dataclass
class ElectronicRoutingInfo:
    """
    ElectronicRoutingInfo is a data model representing the electronic routing information for a bank account.

    Attributes:
        accountNumber (str): The account number associated with the bank account.
        routingNumber (str): The routing number associated with the bank account.
        bankName (Optional[str]): The name of the bank. This attribute is optional.
    """

    accountNumber: str
    routingNumber: str
    bankName: Optional[str]


@dataclass
class CorrespondentInfo:
    """
    CorrespondentInfo class represents the information about a correspondent bank.

    Attributes:
        routingNumber (Optional[str]): The routing number of the correspondent bank.
        swiftCode (Optional[str]): The SWIFT code of the correspondent bank.
        bankName (Optional[str]): The name of the correspondent bank.
    """

    routingNumber: Optional[str]
    swiftCode: Optional[str]
    bankName: Optional[str]


@dataclass
class BankDetails:
    """
    A class to represent bank details.

    Attributes:
        bankName (str): The name of the bank.
        cityState (str): The city and state where the bank is located.
        country (str): The country where the bank is located.
    """

    bankName: str
    cityState: str
    country: str


@dataclass
class InternationalWireRoutingInfo:
    """
    Represents the routing information for an international wire transfer.

    Attributes:
        iban (str): The International Bank Account Number.
        swiftCode (str): The SWIFT/BIC code of the bank.
        correspondentInfo (Optional[CorrespondentInfo]): Information about the correspondent bank.
        bankDetails (Optional[BankDetails]): Details about the bank.
        address (Optional[Address]): The address of the bank.
        phoneNumber (Optional[str]): The phone number of the bank.
        countrySpecific (Optional[dict]): Country-specific routing information.
    """

    iban: str
    swiftCode: str
    correspondentInfo: Optional[CorrespondentInfo]
    bankDetails: Optional[BankDetails]
    address: Optional[Address]
    phoneNumber: Optional[str]
    countrySpecific: Optional[dict]


@dataclass
class DebitCardInfo:
    """
    Class representing information about a debit card.

    Attributes:
        id (str): The unique identifier for the debit card.
    """

    id: str


@dataclass
class CreditCardInfo:
    """
    Class representing credit card information.

    Attributes:
        id (str): The unique identifier for the credit card.
    """

    id: str


@dataclass
class CurrencyExchangeInfo:
    """
    A class to represent information about a currency exchange transaction.

    Attributes:
        convertedFromCurrency (str): The currency code from which the amount is converted.
        convertedToCurrency (str): The currency code to which the amount is converted.
        convertedFromAmount (float): The amount of money in the original currency.
        convertedToAmount (float): The amount of money in the target currency after conversion.
        feeAmount (float): The fee amount charged for the currency exchange.
        feePercentage (float): The percentage of the fee charged for the currency exchange.
        exchangeRate (float): The exchange rate applied for the currency conversion.
        feeTransactionId (str): The transaction ID associated with the fee.
    """

    convertedFromCurrency: str
    convertedToCurrency: str
    convertedFromAmount: float
    convertedToAmount: float
    feeAmount: float
    feePercentage: float
    exchangeRate: float
    feeTransactionId: str


@dataclass
class Attachment:
    """
    Represents an attachment with a file name, URL, and type.

    Attributes:
        fileName (str): The name of the file.
        url (str): The URL where the attachment can be accessed.
        attachmentType (Literal["checkImage", "receipt", "other"]): The type of the attachment.
    """

    fileName: str
    url: str
    attachmentType: Literal["checkImage", "receipt", "other"]


@dataclass
class Details:
    """
    A class to represent the details of a transaction.

    Attributes:
    ----------
    address : Optional[Address]
        The address associated with the transaction.
    domesticWireRoutingInfo : Optional[DomesticWireRoutingInfo]
        Information for domestic wire routing.
    electronicRoutingInfo : Optional[ElectronicRoutingInfo]
        Information for electronic routing.
    internationalWireRoutingInfo : Optional[InternationalWireRoutingInfo]
        Information for international wire routing.
    debitCardInfo : Optional[DebitCardInfo]
        Information for debit card transactions.
    creditCardInfo : Optional[CreditCardInfo]
        Information for credit card transactions.
    """

    address: Optional[Address]
    domesticWireRoutingInfo: Optional[DomesticWireRoutingInfo]
    electronicRoutingInfo: Optional[ElectronicRoutingInfo]
    internationalWireRoutingInfo: Optional[InternationalWireRoutingInfo]
    debitCardInfo: Optional[DebitCardInfo]
    creditCardInfo: Optional[CreditCardInfo]


class TransactionParams:
    """
    TransactionParams is a data model that defines the parameters for querying transactions.

    Attributes:
        limit (int): The maximum number of transactions to return. Default is 500.
        offset (int): The number of transactions to skip before starting to collect the result set. Default is 0.
        status (Literal["pending", "sent", "cancelled", "failed"]): The status of the transactions to filter by. Default is None.
        start (date): The start date for the transaction query in YYYY-MM-DD format or an ISO 8601 string. Default is None.
        end (date): The end date for the transaction query in YYYY-MM-DD format or an ISO 8601 string. Default is None.
        search (str): A search string to filter transactions. Default is None.
    """

    limit: int = 500
    offset: int = 0
    status: Literal["pending", "sent", "cancelled", "failed"] = None
    start: Optional[date] = None  # Format: YYYY-MM-DD or an ISO 8601 string
    end: Optional[date] = None  # Format: YYYY-MM-DD or an ISO 8601 string
    search: Optional[str] = None


@dataclass
class Transaction:
    """
    Represents a financial transaction.

    Attributes:
        amount (float): The amount of the transaction.
        bankDescription (Optional[str]): Description provided by the bank.
        counterpartyId (str): Identifier for the counterparty.
        counterpartyName (str): Name of the counterparty.
        counterpartyNickname (Optional[str]): Nickname of the counterparty.
        createdAt (datetime): Timestamp when the transaction was created.
        dashboardLink (str): Link to the transaction on the dashboard.
        details (Optional[Details]): Additional details about the transaction.
        estimatedDeliveryDate (datetime): Estimated date of delivery for the transaction.
        failedAt (Optional[datetime]): Timestamp when the transaction failed, if applicable.
        id (str): Unique identifier for the transaction.
        kind (Literal): Type of the transaction. Possible values include:
            - "externalTransfer"
            - "internalTransfer"
            - "outgoingPayment"
            - "creditCardCredit"
            - "creditCardTransaction"
            - "debitCardTransaction"
            - "incomingDomesticWire"
            - "checkDeposit"
            - "incomingInternationalWire"
            - "treasuryTransfer"
            - "wireFee"
            - "other"
        note (Optional[str]): Additional note for the transaction.
        externalMemo (Optional[str]): External memo associated with the transaction.
        postedAt (Optional[datetime]): Timestamp when the transaction was posted.
        reasonForFailure (Optional[str]): Reason for the transaction failure, if applicable.
        status (Literal): Status of the transaction. Possible values include:
            - "pending"
            - "sent"
            - "cancelled"
            - "failed"
        feeId (Optional[str]): Identifier for any associated fee.
        currencyExchangeInfo (Optional[CurrencyExchangeInfo]): Information about currency exchange, if applicable.
        compliantWithReceiptPolicy (Optional[bool]): Indicates if the transaction complies with receipt policy.
        hasGeneratedReceipt (Optional[bool]): Indicates if a receipt has been generated for the transaction.
        creditAccountPeriodId (Optional[str]): Identifier for the credit account period.
        mercuryCategory (Optional[str]): Category assigned by Mercury.
        generalLedgerCodeName (Optional[str]): Name of the general ledger code.
        attachments (List[Attachment]): List of attachments associated with the transaction.
    """

    amount: float
    bankDescription: Optional[str]
    counterpartyId: str
    counterpartyName: str
    counterpartyNickname: Optional[str]
    createdAt: datetime
    dashboardLink: str
    details: Optional[Details]
    estimatedDeliveryDate: datetime
    failedAt: Optional[datetime]
    id: str
    kind: Literal[
        "externalTransfer",
        "internalTransfer",
        "outgoingPayment",
        "creditCardCredit",
        "creditCardTransaction",
        "debitCardTransaction",
        "incomingDomesticWire",
        "checkDeposit",
        "incomingInternationalWire",
        "treasuryTransfer",
        "wireFee",
        "other",
    ]
    note: Optional[str]
    externalMemo: Optional[str]
    postedAt: Optional[datetime]
    reasonForFailure: Optional[str]
    status: Literal["pending", "sent", "cancelled", "failed"]
    feeId: Optional[str]
    currencyExchangeInfo: Optional[CurrencyExchangeInfo]
    compliantWithReceiptPolicy: Optional[bool]
    hasGeneratedReceipt: Optional[bool]
    creditAccountPeriodId: Optional[str]
    mercuryCategory: Optional[str]
    generalLedgerCodeName: Optional[str]
    attachments: List[Attachment]


@dataclass
class TransactionsResponse:
    """
    A class to represent the response containing transaction data.

    Attributes:
        total (int): The total number of transactions.
        transactions (List[Transaction]): A list of transaction objects.
    """

    total: int
    transactions: List[Transaction]


@dataclass
class CompanyLegalAddress:
    """
    Represents the legal address of a company.

    Attributes:
        address1 (str): The primary address line.
        address2 (str): The secondary address line.
        city (str): The city of the address.
        country (str): The country of the address.
        name (str): The name associated with the address.
        postalCode (str): The postal code of the address.
        region (str): The region or state of the address.
    """

    address1: str
    address2: str
    city: str
    country: str
    name: str
    postalCode: str
    region: str


@dataclass
class StatementTransaction:
    """
    Represents a transaction statement.

    Attributes:
        createdAt (Optional[datetime]): The date and time when the transaction was created.
        id (str): The unique identifier of the transaction.
        postedAt (Optional[datetime]): The date and time when the transaction was posted.
    """

    createdAt: Optional[datetime]
    id: str
    postedAt: Optional[datetime]


@dataclass
class Statement:
    """
    A class to represent a bank statement.

    Attributes:
    ----------
    id : str
        Unique identifier for the statement.
    accountNumber : str
        The account number associated with the statement.
    companyLegalAddress : CompanyLegalAddress
        The legal address of the company.
    companyLegalName : str
        The legal name of the company.
    ein : Optional[str]
        Employer Identification Number (EIN) of the company.
    endDate : datetime
        The end date of the statement period.
    endingBalance : float
        The ending balance of the account for the statement period.
    routingNumber : str
        The routing number of the bank.
    startDate : datetime
        The start date of the statement period.
    transactions : List[StatementTransaction]
        A list of transactions included in the statement.
    downloadUrl : str
        URL to download the statement.
    """

    id: str
    accountNumber: str
    companyLegalAddress: CompanyLegalAddress
    companyLegalName: str
    ein: Optional[str]
    endDate: datetime
    endingBalance: float
    routingNumber: str
    startDate: datetime
    transactions: List[StatementTransaction]
    downloadUrl: str


@dataclass
class StatementsResponse:
    """
    A class used to represent the response containing a list of statements.

    Attributes
    ----------
    statements : List[Statement]
        A list of Statement objects representing the statements in the response.
    """

    statements: List[Statement]


@dataclass
class AddressDetail:
    """
    AddressDetail represents the details of an address.

    Attributes:
        address1 (str): The primary address line.
        address2 (Optional[str]): The secondary address line (optional).
        city (str): The city of the address.
        state (Optional[str]): The 2-letter US state code (optional).
        postalCode (str): The postal code of the address.
    """

    address1: str
    address2: Optional[str]
    city: str
    state: Optional[str]  # 2-letter US state code
    postalCode: str


@dataclass
class InternationalAddressDetail:
    """
    Represents the details of an international address.

    Attributes:
        address1 (str): The primary address line.
        address2 (Optional[str]): The secondary address line (optional).
        city (str): The city of the address.
        region (str): The region or state of the address.
        postalCode (str): The postal code of the address.
        country (str): The country of the address in ISO 3166-1 alpha-2 format.
    """

    address1: str
    address2: Optional[str]
    city: str
    region: str
    postalCode: str
    country: str  # iso3166Alpha2


@dataclass
class DomesticWireRoutingInfoDetail:
    """
    Represents the details of domestic wire routing information.

    Attributes:
        bankName (Optional[str]): The name of the bank.
        accountNumber (str): The account number.
        routingNumber (str): The routing number.
        address (Optional[InternationalAddressDetail]): The address details.
    """

    bankName: Optional[str]
    accountNumber: str
    routingNumber: str
    address: Optional[InternationalAddressDetail]


@dataclass
class ElectronicRoutingInfoDetail:
    """
    ElectronicRoutingInfoDetail is a data model that represents the details of electronic routing information.

    Attributes:
        accountNumber (str): The account number associated with the electronic routing information.
        routingNumber (str): The routing number associated with the electronic routing information.
        bankName (Optional[str]): The name of the bank associated with the electronic routing information. This attribute is optional.
    """

    accountNumber: str
    routingNumber: str
    bankName: Optional[str]


@dataclass
class CorrespondentInfoDetail:
    """
    Class representing the details of a correspondent bank.

    Attributes:
        routingNumber (Optional[str]): The routing number of the correspondent bank.
        swiftCode (Optional[str]): The SWIFT code of the correspondent bank.
        bankName (Optional[str]): The name of the correspondent bank.
    """

    routingNumber: Optional[str]
    swiftCode: Optional[str]
    bankName: Optional[str]


@dataclass
class BankDetailsDetail:
    """
    Represents the details of a bank.

    Attributes:
        bankName (str): The name of the bank.
        cityState (str): The city and state where the bank is located.
        country (str): The country code in ISO 3166-1 alpha-2 format.
    """

    bankName: str
    cityState: str
    country: str  # iso3166Alpha2


@dataclass
class CountrySpecificDataCanada:
    """
    CountrySpecificDataCanada is a data model representing banking information specific to Canada.

    Attributes:
        bankCode (str): The code of the bank.
        transitNumber (str): The transit number associated with the bank.
    """

    bankCode: str
    transitNumber: str


@dataclass
class CountrySpecificDataAustralia:
    """
    A class to represent country-specific data for Australia.

    Attributes:
    ----------
    bsbCode : str
        The BSB (Bank State Branch) code, which is used to identify individual branches of a financial institution in Australia.
    """

    bsbCode: str


@dataclass
class CountrySpecificDataIndia:
    """
    CountrySpecificDataIndia is a data model representing country-specific information for India.

    Attributes:
        ifscCode (str): The IFSC code of the bank branch.
    """

    ifscCode: str


@dataclass
class CountrySpecificDataRussia:
    """
    CountrySpecificDataRussia is a data model representing country-specific information for Russia.

    Attributes:
        inn (str): The INN (Individual Taxpayer Number) for a Russian entity.
    """

    inn: str


@dataclass
class CountrySpecificDataPhilippines:
    """
    CountrySpecificDataPhilippines is a data model for storing country-specific information
    related to the Philippines.

    Attributes:
        routingNumber (str): The routing number specific to the Philippines.
    """

    routingNumber: str


@dataclass
class CountrySpecificDataSouthAfrica:
    """
    A class to represent country-specific data for South Africa.

    Attributes:
    ----------
    branchCode : str
        The branch code of the bank in South Africa.
    """

    branchCode: str


@dataclass
class CountrySpecificDataDetail:
    """
    CountrySpecificDataDetail holds optional country-specific data for various countries.

    Attributes:
        countrySpecificDataCanada (Optional[CountrySpecificDataCanada]): Data specific to Canada.
        countrySpecificDataAustralia (Optional[CountrySpecificDataAustralia]): Data specific to Australia.
        countrySpecificDataIndia (Optional[CountrySpecificDataIndia]): Data specific to India.
        countrySpecificDataRussia (Optional[CountrySpecificDataRussia]): Data specific to Russia.
        countrySpecificDataPhilippines (Optional[CountrySpecificDataPhilippines]): Data specific to the Philippines.
        countrySpecificDataSouthAfrica (Optional[CountrySpecificDataSouthAfrica]): Data specific to South Africa.
    """

    countrySpecificDataCanada: Optional[CountrySpecificDataCanada]
    countrySpecificDataAustralia: Optional[CountrySpecificDataAustralia]
    countrySpecificDataIndia: Optional[CountrySpecificDataIndia]
    countrySpecificDataRussia: Optional[CountrySpecificDataRussia]
    countrySpecificDataPhilippines: Optional[CountrySpecificDataPhilippines]
    countrySpecificDataSouthAfrica: Optional[CountrySpecificDataSouthAfrica]


@dataclass
class InternationalWireRoutingInfoDetail:
    """
    InternationalWireRoutingInfoDetail represents the details required for international wire routing.

    Attributes:
        iban (str): The International Bank Account Number.
        swiftCode (str): The SWIFT/BIC code of the bank.
        correspondentInfo (Optional[CorrespondentInfoDetail]): Information about the correspondent bank.
        bankDetails (Optional[BankDetailsDetail]): Details about the bank.
        address (Optional[InternationalAddressDetail]): The international address details.
        phoneNumber (Optional[str]): The phone number associated with the bank or account.
        countrySpecific (Optional[CountrySpecificDataDetail]): Country-specific data related to the transaction.
    """

    iban: str
    swiftCode: str
    correspondentInfo: Optional[CorrespondentInfoDetail]
    bankDetails: Optional[BankDetailsDetail]
    address: Optional[InternationalAddressDetail]
    phoneNumber: Optional[str]
    countrySpecific: Optional[CountrySpecificDataDetail]


@dataclass
class DetailsDetail:
    """
    DetailsDetail class represents detailed information about a transaction's details.

    Attributes:
        address (Optional[AddressDetail]): The address details associated with the transaction.
        domesticWireRoutingInfo (Optional[DomesticWireRoutingInfoDetail]): The domestic wire routing information.
        electronicRoutingInfo (Optional[ElectronicRoutingInfoDetail]): The electronic routing information.
        internationalWireRoutingInfo (Optional[InternationalWireRoutingInfoDetail]): The international wire routing information.
    """

    address: Optional[AddressDetail]
    domesticWireRoutingInfo: Optional[DomesticWireRoutingInfoDetail]
    electronicRoutingInfo: Optional[ElectronicRoutingInfoDetail]
    internationalWireRoutingInfo: Optional[InternationalWireRoutingInfoDetail]


@dataclass
class NewTransaction:
    """
    Represents a new transaction in the Mercury Bank API.

    Attributes:
        amount (float): The amount of the transaction.
        bankDescription (Optional[str]): A description provided by the bank.
        counterpartyId (str): The ID of the counterparty involved in the transaction.
        counterpartyName (str): The name of the counterparty.
        counterpartyNickname (Optional[str]): A nickname for the counterparty.
        createdAt (datetime): The timestamp when the transaction was created.
        dashboardLink (str): A link to the transaction on the dashboard.
        details (Optional[DetailsDetail]): Additional details about the transaction.
        estimatedDeliveryDate (datetime): The estimated delivery date of the transaction.
        failedAt (Optional[datetime]): The timestamp when the transaction failed, if applicable.
        id (str): The unique identifier for the transaction.
        kind (Literal): The type of transaction. Possible values are:
            - "externalTransfer"
            - "internalTransfer"
            - "outgoingPayment"
            - "debitCardTransaction"
            - "incomingDomesticWire"
            - "checkDeposit"
            - "incomingInternationalWire"
            - "fee"
            - "other"
        note (Optional[str]): A note associated with the transaction.
        externalMemo (Optional[str]): An external memo for the transaction.
        postedAt (Optional[datetime]): The timestamp when the transaction was posted.
        reasonForFailure (Optional[str]): The reason for the transaction failure, if applicable.
        status (Literal): The status of the transaction. Possible values are:
            - "pending"
            - "sent"
            - "cancelled"
            - "failed"
        feeId (Optional[str]): The ID of the fee associated with the transaction, if applicable.
    """

    amount: float
    bankDescription: Optional[str]
    counterpartyId: str
    counterpartyName: str
    counterpartyNickname: Optional[str]
    createdAt: datetime
    dashboardLink: str
    details: Optional[DetailsDetail]
    estimatedDeliveryDate: datetime
    failedAt: Optional[datetime]
    id: str
    kind: Literal[
        "externalTransfer",
        "internalTransfer",
        "outgoingPayment",
        "debitCardTransaction",
        "incomingDomesticWire",
        "checkDeposit",
        "incomingInternationalWire",
        "fee",
        "other",
    ]
    note: Optional[str]
    externalMemo: Optional[str]
    postedAt: Optional[datetime]
    reasonForFailure: Optional[str]
    status: Literal["pending", "sent", "cancelled", "failed"]
    feeId: Optional[str]


@dataclass
class NewTransactionPayload:
    """
    NewTransactionPayload is a data model representing the payload for creating a new transaction.

    Attributes:
        recipientId (str): The unique identifier of the transaction recipient.
        amount (float): The amount of money to be transferred.
        paymentMethod (Literal["ach"]): The method of payment, default is "ach".
        note (Optional[str]): An optional note for the transaction.
        externalMemo (Optional[str]): An optional external memo for the transaction.
        idempotencyKey (str): A unique key to ensure the idempotency of the transaction.
    """

    recipientId: str
    amount: float
    idempotencyKey: str
    paymentMethod: Literal["ach"] = "ach"
    note: Optional[str] = None
    externalMemo: Optional[str] = None


@dataclass
class TransactionApprovalRequest:
    """
    A data model representing a transaction approval request.

    Attributes:
        accountId (str): The ID of the account associated with the transaction.
        requestId (str): The unique ID of the approval request.
        recipientId (str): The ID of the recipient of the transaction.
        memo (Optional[str]): An optional memo or note associated with the transaction.
        paymentMethod (str): The method of payment for the transaction.
        amount (float): The amount of money involved in the transaction.
        status (Literal["pendingApproval", "approved", "rejected", "cancelled"]): The current status of the approval request.
    """

    accountId: str
    requestId: str
    recipientId: str
    memo: Optional[str]
    paymentMethod: str
    amount: float
    status: Literal["pendingApproval", "approved", "rejected", "cancelled"]

class OpenSandboxAccountRequest:
    name: str


class OpenSandboxAccountResponse:
    account_id: str


class CloseSandboxAccountRequest:
    account_id: str


class CloseSandboxAccountResponse:


class SandboxPayInRequest:
    account_id: str
    amount: 'MoneyValue'


class SandboxPayInResponse:
    balance: 'MoneyValue'

from decimal import Decimal
from datetime import datetime


class Client():
    def __init__(self, name: str, address: str, cpf: str, birth_date: int) -> None:
        self.name = name
        self.address = address
        self.cpf = cpf
        self.birth_date = birth_date
        self.client_since = datetime.today()


class History():
    def __init__(self) -> None:
        self.creation_date = datetime.today()
        self.transactions = []

    def get_history(self):
        return self.transactions


class BankAccount():
    _total_accounts = 0

    @staticmethod
    def get_total_accounts():
        return BankAccount._total_accounts

    def __init__(self, id: str, owner: Client, current_balance: Decimal, credit_card_limit: Decimal = 1500) -> None:
        self.id = id
        self.owner = owner
        self.current_balance = Decimal(current_balance)
        self.credit_card_limit = Decimal(credit_card_limit)
        self.history = History()
        BankAccount._total_accounts += 1

    def deposit(self, added_value):
        if added_value > 0:
            self.current_balance += added_value
            self.history.transactions.append({
                'action': 'deposit',
                'ammount': added_value,
                'type': type(self.current_balance)
            })
            return True
        else:
            raise ValueError(
                'An invalid ammount was given for the operation. Deposit values should be greater than zero')

    def withdraw(self, withdrawn_value):
        if withdrawn_value <= 0:
            raise ValueError(
                'An invalid ammount was given for the operation. Deposit values should be greater than zero')

        if withdrawn_value <= self.current_balance:
            self.current_balance -= withdrawn_value
            self.history.transactions.append({
                'action': 'withdraw',
                'ammount': withdrawn_value
            })
            return True

        else:
            raise ValueError('Withdraw ammount greater than account balance.')

    def show_balance(self):
        return {'account': self.id, 'balance': self.current_balance}

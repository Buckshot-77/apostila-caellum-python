from decimal import Decimal
from datetime import datetime


class Client():
    def __init__(self, name: str, address: str, cpf: str, birth_date: int) -> None:
        self.name = name
        self.address = address
        self.cpf = cpf
        self.birth_date = birth_date
        self.client_since = datetime.today()


class BankAccount():
    def __init__(self, id: str, owner: Client, current_balance: Decimal, credit_card_limit: Decimal = 1500) -> None:
        self.id = id
        self.owner = owner
        self.current_balance = Decimal(current_balance)
        self.credit_card_limit = Decimal(credit_card_limit)

    def deposit(self, added_value):
        if added_value > 0:
            self.current_balance += Decimal(added_value)
        else:
            raise ValueError(
                'An invalid ammount was given for the operation. Deposit values should be greater than zero')

    def withdraw(self, withdrawn_value):
        if withdrawn_value <= 0:
            raise ValueError(
                'An invalid ammount was given for the operation. Deposit values should be greater than zero')

        if withdrawn_value <= self.current_balance:
            self.current_balance -= Decimal(withdrawn_value)
            return True

        else:
            raise ValueError('Withdraw ammount greater than account balance.')

    def show_balance(self):
        return {'account': self.id, 'balance': self.current_balance}

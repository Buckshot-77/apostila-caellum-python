from decimal import Decimal


class BankAccount():
    def __init__(self, id: str, owner: str, current_balance: Decimal) -> None:
        self.id = id
        self.owner = owner
        self.current_balance = Decimal(current_balance)

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

        else:
            raise ValueError('Withdraw ammount greater than account balance.')


account1 = BankAccount('123-4', 'Hugo', 1000)


account1.deposit(300)

print(account1.current_balance)

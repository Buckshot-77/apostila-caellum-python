from decimal import Decimal, getcontext

getcontext().prec = 2


class BankAccount():
    def __init__(self, id: str, owner: str, current_balance: Decimal) -> None:
        self.id = id
        self.owner = owner
        self.current_balance = current_balance


account1 = BankAccount('123-4', 'Hugo', (Decimal(0.1) + Decimal(0.2)))

print(account1.current_balance)

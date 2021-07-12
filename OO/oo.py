from decimal import Decimal


class BankAccount():
    def __init__(self, id: str, owner: str, current_balance: Decimal) -> None:
        self.id = id
        self.owner = owner
        self.current_balance = Decimal(current_balance)

    def balance_operation(self, added_value):
        self.current_balance += Decimal(added_value)


account1 = BankAccount('123-4', 'Hugo', 1000)


account1.balance_operation(-300)

print(account1.current_balance)

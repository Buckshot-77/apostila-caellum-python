from classes import Client, BankAccount

client1 = Client('Hugo', 'Rua A', '00000000000', '01/01/1900')

account1 = BankAccount('3205-8', client1, 1000)

account1.withdraw(300)
account1.deposit(1500)

account2 = BankAccount('32156', client1, 2000)

print(BankAccount.get_total_accounts())

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    def deposit(self , amount):
        amount = input("how much money do you want to deposit: ")
        return f"{int(amount)}$ has added to your bank account"
    def withdraw(self , amount):
        amount = input("how much money do you want to withdraw: ")
        if int(amount) < self.balance:
            return f"{amount}$ has withdrawed from your bank account"
        else:
            return "you dont have that much money on your balance"
bank_account1 = BankAccount(400)
print(bank_account1.deposit(400))
print(bank_account1.withdraw(400))
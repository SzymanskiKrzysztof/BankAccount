class Account:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f'Account owner: {self.owner} \nAccount balance: {self.balance}'

    def deposit(self, amount):
        self.balance += amount
        print('Deposit Accepted')

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print('Withdraw Accepted')
        else:
            print('Fund unavailable!')


acc1 = Account('Krzysztof', 120)
print(acc1)

acc1.deposit(80)
acc1.deposit(30)
acc1.withdraw(100)
print(acc1.balance)
acc1.withdraw(300)
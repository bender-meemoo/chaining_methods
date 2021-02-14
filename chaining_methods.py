class User:
    def __init__(self, name, email ):
        self.name = name
        self.email = email
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def make_withdrawl(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print(self.account_balance)
        return self

Cloud = User("Cloud", "Cloud@shinra.com")
Tifa = User("Tifa", "T_fists@shinra.com")
Barret = User("Barret", "shinrasux@shinra.com")



Cloud.make_deposit(100).make_deposit(500).make_deposit(20).make_withdrawl(300).display_user_balance()
Tifa.make_deposit(1000).make_deposit(40).make_withdrawl(40).make_withdrawl(30).display_user_balance()
Barret.make_deposit(1).make_deposit(15).make_withdrawl(2).make_withdrawl(5).make_withdrawl(.5).display_user_balance()



# print(Cloud.display_user_balance())
# print(Tifa.display_user_balance())
# print(Barret.display_user_balance())
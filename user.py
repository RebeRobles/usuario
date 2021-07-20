class User:
    def __init__(self, username, email_address):
        self.name = username			
        self.email = email_address		
        self.account_balance = 0

# agrega el método depósito 
    def make_deposit(self, amount):	
    	self.account_balance += amount

# agrega el método de retiro de fondos 
    def make_withdrawal(self, amount):
        if amount > self.account_balance:
            print('No existe saldo suficiente para su retiro')
        else:
    	    self.account_balance -= amount

#agrega el método que muestra el saldo
    def display_user_balance(self):
        return f'Usuario: {self.name}, Saldo: $  {self.account_balance}' 

    def transfer_money (self, other_user, amount):
        if amount > self.account_balance:
            print('No existe saldo suficiente para su retiro')
        else:
    	    self.account_balance -= amount
        other_user.account_balance += amount 
        return self      


user1 = User('Bruce Dickinson', 'bruce@ironmaiden.com')
user1.make_deposit(2000)
#print('*'*20)
#print(user1.name)
#print(user1.account_balance)
#print('*'*20)
user1.make_deposit(200)
user1.make_deposit(500)
user1.make_withdrawal(5000)
print(user1.display_user_balance())

user2 = User('Colin Firth', 'cfirth@kingsman.com')
user2.make_deposit(100)
user2.make_deposit(1000)
user2.make_withdrawal(900)
user2.make_withdrawal(100)
print(user2.display_user_balance())

user3 = User('Chris Martin', 'cmartin@coldplay.uk')
user3.make_deposit(10000)
user3.make_withdrawal(1500)
user3.make_withdrawal(500)
user3.make_withdrawal(300)
print(user3.display_user_balance())

user1.transfer_money(user2, 199)
print(user2.display_user_balance())
print(user1.display_user_balance())
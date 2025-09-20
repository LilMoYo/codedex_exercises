class BankAccount:
    def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
    
        self.first_name = first_name
        self.last_name = last_name
        self.account_id = account_id
        self.account_type = account_type
        self.pin = pin
        self.balance = balance
        
    def deposit(self, amount):
        self.balance = self.balance + amount
    
    def withdraw(self, amount):
        self.balance = self.balance - amount
        
    def display_balance(self):
        print(self.balance)
        
moyo = BankAccount("Mo", "Yo", 815, "Private", "1234", 6900.00)
print(vars(moyo))

moyo.deposit(96.00)
moyo.withdraw(25)
moyo.display_balance()

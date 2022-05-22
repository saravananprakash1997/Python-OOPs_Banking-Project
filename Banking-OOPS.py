#Banking Project on OOPS 
#Parent Class : User
#Child Class  : Bank
#Stores Detials about the account class
#Stores Detils about the amount
#Allows for deposits, withdraw, view_balance


#Parent Class
class User:
    def __init__(self, name, age, gender, account_type ):
        self.name = name
        self.age  = age
        self.gender = gender
        self.account_type = account_type
    
    def show_details(self):
        print("Account Holder Details")
        print("Name :", self.name)
        print("Age :" , self.age)
        print("Gender : ", self.gender)
        print("Type of Account :", self.account_type)


#Child Class
class Bank(User):
    def __init__(self, name, age, gender, account_type):
        super().__init__(name, age, gender, account_type)

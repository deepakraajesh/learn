from wsgiref.simple_server import demo_app


class User():
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    def show_user_det(self):
        print("User Details:")
        print("Name:",self.name)
        print("Age:",self.age)
        print("Gender:",self.gender)

class Bank(User):
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
        self.balance=0

    def deposit(self):
        amountD = float(input("Enter the amount to deposit"))
        self.balance += amountD
        print("Deposit Successful")
    
    def withdraw(self):
        amountW = float(input("Enter the amount to Withdraw"))
        if (amountW<=self.balance):
            self.balance -= amountW
        else:
            print("Insufficient Balance")

    def display_bal(self):
        print("Your Account balance is:", self.balance)

deep = Bank('Deepak',24,'M')
user = Bank("Hari", 22, 'M')

deep.show_user_det()
user.show_user_det()

condition=True

while(condition):
    print("1. Depositing the Money\n2. Amount Withdrawl\n3. View Account Balance\n4. Exit")
    option = input("Please enter the option: ")

    if (option=='1'):
        deep.deposit()
        deep.display_bal()

    elif (option=='2'):
        deep.withdraw()
        deep.display_bal()

    elif (option=='3'):
        deep.display_bal()

    elif (option=='4'):
        condition=False
        break

    else:
        print("Enter Correct Option")
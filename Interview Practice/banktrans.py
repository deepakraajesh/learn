import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="test"
)

cursor = db.cursor()
class Transaction:
    def deposit(self):
        accno = input("Enter your Account number: ")
        amountD = float(input("Enter the Amount to be Deposited: "))
        try:
            currentbal = "SELECT balance from sample WHERE accnum = %s",accno
            newbal = currentbal + amountD
            deposit = "UPDATE sample SET balance = %f WHERE accnum = %s",newbal,accno
            cursor.execute(deposit)
            db.commit()
        except:
            print("Enter Correct account number")
            db.rollback()

    def withdraw(self):
        accno = input("Enter your Account number: ")
        amountW = float(input("Enter the Amount to withdraw: "))
        try:
            currentbal = "SELECT balance from sample WHERE accnum = %s",accno
            if (amountW<=currentbal):
                newbal = currentbal - amountW
                withdraw = "UPDATE sample SET balance = %f WHERE accnum = %s",newbal,accno
                cursor.execute(withdraw)
                db.commit()
            else:
                print("Insuffcient Balance")
                db.rollback()
        except:
            print("Enter Correct account number")

    def view_bal(self):
        accno = input("Enter your Account number: ")
        currentbal = "SELECT balance from sample WHERE accnum = %s",accno
        print("Available Balance: ",currentbal)
    
    def transaction(self):
        accnoS = input("Enter your Account number: ")
        accnoR = input("Enter Receiver's Account number: ")
        amountT = float(input("Enter the Amount to Transact: "))
        try:
            currentbalS = "SELECT balance from sample WHERE accnum = %s",accnoS
            currentbalR = "SELECT balance from sample WHERE accnum = %s",accnoR
            if (amountT<=currentbalS):
                newbalS = currentbalS - amountT
                newbalR = currentbalR + amountT
                transactS = "UPDATE sample SET balance = %f WHERE accnum = %s",newbalS,accnoS
                transactR = "UPDATE sample SET balance = %f WHERE accnum = %s",newbalR,accnoR
                cursor.execute(transactS)
                cursor.execute(transactR)
                db.commit()
            else:
                print("Insuffcient Balance")
                db.rollback()
        except:
            print("Check Account number of Sender and Receiver")

condition=True
bank = Transaction()

while(condition):
    print("1. Depositing the Money in your Account\n2. Amount Withdrawl from your Account\n3. View Account Balance of your Account\n4. Send Money to others\n5. Exit")
    option = input("Please enter the option: ")

    if (option=='1'):
        bank.deposit()
        bank.view_bal()

    elif (option=='2'):
        bank.withdraw()
        bank.view_bal()

    elif (option=='3'):
        bank.view_bal()

    elif (option=='4'):
        bank.transaction()

    elif (option=='5'):
        condition=False
        break

    else:
        print("Enter Correct Option")

db.close()
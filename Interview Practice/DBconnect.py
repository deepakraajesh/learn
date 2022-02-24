from locale import currency
import mysql.connector

db = mysql.connector.connect(host="localhost",username="root",passwd="1234",database="test")

mycursor = db.cursor()

class Transaction:
    def deposit(self):
        #Getting User Details
        accnum = input("Enter your Account Number: ")
        select_stmt = "SELECT * FROM sample WHERE accnum = %(accnum)s"
        mycursor.execute(select_stmt, {'accnum':accnum})
        userDet = mycursor.fetchone()
        print("Welcome ",userDet[1])
        
        #Getting Amount to be Deposited
        amountD = float(input("Enter the Amount to be Deposited: "))

        #Add it to the exisiting balance
        cur_bal = userDet[2]
        new_bal = amountD + cur_bal

        update_stmt = "UPDATE sample SET balance=%(newbal)d WHERE accnum=%(accnum)s"
        mycursor.execute(update_stmt)

        #Print Current Balance
        print("New Balance is ",new_bal)

condition = True
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
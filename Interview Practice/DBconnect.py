from locale import currency
import sqlite3

db = sqlite3.connect("bank.sqlite")
mycursor = db.cursor()

class Transaction:
    def welcome(self,accnum):
        userDet = mycursor.execute("SELECT name,balance FROM accdet WHERE accnum = ?",(accnum,)).fetchone()
        print("Welcome ",userDet[0])
        
    def deposit(self,accnum):
        #Getting User Details
        userDet = mycursor.execute("SELECT name,balance FROM accdet WHERE accnum = ?",(accnum,)).fetchone()
        
        #Getting Amount to be Deposited
        amountD = float(input("Enter the Amount to be Deposited: "))

        #Add it to the exisiting balance
        new_bal = amountD + userDet[1]
        mycursor.execute("UPDATE accdet SET balance=? WHERE accnum=?",(new_bal,accnum))
        db.commit()

    def withdraw(self,accnum):
        amountw = float(input("Enter Amount to withdraw: "))
        userDet = mycursor.execute("SELECT name,balance FROM accdet WHERE accnum = ?",(accnum,)).fetchone()
        # check if withdraw amount is greater than current balance
        if (amountw > userDet[1]):
            print("Insufficient Balance")
        else:
            new_bal = userDet[1]-amountw
            mycursor.execute("UPDATE accdet SET balance=? WHERE accnum=?",(new_bal,accnum))
            db.commit()

    def view_bal(self,accnum):
        userDet = mycursor.execute("SELECT name,balance FROM accdet WHERE accnum = ?",(accnum,)).fetchone()
        print("Hello "+userDet[0]+"!!.. Your account balance is "+str(userDet[1]))

    def transaction(self,accnum):
        #Get Recipient Account number
        recipent = input("Enter Account number of the Recipient Bank")
        userDet = mycursor.execute("SELECT name,balance FROM accdet WHERE accnum = ?",(accnum,)).fetchone()
        #Check if Recipient account number is found
        try:
            recpDet = mycursor.execute("SELECT accnum,name,balance FROM accdet WHERE accnum = ?",(recipent,)).fetchone()
        except:
            print("Please Enter Valid Recipient Account Number")
        transfer = int(input("Enter the Amount to transfer: "))
        if (transfer > recpDet[2]):
            print("Insuffcient Funds")
        else:
            new_bal = userDet[1] - transfer
            recipientbal = recpDet[2] + transfer
            mycursor.execute("UPDATE accdet SET balance=? WHERE accnum=?",(new_bal,accnum))
            mycursor.execute("UPDATE accdet SET balance=? WHERE accnum=?",(recipientbal,recipent))
            db.commit()

condition = True
accnum = input("Enter your Account Number: ")
bank = Transaction()
while(condition):
    print("1. Depositing the Money in your Account\n2. Amount Withdrawl from your Account\n3. View Account Balance of your Account\n4. Send Money to others\n5. Exit")
    option = input("Please enter the option: ")
    bank.welcome(accnum)

    if (option=='1'):
        bank.deposit(accnum)
        bank.view_bal(accnum)

    elif (option=='2'):
        bank.withdraw(accnum)
        bank.view_bal(accnum)

    elif (option=='3'):
        bank.view_bal(accnum)

    elif (option=='4'):
        bank.transaction(accnum)
        bank.view_bal(accnum)

    elif (option=='5'):
        condition=False
        break

    else:
        print("Enter Correct Option")
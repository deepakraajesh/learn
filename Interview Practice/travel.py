import sqlite3
from datetime import datetime

db = sqlite3.connect("travel.sqlite")
print("DB Connected")
dbcursor = db.cursor()

# Getting inputs from the user
source = input("From which city you want to travel: ")
destination = input("To which city: ")
year, month, day = map(int,input("Type travel date in this format yyyy-mm-dd: ").split('-'))
dateon = datetime(year,month,day)

#Destination for the user, but "sources" is the table column name.
getcovidinfo = dbcursor.execute("SELECT until, restricted FROM travel WHERE city = ?",(destination,))
for row in getcovidinfo:
    tyear, tmonth, tday = map(int,row[0].split('-'))
    until = datetime(tyear,tmonth,tday)

    #If the travel date is greater than the date present in the DB, indicates, the latest update is not present
    if (dateon > until):
        print("Covid Restrictions update is not present yet")
    #If the date provided by the user is less than today, then the date is invalid
    elif (dateon < datetime.now()):
        print("Please enter a valid Date")
    #If the above conditions are failed to execute the given input is correct
    else:
        #If the column restricted is FALSE, Covid restrictions are not there
        if (row[1]=="FALSE"):
            print("It is not restricted since "+row[0])
        #vice-versa of above
        else:
            print("Covid restrictions are there until "+row[0])
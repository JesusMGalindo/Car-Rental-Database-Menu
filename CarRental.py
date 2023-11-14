import pymysql
from pymysql import Error
import datetime
import re
import copy

def validPhone(number):
    phone_match = re.compile("^(\w{3}-\w{3}-\w{4})$")
    match = phone_match.match(number)
    if match:
        return True
    return False

def printMenu():                 # Function to print menu
    print("\nMain Menu")
    for key in menuOptions.keys(): # loop through keys and print out values
        print (key, '--', menuOptions[key])

menuOptions = {                  # Menu using dictionary
    1: 'Customer List',
    2: 'Car List',
    3: 'Rental List',
    4: 'Exit',
}
    
if __name__=='__main__':         # Main driver
    print("Connecting to database...")
    DBNAME = input("Enter database name: ")
    try:            # establish database connection
        connection = pymysql.connect(
            host = "localhost",
            user = "root",
            passwd = "",
            database = DBNAME
        )
        print("MySQL database connection successfull")
    except Error as err:        # Exit if could not connect
        print(f"Error: '{err}'\nExiting...")
        exit()
    cursor = connection.cursor()    # create cursor to enable database manipulation
    while(True):
        printMenu()
        option = ''
        try:
            option = int(input('Select option: '))
        except:
            print('Wrong input. Please enter a number.')
        if option == 1:        # option 1 for customer table
            while(True):
                q1 = "SELECT * FROM CUSTOMER"      # query for display cusomer table
                cursor.execute(q1)          # execut query
                result = cursor.fetchall()  # fetch all records
                print("\n(IDNo, PHONE, NAME)")
                for tuple in result:
                    print(tuple)
                print("1 -- Add customer\n2 -- Back")
                op1 = ''
                try:
                    op1 = int(input('Select option: '))
                except:
                    print('Wrong input. Please enter a number.')
                if op1 == 1:
                    print("Enter customer credentials.")
                    name = input("Customer name: ")
                    phone = input("Customer phone number in the format XXX-XXX-XXXX: ")
                    if not validPhone(phone):
                        print("Invalid phone number.")
                        continue
                    query = "INSERT INTO CUSTOMER(NAME, PHONE) VALUES ('{0}', '{1}')".format(name, phone)   # query to insert tuple to table
                    try:
                        cursor.execute(query)   # execute query
                        connection.commit()     # commit/confirm change
                        print("Insert was successful")
                    except Error as err:        # check if query didn't error
                        print(f"Error: '{err}'")
                        continue
                elif op1 == 2:
                    break
                else:
                    print("Enter a valid input.")
        elif option == 2:
            while(True):
                q1 = "SELECT * FROM CARS"   # query to get cars table
                cursor.execute(q1)      # execute query
                result = cursor.fetchall()  # get all entries
                print("\n(DAILYRATE, WEEKLYRATE, VEHICLEID, MODEL, TYPE, MADE)")
                for tuple in result:
                    print(tuple)
                print("1 -- Add cars\n2 -- Back")
                op2 = ''
                try:
                    op2 = int(input('Select option: '))
                except:
                    print('Wrong input. Please enter a number.')
                if op2 == 1:
                    print("Enter car credentials.")
                    model = input("Car model: ")
                    made = ''
                    try:
                        made = int(input("Year car was made: "))
                    except:
                        print('Wrong input. Please enter a number.')
                        continue
                    cartype = input("Type of car: ")
                    dailyrate = ''
                    try:
                        dailyrate = int(input("Daily rate: "))
                    except:
                        print('Wrong input. Please enter a number.')
                        continue
                    weeklyrate = ''
                    try:
                        weeklyrate = int(input("Weekly rate: "))
                    except:
                        print('Wrong input. Please enter a number.')
                        continue
                    query = "INSERT INTO CARS(MODEL, MADE, TYPE, DAILYRATE, WEEKLYRATE) VALUES ('{0}', {1}, '{2}', {3}, {4}) ".format(model, made, cartype, dailyrate, weeklyrate)
                    try:
                        cursor.execute(query)   # execute query
                        connection.commit()     # commit/confirm change
                        print("Insert was successful")
                    except Error as err:        # check if error
                        print(f"Error: '{err}'")
                        continue
                elif op2 == 2:
                    break
                else:
                    print("Enter a valid input.")
        elif option == 3:
            while(True):
                q1 = "SELECT * FROM RENTAL" # query to get rental table
                cursor.execute(q1)          # execute query
                result = cursor.fetchall()  # fetch all entries
                print("\n(RENTID, RENTALTYPE, AMOUNTDUE, CUSTOMERID, VEHICLEID)")
                for tuple in result:
                    print(tuple)
                print("1 -- Add rental\n2 -- Back")
                op3 = ''
                try:
                    op3 = int(input('Select option: '))
                except:
                    print('Wrong input. Please enter a number.')
                if op3 == 1:
                    q1 = "SELECT * FROM CUSTOMER"   # display customer table
                    cursor.execute(q1)
                    result = cursor.fetchall()
                    print("\n(IDNo, PHONE, NAME)")
                    for tuple in result:
                        print(tuple)
                    try:
                        CID = int(input("Enter the customer ID of the customer making the purchase: "))
                    except:
                        print('Wrong input. Please enter a number.')
                        continue
                    q1 = "SELECT * FROM CUSTOMER WHERE IDNo={0}".format(CID)    # query to check if ID in customer table
                    cursor.execute(q1)  # execute query
                    result = cursor.fetchone()  # fetch the one entry since its a primary key
                    if result == None:  # check if it exists
                        print("ID not in table.")
                        continue
                    startDate = input('Enter the start date. (YYYY-MM-DD): ')
                    try:
                        Start_date = datetime.datetime.strptime(startDate, "%Y-%m-%d")
                    except ValueError:
                        print("Sorry, that is in the incorrect format.")
                        continue
                    print("Select rental type.\n1 -- Daily\n2 -- Weekly")
                    rentType = ''
                    try:
                        rentType = int(input('Select option: '))
                    except:
                        print('Wrong input. Please enter a number.')
                        continue
                    if rentType == 1:
                        rentType = 'D'
                    elif rentType == 2:
                        rentType = 'W'
                    else:
                        print('Invalid option. Please enter a number between 1 and 4.')
                        continue
                    numOfDW = ''
                    try:
                        numOfDW = int(input('Enter amount of days or weeks car is being rented: '))
                    except:
                        print('Wrong input. Please enter a number.')
                        continue
                    returnDate = ''
                    if rentType == 'D':
                        try:
                            returnDate = Start_date + datetime.timedelta(days=numOfDW)
                        except OverflowError as err:
                            print(f"Error: '{err}'")
                            continue
                        returnDate = returnDate.strftime('%Y-%m-%d')
                    elif rentType == 'W':
                        try:
                            returnDate = Start_date + datetime.timedelta(weeks=numOfDW)
                        except OverflowError as err:
                            print(f"Error: '{err}'")
                        returnDate = returnDate.strftime('%Y-%m-%d')
                    print(f"Start Date: {startDate}")
                    print(f"Return Date: {returnDate}")
                    q1 = """SELECT VEHICLEID, MODEL, TYPE, MADE, DAILYRATE, WEEKLYRATE 
                    FROM CARS WHERE VEHICLEID NOT IN 
                    (SELECT CARS.VEHICLEID FROM CARS JOIN RENTAL ON CARS.VEHICLEID = RENTAL.VEHICLEID 
                    JOIN DAILYRENTAL ON RENTAL.RENTALID = DAILYRENTAL.RENTALID 
                    WHERE '{0}' < DAILYRENTAL.RETURNDATE AND '{1}' > DAILYRENTAL.STARTDATE) 
                    AND VEHICLEID NOT IN 
                    (SELECT CARS.VEHICLEID FROM CARS JOIN RENTAL ON CARS.VEHICLEID = RENTAL.VEHICLEID 
                    JOIN WEEKLYRENTAL ON RENTAL.RENTALID = WEEKLYRENTAL.RENTALID 
                    WHERE '{0}' < WEEKLYRENTAL.RETURNDATE AND '{1}' > WEEKLYRENTAL.STARTDATE);""".format(startDate, returnDate) # query to search for vehcle id in cars table
                    cursor.execute(q1)
                    result = cursor.fetchall()
                    print("\nAVAILABLE CARS\n(VEHICHLEID, MODEL, TYPE, MADE, DAILYRATE, WEEKLYRATE)")
                    for tuple in result:
                        print(tuple)
                    try:
                        VID = int(input("Enter the vehicle ID of the car being rented: "))
                    except:
                        print('Wrong input. Please enter a number.')
                        continue
                    q1 = "SELECT * FROM CARS WHERE VEHICLEID={0}".format(VID) # query to search for vehcle id in cars table
                    cursor.execute(q1)  # execute query
                    result = cursor.fetchone()  # fetch single entry since its a primary key
                    if result == None:  # check if it exists
                        print("Car not in records.")
                        continue
                    q1 = """SELECT VEHICLEID, MODEL, TYPE, MADE, DAILYRATE, WEEKLYRATE 
                    FROM CARS WHERE VEHICLEID NOT IN 
                    (SELECT CARS.VEHICLEID FROM CARS JOIN RENTAL ON CARS.VEHICLEID = RENTAL.VEHICLEID 
                    JOIN DAILYRENTAL ON RENTAL.RENTALID = DAILYRENTAL.RENTALID 
                    WHERE '{0}' < DAILYRENTAL.RETURNDATE AND '{1}' > DAILYRENTAL.STARTDATE) 
                    AND VEHICLEID NOT IN 
                    (SELECT CARS.VEHICLEID FROM CARS JOIN RENTAL ON CARS.VEHICLEID = RENTAL.VEHICLEID 
                    JOIN WEEKLYRENTAL ON RENTAL.RENTALID = WEEKLYRENTAL.RENTALID 
                    WHERE '{0}' < WEEKLYRENTAL.RETURNDATE AND '{1}' > WEEKLYRENTAL.STARTDATE) 
                    AND VEHICLEID = {2};""".format(startDate, returnDate, VID) # query to search for vehcle id in cars table
                    cursor.execute(q1)  # execute query
                    result = cursor.fetchone()  # fetch single entry since its a primary key
                    if result == None:  # check if it exists
                        print("Car is unavailable.")
                        continue
                    rate = ''
                    if rentType == "W":
                        q1 = "SELECT WEEKLYRATE FROM CARS WHERE VEHICLEID={0}".format(VID) # query to check if car is available
                        cursor.execute(q1)  # execute query
                        result = cursor.fetchone()  # fetch single entry since its a primary key
                        rate = int(copy.deepcopy(result[0])) * numOfDW
                    elif rentType == "D":
                        q1 = "SELECT DAILYRATE FROM CARS WHERE VEHICLEID={0}".format(VID) # query to check if car is available
                        cursor.execute(q1)  # execute query
                        result = cursor.fetchone()  # fetch single entry since its a primary key
                        rate = int(copy.deepcopy(result[0])) * numOfDW
                    q1 = "INSERT INTO RENTAL(AMOUNTDUE, RENTALTYPE, CUSTOMERID, VEHICLEID) VALUES ({0}, '{1}', {2}, {3}) ".format(rate, rentType, CID, VID)
                    try:
                        cursor.execute(q1)   # execute query
                        connection.commit()     # commit/confirm change
                        print("Insert was successful")
                    except Error as err:        # check if error
                        print(f"Error: '{err}'")
                        continue
                    if rentType == 'W':
                        q1 = "SELECT RENTALID FROM RENTAL WHERE RENTALTYPE = '{0}' AND AMOUNTDUE = {1} AND CUSTOMERID = {2} AND VEHICLEID = {3};".format(rentType, rate, CID, VID)
                        cursor.execute(q1)  # execute query
                        result = cursor.fetchone()  # fetch single entry since its a primary key
                        rentID = int(copy.deepcopy(result[0]))
                        q1 = "INSERT INTO WEEKLYRENTAL(RENTALID, NUMOFWEEKS, STARTDATE, RETURNDATE) VALUES ({0}, {1}, '{2}', '{3}')".format(rentID, numOfDW, startDate, returnDate)
                        try:
                            cursor.execute(q1)   # execute query
                            connection.commit()     # commit/confirm change
                            print("Insert was successful")
                        except Error as err:        # check if error
                            print(f"Error: '{err}'")
                            continue
                    elif rentType == 'D':
                        q1 = "SELECT RENTALID FROM RENTAL WHERE RENTALTYPE = '{0}' AND AMOUNTDUE = {1} AND CUSTOMERID = {2} AND VEHICLEID = {3};".format(rentType, rate, CID, VID)
                        cursor.execute(q1)  # execute query
                        result = cursor.fetchone()  # fetch single entry since its a primary key
                        rentID = int(copy.deepcopy(result[0]))
                        q1 = "INSERT INTO DAILYRENTAL(RENTALID, NUMOFDAYS, STARTDATE, RETURNDATE) VALUES ({0}, {1}, '{2}', '{3}')".format(rentID, numOfDW, startDate, returnDate)
                        try:
                            cursor.execute(q1)   # execute query
                            connection.commit()     # commit/confirm change
                            print("Insert was successful")
                        except Error as err:        # check if error
                            print(f"Error: '{err}'")
                            continue
                elif op3 == 2:
                    break
        elif option == 4:
            print('Exiting...')
            cursor.close()  # close connections
            connection.close()
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 4.')
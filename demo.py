import sqlite3
from sqlite3 import Error
from dbmethods import create_drivers_passengers_table


def passengers():
    ''' Function to return dict '''
    passenger_list = [{
"name": "Passenger1", "zipcode": "Zipcode1"},
{"name": "Passenger2", "zipcode": "Zipcode2"},
{"name": "Passenger3", "zipcode": "Zipcode3"},] 
    return passenger_list
#return statement
def drivers():
    "return driver_list"
    #return driver_list
#documentation string
def save_drivers_to_database():
    driver_list = [{ 
"name": "Driver1", "zipcode": "zipcode1"},
{"name": "Driver2", "zipcode": "zipcode2"},
{"name": "Driver3", "zipcode": "zipcode3"},]
def match(
    passenger
#make passenger as an argument to match
):
    driver_list = drivers()
    passenger_zipcode = passenger["zipcode"]
    for driver in driver_list:
        driverzipcode = driver["zipcode"]
        if driverzipcode == passenger_zipcode:
        #== bc test for equality
            drivername = driver["name"]
            passengername = passenger["name"]
            return f"{drivername} = {passengername}"
            #rememeber to format with f
def main ():
    passenger_list = passengers()
    #inside main method getting a list of passengers
    passenger = passenger_list[1]
    #takes first passenger out of the list and calls it passenger
    message = match(passenger)
    print (message)


if __name__ == '__main__':
    create_drivers_passengers_table()
    main()
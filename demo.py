def passengers():
    ''' Function to return dict '''
    passenger_list = [{
"Name": "Passenger1", "Zipcodes": "Zipcode1"},
{"Name": "Passenger2", "Zipcodes": "Zipcode2"},
{"Name": "Passenger3", "Zipcodes": "Zipcode3"},] 
    return passenger_list
#return statement
def drivers():
    "return driver_list"
#documentation string
    driver_list = [{ 
"Name": "Driver1", "Zipcodes": "Zipcode1"},
{"Name": "Driver2", "Zipcodes": "Zipcode2"},
{"Name": "Driver3", "Zipcodes": "Zipcode3"},]
    return driver_list
def match(
    passenger
#make passenger as an argument to match
):
    driver_list = drivers()
    passenger_zipcode = passenger["Zipcodes"]
    for driver in driver_list:
        driverzipcode = driver["Zipcodes"]
        if driverzipcode == passenger_zipcode:
        #== bc test for equality
            drivername = driver["Name"]
            passengername = passenger["Name"]
            return f"{drivername} = {passengername}"
            #rememeber to format with f
def main ():
    passenger_list = passengers()
    #inside main method getting a list of passengers
    passenger = passenger_list[1]
    #takes first passenger out of the list and calls it passenger
    message = match(passenger)
    print (message)
main()

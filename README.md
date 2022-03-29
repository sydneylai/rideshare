# Start Draft 1
    
Research 
    
Reality:
Create a decentralized database
Matching drivers and passengers based on their matching zipcodes in their metro area
    
MVP: Showcase publishing and subscribing within the terminal 
Creating the json files for the passengers and drivers

Publish Subscribe
Idea: 
    Set of aggregators in the middle between the publishers and the subscribers. For exampble Google News: the news gets published but Google News aggregates the news. Instead of Google News, now IPFS is in the middle and the topic is drivers and passengers. The idea is the passenger broadcasts their location and the driver subscribes to their topic. The driver will publish and the passenger will subscribe. 
    
Level 1: passenger publish, and all drivers in that area will subscribe
Level 2: Driver will publish to that specifically and the passenger will subscribe or tell the Driver that they accept that fair. The acceptance will then be published to the driver's topic. 
    
Resources: 
    https://blog.ipfs.io/25-pubsub/
    https://docs.ipfs.io/reference/cli/#ipfs-pubsub

Design 
    
1. List of drivers
    - Driver Object should be a JSON object, python dictionary of values 
        - Name of driver, the value (zipcode) of the driver
3. List of passengers
    - Passenger Object should be a JSON object, python dictionary of values 
        - Name of driver, the value (zipcode) of the driver
5. Function: randomly assigns Driver and Passenger if they are in the same zipcode 
6. Result: Driver 1 is matched with Passenger 1

Backend "database"
1. (Decentralized) P2P database IPFS/distributed file systems
2. (Centralized) Created a small SQL database example to show comparison 
3. The centralized database was in the demo.py file 

The Idea: Is to wrap the shell commands with python code so can write python code in the command line - however this would require writing API REQUESTS

What we ended executing on: We demonstrated the demo by using curl commands in the terminal 
    
Curl is for bash
Request is for python (for API calls)
    

## Centralized Example
    
1. Python file
2. Centralized database with SQL

```python=
import sqlite3
import logging
from sqlite3 import Error

#first create connection function
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

#second create table function
def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
def create_driver(conn, driver):
    """
    Create a new driver
    :param conn:
    :param driver:
    :return:
    """

    sql = ''' INSERT INTO drivers(name,zipcodes)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, driver)
    conn.commit()
# this inserts the driver into the database

    return cur.lastrowid
#third create a main function to create the passenger, in this example you would create a API request to publish the passenger (Decetralized matching, you create the copy and the idea is that it becomes decentralied)

def create_passenger(conn, passenger):
    """
    Create a new passenger
    :param conn:
    :param passenger:
    :return:
    """

    sql = ''' INSERT INTO passengers(name,zipcodes)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, passenger)
    conn.commit()
# this return function is a webrequest return, you would return the value of the webrequest - success!

    return cur.lastrowid
#fourth create a main function to create the drivers and passenger tables

def create_drivers_passengers():
    database = r"pythonsqlite.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        # create a new driver
        driver1 = ('John', '92802');
        driver1ID = create_driver(conn, driver1)

        # passenger
        passenger_1 = ('Sydney','92704')
        passenger_2 = ('Rob','92802')

        # create passenger
        create_passenger(conn, passenger_1)
        create_passenger(conn, passenger_2)


def create_drivers_passengers_table():
    database = r"pythonsqlite.db"

    sql_create_drivers_table = """ -- drivers table
                                CREATE TABLE IF NOT EXISTS drivers (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    zipcodes text NOT NULL
                                    );"""

    sql_create_passengers_table = """-- passengers table
                                CREATE TABLE IF NOT EXISTS passengers (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    zipcodes text NOT NULL
                                );"""
    # create a database connection
    conn = create_connection(database)

    # create tables to create the connection
    if conn is not None:
        # create drivers table
        create_table(conn, sql_create_drivers_table)

        # create passengers table
        create_table(conn, sql_create_passengers_table)
    else:
        print("Error! cannot create the database connection.")

#Fifth, reconnect database and extract from that database

# This would have been an API Request to my 127001 - would subscribe and get back all the passengers
def select_all_passengers(conn):
    """
    Query all rows in the passengers table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM passengers")

    rows = cur.fetchall()
#fetch all the rows but this does not return anything
    passenger_list=[]
    for row in rows:
        print(row)
        passenger={"name":row[1],"zipcode":row[2]}
        #reconnect db and extract from that db
        passenger_list.append(passenger)
    return passenger_list    


#run this function, and call this function
def select_all_drivers(conn):
    """
    Query all rows in the drivers table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM drivers")

    rows = cur.fetchall()
    driver_list=[]
    for row in rows:
        driver={"name":row[1],"zipcode":row[2]}
        #reconnect db and extract from that db
        driver_list.append(driver)
        print(row)
    return driver_list

def drivers():
    database = r"pythonsqlite.db"
    conn = create_connection(database)
    return select_all_drivers(conn)
def passengers():
    database = r"pythonsqlite.db"
    conn = create_connection(database)
    return select_all_passengers(conn)
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
def main():
    create_drivers_passengers_table()
    #create_drivers_passengers() - this is redundant, does not need to be run more than once
    database = r"pythonsqlite.db"
    conn = create_connection(database)
    #select_all_passengers(conn) - these are stepping stones to get database to work
    #select_all_drivers(conn) - these are stepping stones to get database to work

    passenger_list = passengers()
    #conn is the connection to the database
    logging.warning(passenger_list)
    passenger = passenger_list[1]
    #takes first passenger out of the list and calls it passenger
    message = match(passenger)
    print (message)
main()




```
### Create Table 
1. create connection function
2. create table function
3. create main function to create drivers and passengers

Edit the template to equal to passengers

Table names must map, and turn those into DB
```
Driver Name
Driver Zipcodes
Passenger Name
Pasenger Zipcodes
```
    
Lesson: database is hardcoded within python file
    
## Decentralized Example
    
1. Create a json file for each driver and each passenger
2. Matching the driver and passengers with the IPFS pubsub method via curl commands in the terminal to showcase peer to peer to matching
    
driver1.json
    
```json=
    {
    "name":"Todd", "zipcode":"33101"
} 
```
    
driver2.json

```json=
{
    "name":"Bob", "zipcode":"33129"
}
```
    
passenger1.json

```json=
    {
    "name":"John", "zipcode":"33101"
}
```
    
passenger2.json
```json=
    {
    "name":"Sally", "zipcode":"33129"
}
```

These json files require less code than a traditional python file with a centralized database.
    
1. Create a Topic - via JSON file
    Every passenger would have their own JSON (JSON formmated payloads) file, so if this app had 20M passengers there would be 20M JSON files. So here you can see another perspective of having a decentralized database because you would need 20M individual JSON files rather than having 20M rows in a single database. 
    
2. Create a Passenger File
3. Create a Driver File
4. Publish passenger file to passenger topic 
5. Publish driver file to driver topic 
6. Subscribe to passenger topic to get location
    
At this point I've created JSON files for Passengers and Drivers.
    
## Create a database as an end point
    
Install the IPFS
    https://docs.ipfs.io/install/command-line/#official-distributions
Once IPFS is installed you can call the daemon from the Command Line.
    
To store Drivers and Passengers, each profile would be json files in IPFS.
    - List of Drivers with zip codes as a file
    - List of Passengers with zip codes as a file
    Every file would be published with a curl command to the local host 127001.
    Each driver/passenger would publish their own request, and pull each other's profiles. Each file would be their own driver/passenger profile.
    
Lesson: at this point, I have: 
    - Learned how to interact with IPFS
    - Installed IPFS in the terminal https://docs.ipfs.io/install/command-line/#official-distributions
    
## Start the daemon
Installing the IPFS is like building the post-office. Publishing a JSON file would be putting a letter in the mail. 

Start the daemon to run in the background, like opening the post-office: 
    
    ```sudo ipfs daemon```
    by starting the IPFS daemon
    
IPFS generates a hash in the system to provide a unique identifier. 
    
Driver1 Hash ```"Hash":"QmWFRKVtsJCdwPaD3SozvSwMdhxo3EJLpEv4LMoPcqopoX"```
    
Driver 2 Hash ```"Hash":"QmUr2jDAeWpVFX6s6fkCLGoQCn8SpDaQQMqZazJSiomZKj"```
    
At this stage, we are trying list all file objects loaded in IPFS, to do so we need to know our Hash. 
    
When running curl commands we directly interacted with IPFS. 
    
The webapp would send request to sever (or in this case, a decenetralized file system) and now all these hashes are stored in a JSON server. 
    
Lesson: At this point I am able to upload the JSON files for Drivers and Passengers with a curl command.
    
Next Steps:
    1. assign a Topic
    2. and then pub/sub

A topic can be constructed however you want, so if you had a topic for a particular zip code, then everyone subscribed to that zip code will see all messages published to it. For example:
    
```curl -X POST -F file=@myfile "http://127.0.0.1:5001/api/v0/pubsub/pub?arg=90011" ```
    
Would publish to the topic (in this case a zip code) "90011" if you wanted to sub, so you can retrieve all messages sent to that zip code with the following:
    
```curl -X POST "http://127.0.0.1:5001/api/v0/pubsub/sub?arg=90011"```
    

In the terminal, this command should retreieve all previous CIDs (content identifier) I've created:
    
```
    ipfs pin ls
```
        
QmejvEPop4D7YUadeGqYWmZxHhLc4JBUCzJJHWMzdcMe2y indirect
QmQ5vhrL7uv6tuoN9KeVBwd4PwfQkXdVVmDLUZuTNxqgvm indirect
QmYCvbfNbCwFR45HiNP45rwJgvatpiW38D961L5qAhUM5Y indirect
QmdvS8djomKst8dkkahdCsDkyWjkH3D5yeXu9s5PC74VuB recursive
QmPZ9gcCEpqKTo6aq61g2nXGUhM4iCL3ewB6LDXZCtioEB indirect
QmU5k7ter3RdjZXu3sHghsga1UQtrztnQxmTL22nPnsu3g indirect
QmUr2jDAeWpVFX6s6fkCLGoQCn8SpDaQQMqZazJSiomZKj recursive
QmWFRKVtsJCdwPaD3SozvSwMdhxo3EJLpEv4LMoPcqopoX recursive
QmZnzGhPM5mo8BSWcABeWXavkjpjFsu8yoMg5HQ7A998ty recursive
QmeGVdbzX2gn8wFyK5cQok4UctCfZrS1phPJe5ZEi5FhpW recursive
QmQGiYLVAdSHJQKYFRTJZMG4BXBHqKperaZtyKGmCRLmsF indirect
QmQPeNsJPyVWPFDVHb77w8G42Fvo15z4bG2X8D2GhfbSXc recursive
QmTReW6Cu4E7PARfJ9FUU5y3r215rVvqmQtripsSAwFBxc recursive
QmQy6xmJhrcC5QLboAcGFcAE1tC8CrwDVkrHdEYJkLscrQ indirect
QmUNLLsPACCz1vLxQVkXqqLX5R1X345qqfHbsf67hvA3Nn recursive
    
## Create a topic
    
https://blog.ipfs.io/25-pubsub/
https://docs.ipfs.io/reference/cli/#ipfs-pubsub-ls
    
1. sub to the topic 
    
```ipfs pubsub passengers```

2. publish to a topic    
```ipfs pubsub pub passengers passengers/passenger1.json```
    
    
Result: 
    
![](https://i.imgur.com/A7iMLVn.png)
    
What ends up happening: 
    1. passsenger publishes to a zipcode
    2. driver subs to a zipcode
    3. gets matched through pubsub
    
## Publish to a Driver topic
    
1. sub to the topic 
    
```ipfs pubsub drivers```

2. publish to a topic    
```ipfs pubsub pub drivers drivers/driver1.json```
    
Result:
    
![](https://i.imgur.com/cK0uaAn.png)
    
:lightning: What you see here is John is a passenger in zip code 33101 and Todd is a driver in zip code 33101 and are matched in IPFS. 

## Lesson Learned
    
- learned a new mental model on databases, so instead of the traditional one database with various files, I had to "host" each individual file in IPFS. Instead of having a database of passenger and drivers, I needed to create a single JSON file per driver and per passenger, and so instead of having a database of 20M drivers and passengers, I would need to create 20M individual JSON files
- learned pubsub, publishing to an IPFS Topic and subscribing to an IPFS Topic which allows passenger to publish their zip code to an IPFS Topic which is then matched with a driver that subscribes to an IPFS Topic
- how conceptually difficult it is to make a decentralized ridesharing app, but at the same time the core matching mechanism of pairing json files to json files requires less lines of code
- learn how to make a database and connecting to it

import sqlite3
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
# this inserts the driver into the DB

    return cur.lastrowid
#third create a main function to create the drivers and passenger tables

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
# this inserts the passenger into the DB

    return cur.lastrowid
#third create a main function to create the drivers and passenger tables

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
    # edit template into drivers passengers
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

#reconnect db and extract from that db

#run this function, and call this function as HW
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
    #select_all_passengers(conn) - these are stepping stones to get db to work
    #select_all_drivers(conn) - these are stepping stones to get db to work

    passenger_list = passengers()
    #conn is the connection to the db
    passenger = passenger_list[1]
    #takes first passenger out of the list and calls it passenger
    message = match(passenger)
    print (message)
main()
    
#load a driver into the table
#define db file as a string
#create a connection from that db file 
#define driver
#load the driver into the db by using the driver object and connections object



import psycopg2
from time import sleep
from os import system

def create_table_loginusers():   # function for creating tables in PostgreSQL
    try:
        connection = psycopg2.connect(user = 'postgres',
                                      password = 'itspasswordhere',
                                      host = '127.0.0.1',
                                      port = "5432",
                                      database = "postgres")
        cursor = connection.cursor()
        tables_var = ("""
                      CREATE TABLE loginusers (
                      email_id TEXT PRIMARY KEY NOT NULL,
                      phone    TEXT NOT NULL,
                      passwrd  TEXT NOT NULL )""" )
        cursor.execute(tables_var)
        connection.commit()
        print("Table created successfully in PostgreSQL")
    except(Exception, psycopg2.DatabaseError) as error:
        print("Error while creating PostgreSQL table", error)
    finally:
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed..")


def exist_login():
    email = input("Email : ")
    print("\n")
    passw = input("Password : ")
    print("\n")
    con = psycopg2.connect(database = "postgres", user = "postgres",
                           password = "itspasswordhere", host = "localhost",
                           port = "5432")
    cur = con.cursor()
    








def newuser_creation():
    email = input("Email : ")
    print("\n")
    pho = input("Phone : ")
    print("\n")
    passw = input("Password : ")
    print("\n")
    passw2 = input("Confirm Password : ")
    print("\n")
    if passw != passw2:
        print("Please enter same passwords each time!\n")
        print("Re-enter your user-creation data....")
        sleep(0.7)
        newuser_creation()

    else:
        # create_table_loginusers()
        con = psycopg2.connect(database = "postgres", user = "postgres",
                               password = "itspasswordhere", host = "localhost",
                               port = "5432")
        print("Database opened successfully")
        cur = con.cursor()
        sleep(2)
        insert_query = "INSERT INTO loginusers (email_id, phone, passwrd) VALUES (%s, %s, %s);"
        record_to_insert = (email, pho, passw2)
        cur.execute(insert_query, record_to_insert)
        con.commit()
        print("New user created successfully")
        cur.close()
        con.close()

def mm_choice():
    print("\t\t\t\t\tWelcome to the SafePass Database!!\n")
    sleep(1)
    print("1. Login Existing User\n")
    print("2. Create New User")

    b = input()
    if int(b) == 1:
        print("existing user login")
        # function call for existing user login
    elif int(b) == 2:
        print("New user creation")
        newuser_creation()
        # create_table_loginusers()    # no need, table already created
    else:
        print("Please enter a valid choice")
        sleep(0.7)
        system('cls')
        mm_choice()
mm_choice()

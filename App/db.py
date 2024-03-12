import sqlite3
import re
from sqlite3 import Error
import json


def create_user(email, password, forename, surname, dob):
    try:
        sql = f'''INSERT INTO user VALUES ('{email}', '{password}', '{forename}','{surname}','{dob}');'''
        run_query(sql)

    except sqlite3.Error as e:
        print(e)


def create_outdoor_workout(ExerciseType, Distance, TimeTaken, DateCompleted):
    try:
        sql = f'''INSERT INTO outdoorworkouts VALUES ('{ExerciseType}', '{Distance}', '{TimeTaken}','{DateCompleted}');'''
        run_query(sql)

    except sqlite3.Error as e:
        print(e)

def update_user(email, oldPassword, newPassword):
    try:
        sql = f'''UPDATE user SET password='{newPassword}' WHERE email='{email}', AND password='{oldPassword}';'''
        run_query(sql)
    except sqlite3.Error as e:
        raise e


def get_user(conn, email, password, forename, surname, age):
    pass


def login(emailcheck, passwordcheck):
    sql1 = f'''SELECT * FROM user WHERE email = '{emailcheck}' AND password = '{passwordcheck}';'''
    bool(run_query(sql1))

def remove_user(emailcheck, passwordcheck):
    sql1 = f'''DELETE FROM user WHERE email = '{emailcheck}' AND password = '{passwordcheck}';'''
    run_query(sql1)


def run_query(query):
    try:
        conn = sqlite3.connect("identifier.sqlite")
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        return cursor.fetchall()

    except sqlite3.Error as e:
        raise e
        conn.rollback()
    finally:
        conn.close()

def clear_table(table):
    try:
        sql = f'''DELETE FROM 'user';'''
        run_query(sql)
    except sqlite3.Error as e:
        raise e

def get_all_users():
    #gets all users in a database
    find_user_query = "SELECT * FROM user"
    result = run_query(find_user_query)
    users=[]
    for record in result:
        users.append(users(record[1], record[0]))
    print("inline", users)
    return users


def check_password(password):
    min_length = 10
    require = {"up": False, "low": False, "digit": False, "symbol": False}
    for char in password:
        if char.isupper():
            require["up"] = True
        elif char.islower():
            require["low"] = True
        elif char.isdigit():
            require["digit"] = True
        elif not char.isalnum():
            require["symbol"] = True
    if len(password) < min_length:
        raise ValueError("password too short")


# makes regular expression for validating email
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'


# validates the email entry conforms with the right structure
def check_email(email):
    # the regular expression is passed and the email string is passed into the fullmatch() method
    if len.email > 30 or len.email < 5 or (re.fullmatch(regex, email)):
        print("Valid Email")

    else:
        raise ValueError("the email you have entered is not in the correct format")


def check_name(forename, surname):
    if len.forename > 30 or len.forename < 1 or len.surname > 30 or len.surname < 1:
        raise ValueError("the name you have entered is too long or too short")


def check_dob():











if __name__ == "__main__":
    db_file = "identifier.sqlite"




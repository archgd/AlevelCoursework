import datetime
import sqlite3
import re
from sqlite3 import Error
import json



def create_user(email, password, forename, surname, dob): #this function is called in init.py in the register app route and adds the users inputs from the html forms into the user SQL table
    try:
        sql = f'''INSERT INTO user VALUES ('{email}', '{password}', '{forename}','{surname}','{dob}');'''  #inserts the users information into the user SQL table
        run_query(sql)

    except sqlite3.Error as e:
        print(e)


def login(emailcheck, passwordcheck): #this function called in init.py and takes the parameters from the users input to a HTML form on the compares the inputs to the stored values in the user SQL table before granting the user access to the website
    sql = f'''SELECT * FROM user WHERE email = '{emailcheck}' AND password = '{passwordcheck}';'''
    bool(run_query(sql))


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


def clear_table(table):  #this function is used to clear the table during testing when test data is entered
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


def create_custom_workout(email, exercise, weight, reps, datedone):  #takes the users input and allows them to store custom exercises
    try:
        sql = f'''INSERT INTO gymworkouts VALUES ('{email}', '{exercise}', '{weight}','{reps}','{datedone}');'''  #users data is added to the gymworkouts SQL table
        run_query(sql)

    except sqlite3.Error as e:
        print(e)


def record_planned_workout(email, workout, datecompleted):  #takes the users input and allows them to store preplanned exercises
    try:
        sql = f'''INSERT INTO preplannedworkouts VALUES ('{email}', '{workout}', '{datecompleted}');'''  #adds the users input to the preplannedworkouts SQL table
        run_query(sql)

    except sqlite3.Error as e:
        print(e)


def create_outdoor_workout(email, exercisetype, distance, timetaken, date):  #takes the users input and allows them to store outdoor exercises
    try:
        sql = f'''INSERT INTO outdoorworkouts VALUES ('{email}', '{exercisetype}', '{distance}','{timetaken}','{date}');'''  #adds the users input to the outdoorworkouts SQL table
        run_query(sql)

    except sqlite3.Error as e:
        print(e)


def get_exercises(email, exercise):  #gets the users input to and retrieves the data from the gymworkouts SQL table
    try:
        sql = f'''SELECT Exercise, Weight, Reps, DateDone FROM gymworkouts WHERE email='{email}' AND Exercise='{exercise}'; '''

        res = run_query(sql)
        return res
    except sqlite3.Error as e:
        print(e)


def get_outdoor_exercises(email, exercise):  #gets the users input to and retrieves the data from the outdoor SQL table
    try:
        sql = f'''SELECT ExerciseType, Distance, TimeTaken, DateCompleted FROM outdoorworkouts WHERE email='{email}' AND ExerciseType='{exercise}'; '''

        res = run_query(sql)
        return res
    except sqlite3.Error as e:
        print(e)


def get_user(email, password):
    try:
        sql = f'''SELECT email, password FROM user WHERE email='{email}' AND password ='{password}'; '''

        res = run_query(sql)
        return res
    except sqlite3.Error as e:
        print(e)


if __name__ == "__main__":
    print(get_outdoor_exercises("archgd912@outlook.com", "Run"))



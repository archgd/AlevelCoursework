import sqlite3
import flask
from flask import Flask, render_template, request, session, redirect, url_for

from App import db  # imports all of the functions written in db.py

app = Flask(__name__)
app.secret_key = "ILOVEKEYS"


@app.route('/home')
def home():
    return render_template('HomePage.html')
#this app route renders the home page for the user and nothing else

@app.route('/workouts')
def workouts():
    return render_template("Workouts.html")
#this app route renders the workouts landing page for the user and nothing else


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == "GET":
        print("test2")
        return render_template("LoginPage.html")
    # default loads the login page when the app is run
    elif request.method == "POST":  # only runs if the user submits the login form
        email = request.form["email"] #the email form on the webpage is set as the local variable email
        print(email)
        password = request.form["password"] #the password form on the webpage is set as the local variable password
        print(password)
        user = [(email, password)]  # stores the email and password from the form as a local variable
        print(user)
        try:
            res = db.get_user(email, password)
            print(res)
            if  res == user:  # checks if the email matches the password stored in the database
                # session['username'] = request.form['email']  # sets the session username to the email address
                return redirect(url_for('home'))  # redirects the user to the home page of the website

            else:
                text = "Enter a valid email and password" #raises error message to the user letting them know that the combination entered is incorrect
                return render_template("incorrectPassword.html")

        except sqlite3.Error as e:
            print(e)
            return redirect(url_for('login'))

@app.route('/')
@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == "GET":
        return render_template('SignUp.html')  # renders the registration page template
    elif request.method == "POST":  # only runs if the user submits the login form
        print("first")  # error checking
        email = request.form["email"] # the email form on the webpage is set as the local variable email
        password = request.form["password"] # the password form on the webpage is set as the local variable password
        forename = request.form["forename"] # the forename form on the webpage is set as the local variable forename
        surname = request.form["surname"] # the surname form on the webpage is set as the local variable surname
        dob = request.form["dob"] # the dob form on the webpage is set as the local variable dob
        print("second") # error checking

        session['username'] = request.form["email"]  # sets the session username to the users email that they enter

        db.create_user(email.lower(), password, forename.lower(), surname.lower(), dob)  # runs the db.py function create_user which adds the users details to the users table and creates their account
        return redirect(url_for('login'))


@app.route('/GymWorkouts', methods=['POST', 'GET'])
def GymWorkouts():
    if request.method == "GET":
        return render_template('CustomWorkouts.html')
    elif request.method == "POST":
        Exercise = request.form["exercise"]  # the exercise form on the webpage is set as the local variable exercise
        email = request.form['email']  # the email form on the webpage is set as the local variable email
        Reps = request.form["reps"]  # the reps form on the webpage is set as the local variable reps
        Weight = request.form["weight"]  # the weight form on the webpage is set as the local variable weight
        DateDone = request.form["date completed"]  # the date completed form on the webpage is set as the local variable DateDone

        db.create_custom_workout(email, Exercise, Reps, Weight, DateDone)  # runs the db.py function create_custom_workout which adds the entered details to the gymworkouts table
        return redirect(url_for('GymWorkouts'))  # after the operation is carried out the custom workouts page is returned so users can add more exercises if they wish
    return render_template("CustomWorkouts.html")


#
#
@app.route('/OutdoorWorkouts', methods=['POST', 'GET'])
def OutdoorWorkouts():
    if request.method == "GET":
        return render_template('OutdoorWorkouts.html')
    elif request.method == "POST":
        exercisetype = request.form["exercisetype"]  # the exercisetype form on the webpage is set as the local variable exercisetype
        distance = request.form["distance"]  # the distance form on the webpage is set as the local variable distance
        timetaken = request.form["timetaken"]  # the timetaken form on the webpage is set as the local variable timetaken
        email = request.form["email"]  # the email form on the webpage is set as the local variable email
        date = request.form["date"]  # the date form on the webpage is set as the local variable date

        db.create_outdoor_workout(email, exercisetype, distance, timetaken, date)   # runs the db.py function create_outdoor_workout which adds the entered details to the outdoorworkouts table
        return redirect(url_for('workouts')) # after the operation is carried out the workouts landing page is returned so users can navigate the website to other parts of it easily
    return render_template("OutdoorWorkouts.html")
#

@app.route('/PrePlannedWorkouts', methods=['POST', 'GET'])
def PrePlannedWorkouts():
    if request.method == "GET":
        return render_template('PrePlannedWorkouts.html')
    elif request.method == "POST":
        email = request.form["email"]  # the email form on the webpage is set as the local variable email
        workout = request.form["type_of_exercise"]  # the type_of_exercise form on the webpage is set as the local variable workout
        datecompleted = request.form["datecompleted"]  # the datecompleted form on the webpage is set as the local variable datecompleted

        db.record_planned_workout(email, workout, datecompleted)  # runs the db.py record_planned_workout which adds the entered details to the preplannedworkouts table
        return redirect(url_for('workouts'))  # after the operation is carried out the workouts landing page is returned so users can navigate the website to other parts of it easily
    return render_template("PrePlannedWorkouts.html")


@app.route('/MyProgressQuerey', methods=['POST', 'GET'])
def myProgressQuerey():
    if request.method == "GET":
        print("hi")
        return render_template("MyProgressQuerey.html")
        print("test")
    elif request.method == "POST":
        print("test2")
        email = request.form["email"]  # requests the users email so that exercises they have entered to the database can be retrieved
        exercise = request.form["exercise"]  # requests the type of exercise that the user wants to recieve their data for
        print("false")
        res = db.get_exercises(email, exercise)  # the db.py function get_exercises is run which takes the users inputs as parameters and then returns the necessary data to be put into the table
        print("true")
        # print(res)
        return render_template("MyProgress.html",array=res)  # once the user has entered and submitted their data then the my gym progress page is returned which has the table format of the requested users data on it



@app.route('/MyOutdoorProgressQuery', methods=['POST', 'GET'])
def MyOutdoorProgressQuery():
    if request.method == "GET":
        print("hi")
        return render_template("MyOutdoorProgressQuery.html")
        print("test")
    elif request.method == "POST":
        email = request.form ["email"]  # requests the users email so that exercises they have entered to the database can be retrieved
        exercise = request.form["exercise"]  # requests the type of exercise that the user wants to recieve their data for
        res = db.get_outdoor_exercises(email, exercise)  # the db.py function get_outdoor_exercises is run which takes the users inputs as parameters and then returns the necessary data to be put into the table
        print (res)
        return render_template("MyOutdoorProgress.html", array=res)  # once the user has entered and submitted their data then the my outdoor progress page is returned which has the table format of the requested users data on it




if __name__ == '__main__':
    app.run()



import sqlite3
import flask
from flask import Flask, render_template, request, session, redirect, url_for

from App import db

app = Flask(__name__)


@app.route('/user/HomePage')
def home():
    return render_template('HomePage.html', active_page='Homepage.html ')
    


@app.route('/user/Workouts', methods=['POST', 'GET'])
def workouts():
    if request.method == "GET":
        return render_template("Workouts.html")


@app.route('/user/OutdoorWorkouts', methods=['POST', 'GET'])
def OutdoorWorkouts():
    if request.method == "GET":
        return render_template("OutdoorWorkouts.html")
    elif request.method == "POST":
        ExerciseType = request.form["ExerciseType"]
        Distance = request.form["Distance"]
        TimeTaken = request.form["TimeTaken"]
        DateCompleted = request.form["DateCompleted"]
        try:
            db.create_outdoor_workout(ExerciseType, Distance, TimeTaken, DateCompleted)
            return redirect(url_for('workouts'))
        except sqlite3.Error as e:
            print(e)
            return render_template('OutdoorWorkouts.html')


@app.route('/user/LoginPage', methods=['POST', 'GET'])
def login():
    if request.method == "GET":
        return render_template("LoginPage.html")
    # default loads the login page

    elif request.method == "POST":  # only runs if the user submits the login form
        email = request.form["email"]
        password = request.form["password"]
        user = [(email, password)]  # stores the email and password from the form as a local variable

        try:
            if db.get_user(email) == user:  # checks if the email matches the password stored in the database
                session['username'] = request.form['email']  # sets the session username to the email address
                return redirect(url_for('home'))  # redirects the user to the home page of the website

            else:
                text = "Enter a valid email and password"
                return redirect(url_for('login', text=text))
        except sqlite3.Error as e:
            print(e)
            return redirect(url_for('login', error=e))


@app.route('/11', methods=['POST', 'GET'])
def register():
    if request.method == "GET":
        return render_template('SignUp.html')
    elif request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        forename = request.form["forename"]
        surname = request.form["surname"]
        dob = request.form["dob"]

        db.create_user(email.lower(), password, forename.lower(), surname.lower(), dob)
        return redirect(url_for('login'))
    return render_template("SignUp.html")


@app.route('/', methods=['POST', 'GET'])
def GymWorkouts():
    if request.method == "GET":
        return render_template('CustomWorkouts.html')
    elif request.method == "POST":
        Exercise = request.form["exercise"]
        email = request.form['email']
        Reps = request.form["reps"]
        Weight = request.form["weight"]
        DateDone = request.form["date completed"]

        db.create_custom_workout(email, Exercise, Reps, Weight, DateDone)
        return redirect(url_for('GymWorkouts'))
    return render_template("CustomWorkouts.html")
#
#
# @app.route('/user/Outdoor', methods=['POST', 'GET'])
# def OutdoorWorkouts():
#     if request.method == "GET":
#         return render_template('OutdoorWorkouts.html')
#     elif request.method == "POST":
#         email = ['username']
#         ExerciseType = request.form["exercisetype"]
#         Distance = request.form["distance"]
#         TimeTaken = request.form["timetaken"]
#
#         db.create_outdoor_workout(email, ExerciseType, Distance, TimeTaken)
#         return redirect(url_for('home'))
#     return render_template("OutdoorWorkouts.html")
#
#
# @app.route('/preplannedworkouts', methods=['POST', 'GET'])
# def PrePlannedWorkouts():
#     if request.method == "GET":
#         return render_template('PrePlannedWorkouts.html')
#     elif request.method == "POST":
#         email = ['username']
#         Workout = request.form["workout"]
#
#         db.record_planned_workout(email, Workout)
#         return redirect(url_for('home'))
#     return render_template("PrePlannedWorkouts.html")
#

if __name__ == '__main__':
    app.run()



# validation can be done in JS and HTML5 doesn't have to be server side :)

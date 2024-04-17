import sqlite3
import flask
from flask import Flask, render_template, request, session, redirect, url_for

from App import db

app = Flask(__name__)


@app.route('/user/HomePage')
def home():
    return render_template('HomePage.html')


@app.route('/user/Workouts')
def workouts():
    return render_template("Workouts.html")



@app.route('/1', methods=['POST', 'GET'])
def login():
    if request.method == "GET":
        return render_template("LoginPage.html")
    # default loads the login page

    elif request.method == "POST":  # only runs if the user submits the login form
        email = request.form["email"]
        password = request.form["password"]
        user = [(email, password)]  # stores the email and password from the form as a local variable

        try:
            if db.get_user(email, password) == user:  # checks if the email matches the password stored in the database
                session['username'] = request.form['email']  # sets the session username to the email address
                return redirect(url_for('home'))  # redirects the user to the home page of the website

            else:
                text = "Enter a valid email and password"
                return redirect(url_for('login'))
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


@app.route('/47', methods=['POST', 'GET'])
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
@app.route('/', methods=['POST', 'GET'])
def OutdoorWorkouts():
    if request.method == "GET":
        return render_template('OutdoorWorkouts.html')
    elif request.method == "POST":
        exercisetype = request.form["exercisetype"]
        distance = request.form["distance"]
        timetaken = request.form["timetaken"]
        email = request.form["email"]
        date = request.form["date"]

        db.create_outdoor_workout(email, exercisetype, distance, timetaken, date)
        return redirect(url_for('workouts'))
    return render_template("OutdoorWorkouts.html")
#

@app.route('/23', methods=['POST', 'GET'])
def PrePlannedWorkouts():
    if request.method == "GET":
        return render_template('PrePlannedWorkouts.html')
    elif request.method == "POST":
        email = request.form["email"]
        workout = request.form["type_of_exercise"]
        datecompleted = request.form["datecompleted"]

        db.record_planned_workout(email, workout, datecompleted)
        return redirect(url_for('PrePlannedWorkouts'))
    return render_template("PrePlannedWorkouts.html")


@app.route('/21', methods=['POST', 'GET'])
def myData():
    if request.method == "GET":
        return render_template('HomePage.html')
    else:
        return render_template('MyProgress.html')

@app.route('/22', methods=['POST', 'GET'])
def myAccount():
    if request.method == "GET":
        return render_template('HomePage.html')
    else:
        return render_template('MyProgress.html')



if __name__ == '__main__':
    app.run()

# validation can be done in JS and HTML5 doesn't have to be server side :)

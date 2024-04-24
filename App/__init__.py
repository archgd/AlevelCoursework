import sqlite3
import flask
from flask import Flask, render_template, request, session, redirect, url_for

from App import db

app = Flask(__name__)
app.secret_key = "ILOVEKEYS"


@app.route('/8')
def home():
    return render_template('HomePage.html')


@app.route('/')
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
                return redirect(url_for('login'), text)
        except sqlite3.Error as e:
            print(e)
            return redirect(url_for('login', error=e))


@app.route('/8', methods=['POST', 'GET'])
def register():
    if request.method == "GET":
        return render_template('SignUp.html')
    elif request.method == "POST":
        print("first")
        email = request.form["email"]
        password = request.form["password"]
        forename = request.form["forename"]
        surname = request.form["surname"]
        dob = request.form["dob"]
        print("second")

        session['username'] = request.form["email"]

        db.create_user(email.lower(), password, forename.lower(), surname.lower(), dob)
        return redirect(url_for('MyOutdoorProgressQuerey'))


@app.route('/GymWorkouts', methods=['POST', 'GET'])
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
@app.route('/OutdoorWorkouts', methods=['POST', 'GET'])
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

@app.route('/PrePlannedWorkouts', methods=['POST', 'GET'])
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


@app.route('/MyProgressQuerey', methods=['POST', 'GET'])
def myProgressQuerey():
    if request.method == "GET":
        return render_template('MyProgressQuerey.html')
    elif request.method == "POST":
        email = request.form["email"]
        exercise = request.form["type_of_exercise"]

        db.get_exercises(email, exercise)
        return redirect(url_for('MyProgress'))
    return render_template("MyProgressQuerey.html")


@app.route('/MyOutdoorProgressQuerey', methods=['POST', 'GET'])
def MyOutdoorProgressQuerey():
    if request.method == "GET":
        return render_template("MyOutdoorProgressQuerey.html")
    elif request.method == "POST":
        email = session['username']
        exercise = request.form["exercise"]
        db.get_outdoor_exercises(email, exercise)
        return render_template("MyOutdoorProgress.html", exercise = exercise)



if __name__ == '__main__':
    app.run()



import sqlite3

from flask import Flask, render_template, request, session, redirect, url_for

from App import db


app = Flask(__name__)


@app.route('/user/HomePage')
def home():
    return 'welcome'
    if request.method == "POST":
        return render_template("HomePage.html")
    else:
        return render_template("Workouts.html")


@app.route('/user/Workouts', methods=['POST', 'GET'])
def workouts():
    if request.method == "GET":
        return render_template("Workouts.html")


@app.route('/1', methods=['POST', 'GET'])
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


@app.route('/1', methods=['POST', 'GET'])
def login():
    if request.method == "GET":
        return render_template("LoginPage.html")
    elif request.method == "POST":
        session['username'] = request.form['email']
        session['password'] = request.form['password']

        try:
            if login(session['username'], session['password']):

                print(session)
                print('hello')
                return redirect(url_for('home'))
            else:
                return redirect(url_for('login'))
        except sqlite3.Error as e:
            print(e)
            return redirect(url_for('login', error=e))


@app.route('/', methods=['POST', 'GET'])
def register():
    if request.method == "GET":
        return render_template('SignUp.html')
    elif request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        forename = request.form["forename"]
        surname = request.form["surname"]
        dob = request.form["dob"]
        try:
            if db.get_user(email):
                text = "email already registered"
            db.check_email(email)
            db.check_password(password)
            db.check_name(forename)
            db.check_name(surname)
            db.check_dob(dob)

            db.create_user(email, password, forename, surname, dob)
            return redirect(url_for('login'))
        except sqlite3.Error as e:
            print(e)
            return render_template("SignUp.html")

    return render_template("SignUp.html")




if __name__ == '__main__':
    app.run()

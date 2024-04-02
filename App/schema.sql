CREATE TABLE IF NOT EXISTS user
(
    email    VARCHAR(25) NOT NULL,
    password VARCHAR(25) NOT NULL,
    forename VARCHAR(30) NOT NULL,
    surname  VARCHAR(30) NOT NULL,
    dob      VARCHAR(10) NOT NULL,
    PRIMARY KEY (email)
);

CREATE TABLE IF NOT EXISTS outdoorworkouts
(

    ExerciseType VARCHAR(40) NOT NULL,
    Distance integer(4) NOT NULL,
    TimeTaken integer(4) NOT NULL,
    DateCompleted  VARCHAR(10) NOT NULL,
    FOREIGN KEY (email) REFERENCES user(email)


);

CREATE TABLE IF NOT EXISTS gymworkouts
(
    Exercise VARCHAR(40) NOT NULL,
    Reps integer(4) NOT NULL,
    Weight integer(3) NOT NULL,
    DateDone VARCHAR(10) NOT NULL,
    FOREIGN KEY (email) REFERENCES user(email)



)

CREATE TABLE IF NOT EXISTS preplannedworkouts
(
    Workout VARCHAR(40) NOT NULL,
    Date VARCHAR(10) NOT NULL,
    FOREIGN KEY(email) REFERENCES user(email)
)

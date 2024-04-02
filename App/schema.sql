CREATE TABLE IF NOT EXISTS user
(
    email    VARCHAR(25) NOT NULL UNIQUE,
    password VARCHAR(25) NOT NULL,
    forename VARCHAR(30) NOT NULL,
    surname  VARCHAR(30) NOT NULL,
    dob      DATE NOT NULL,
    PRIMARY KEY (email)
);

CREATE TABLE IF NOT EXISTS outdoorworkouts
(
    email VARCHAR(25) NOT NULL UNIQUE,
    ExerciseType VARCHAR(40) NOT NULL,
    Distance integer(4) NOT NULL,
    TimeTaken integer(4) NOT NULL,
    DateCompleted  DATE NOT NULL,
    FOREIGN KEY (email) REFERENCES user(email)


);

CREATE TABLE IF NOT EXISTS gymworkouts
(
    email VARCHAR(25) NOT NULL UNIQUE,
    Exercise VARCHAR(40) NOT NULL,
    Reps integer(4) NOT NULL,
    Weight integer(3) NOT NULL,
    DateDone DATE NOT NULL,
    FOREIGN KEY (email) REFERENCES user(email)



);

CREATE TABLE IF NOT EXISTS preplannedworkouts
(
    email VARCHAR(25) NOT NULL UNIQUE,
    Workout VARCHAR(40) NOT NULL,
    Date DATE NOT NULL,
    FOREIGN KEY(email) REFERENCES user(email)
)

-- DROP table users;
-- DROP table outdoorworkouts
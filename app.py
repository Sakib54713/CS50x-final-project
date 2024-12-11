from flask import Flask, render_template, request
import sqlite3
import json


app = Flask(__name__)

with open('static/personalities.json') as file:
    personalities = json.load(file)

with open('static/story.json') as file:
    story = json.load(file)

@app.route("/")
def index():
    conn, db = create_database()

    result = db.execute("SELECT count FROM button_presses WHERE id = 1")
    counter_row = result.fetchone()  

    if counter_row:
        counter = counter_row[0]
    else:
        counter = 0

    conn.close()

    return render_template("index.html", counter=counter)

@app.route("/types")
def types():
    return render_template("types.html", personalities=personalities)

@app.route("/story", methods=["GET", "POST"])
def story_view():


    if request.method == "GET":
        return render_template("story.html", story=story)


@app.route("/submit", methods=["POST"])
def submit_query():
    answers = request.form.getlist('answers[]')

    countA = 0
    countB = 0
    countC = 0
    title = None
    description = None

    for answer in answers:
        if answer == 'a':
            countA += 1
        if answer == 'b':
            countB += 1
        if answer == 'c':
            countC += 1

    if countA > countB and countA > countC:
        title = personalities[0]['title']
        description = personalities[0]['description']

    elif countB > countA and countB > countC:
        title = personalities[1]['title']
        description = personalities[1]['description']

    elif countC > countA and countC > countB:
        title = personalities[2]['title']
        description = personalities[2]['description']

    elif countA == countB:
        title = personalities[3]['title']
        description = personalities[3]['description']

    elif countA == countC:
        title = personalities[4]['title']
        description = personalities[4]['description']

    elif countB == countC:
        title = personalities[5]['title']
        description = personalities[5]['description']

    conn, db = create_database()
    db.execute("UPDATE button_presses SET count = count + 1 WHERE id = 1")
    conn.commit()
    conn.close()

    return render_template("result.html", title=title, description=description)


def create_database():
    conn = sqlite3.connect("counter.db")
    db = conn.cursor()

    db.execute("""
    CREATE TABLE IF NOT EXISTS button_presses (id INTEGER PRIMARY KEY, count INTEGER)
    """)
    conn.commit()

    db.execute("""
    INSERT OR IGNORE INTO button_presses (id, count) VALUES (1, 0)
    """)
    conn.commit()

    return conn, db


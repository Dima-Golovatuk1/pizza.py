from flask import Flask
from flask import render_template
import random
import datetime
import sqlite3

app = Flask(__name__)



@app.route('/')
def hellp_world():
    return render_template("base.html")


@app.route('/menu', methods=["GET", "POST"])
def name():
    with sqlite3.connect("data.db") as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM MENU")
        datamenu = cursor.fetchall()
    return render_template("menu.html", data=datamenu)


@app.route('/contact')
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
import sqlite3

from flask import Flask, redirect, render_template, request, url_for

db = sqlite3.connect("books-collection.db")
cursor = db.cursor()
cursor.execute(
    "CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE,\
          author varchar(250) NOT NULL, rating FLOAT NOT NULL)"
)

cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
db.commit()
# from flask_wtf import FlaskForm
# from wtforms import SelectField, StringField, SubmitField
# from wtforms.validators import URL, DataRequired

app = Flask(__name__)

all_books = []


@app.route("/")
def home():
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_book = {
            "title": request.form["title"],
            "author": request.form["author"],
            "rating": request.form["rating"],
        }
        all_books.append(new_book)
        return redirect(url_for("home"))
    return render_template("add.html")

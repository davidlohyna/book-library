from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL

app = Flask(__name__)

all_books = []

class AddBook(FlaskForm):
    name = 
    author =
    rating =


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add", methods=["GET", "POST"])
def add():
    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, redirect, render_template, request, url_for
from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField
from wtforms.validators import URL, DataRequired

app = Flask(__name__)

all_books = []


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add", methods=["GET", "POST"])
def add():
    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)

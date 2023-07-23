from flask import Flask, flash, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "123456"
db = SQLAlchemy(app)


# CREATE TABLE
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f"<Book {self.title}>"


@app.route("/")
def home():
    with app.app_context():
        ##READ ALL RECORDS
        # all_books = db.session.execute(db.select(Book).order_by(Book.title)).scalars()
        return render_template("index.html", books=Book.query.all())


@app.route("/delete")
def delete():
    book_id = request.args.get("id")
    book_to_delete = db.get_or_404(Book, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_book = Book(
            title=request.form["title"],
            author=request.form["author"],
            rating=request.form["rating"],
        )
        db.session.add(new_book)
        db.session.commit()
        flash("Record was successfully added")
        return redirect(url_for("home"))
    return render_template("add.html")


@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        # UPDATE RECORD
        book_id = request.form["id"]
        book_to_update = db.get_or_404(Book, book_id)
        book_to_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for("home"))
    book_id = request.args.get("id")
    selected_book = db.get_or_404(Book, book_id)
    # with app.app_context():
    #     selected_book = db.session.execute(
    #         db.select(Book).filter_by(id=book_id)
    #     ).scalar()
    # return redirect(url_for("home"))
    return render_template("edit.html", book=selected_book)  #


with app.app_context():
    db.create_all()

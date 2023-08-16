# Flask SQL Alchemy Book Collection App

This is a simple Flask web application that allows you to manage a collection of books using a SQLite database with SQLAlchemy.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Routes](#routes)
- [Database](#database)
- [Contributing](#contributing)

## Installation

1. Clone the repository:

```
git clone https://github.com/your-username/flask-book-collection-app.git
```
2. Install the required dependencies:

```
pip install -r requirements.txt
```

4. Run the application:

```
python app.py
```

## Usage

After starting the application, open a web browser and navigate to http://localhost:5000 to access the book collection interface. You can add, edit, and delete books from the collection.
### Routes

    / - Home page displaying the list of books in the collection.
    /add - Page to add a new book to the collection.
    /edit?id=<book_id> - Page to edit the details of a specific book.
    /delete?id=<book_id> - Endpoint to delete a book from the collection.

### Database

This application uses an SQLite database to store the book collection. The database schema includes a Book table with the following columns:

    id (Primary Key, Integer): Unique identifier for each book.
    title (String): Title of the book (unique and non-null).
    author (String): Author of the book (non-null).
    rating (Float): Rating of the book (non-null).

### Contributing

Contributions are welcome! If you find any issues or want to enhance the application, feel free to fork the repository and create a pull request.

    Fork the repository.
    Create a new branch: git checkout -b feature/my-feature.
    Make your changes and commit them: git commit -am 'Add some feature'.
    Push to the branch: git push origin feature/my-feature.
    Create a new Pull Request.


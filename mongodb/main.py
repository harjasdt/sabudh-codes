import os
from pymongo import MongoClient  # PyMongo library to connect to MongoDB
from dotenv import load_dotenv  # Load environment variables from .env file

load_dotenv()  # Load MONGODB_URI from .env file

# Get connection string from .env file
MONGODB_URI = os.getenv("MONGODB_URI")

# MongoClient - Creates connection to MongoDB Atlas cluster
client = MongoClient(MONGODB_URI)

# Select database named "library" (creates if doesn't exist)
db = client.library

# Select collection named "books" inside the database (like a table in SQL)
books = db.books

# CREATE - Add new book to collection
def add_book(title, author, genre, year):
    # Create a document (JSON object) with book details
    book = {"title": title, "author": author, "genre": genre, "year": year}
    # insert_one() - Adds one document to the collection
    result = books.insert_one(book)
    # Returns the unique ID (_id) of the inserted document
    return result.inserted_id

# READ - Fetch books from collection
def get_all_books():
    # find({}) - Gets all documents from collection
    # {"_id": 0} - Projection to hide the _id field (0=exclude, 1=include)
    return list(books.find({}, {"_id": 0}))

def get_book_by_title(title):
    # find_one() - Gets first matching document
    # {"title": title} - Filter condition (WHERE clause in SQL)
    return books.find_one({"title": title}, {"_id": 0})

# UPDATE - Modify existing book
def update_book(title, new_genre):
    # update_one() - Updates first matching document
    # {"title": title} - Filter to find which book to update
    # {"$set": ...} - MongoDB operator to update specific fields
    books.update_one({"title": title}, {"$set": {"genre": new_genre}})

# DELETE - Remove book from collection
def delete_book(title):
    # delete_one() - Removes first matching document from collection
    # {"title": title} - Filter to find which book to delete
    books.delete_one({"title": title})

if __name__ == "__main__":
    print("MongoDB connection ready! Use this with app.py for Streamlit dashboard")
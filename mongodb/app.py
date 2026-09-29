import streamlit as st
from main import add_book, get_all_books, get_book_by_title, update_book, delete_book

st.set_page_config(page_title="Book Management", layout="wide")

st.title("📚 Book Management System")

# Sidebar menu
menu = st.sidebar.radio("Menu", ["View Books", "Add Book", "Update Book", "Delete Book"])

if menu == "View Books":
    st.subheader("All Books")
    books = get_all_books()
    if books:
        for book in books:
            st.write(f"**{book['title']}** by {book['author']} ({book['year']}) - {book['genre']}")
    else:
        st.info("No books found")

elif menu == "Add Book":
    st.subheader("Add New Book")
    title = st.text_input("Book Title")
    author = st.text_input("Author")
    genre = st.text_input("Genre")
    year = st.number_input("Year", min_value=1900, max_value=2100)

    if st.button("Add Book"):
        add_book(title, author, genre, int(year))
        st.success(f"✓ Book '{title}' added successfully!")

elif menu == "Update Book":
    st.subheader("Update Book Genre")
    title = st.text_input("Book Title to Update")
    new_genre = st.text_input("New Genre")

    if st.button("Update"):
        update_book(title, new_genre)
        st.success(f"✓ Book updated successfully!")

elif menu == "Delete Book":
    st.subheader("Delete Book")
    title = st.text_input("Book Title to Delete")

    if st.button("Delete"):
        delete_book(title)
        st.success(f"✓ Book deleted successfully!")

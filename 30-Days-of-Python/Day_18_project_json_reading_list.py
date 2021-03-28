# Day 18 Project: JSON Reading List
# Project details: https://teclado.com/30-days-of-python/python-30-day-18-project

import json

def add_book():
    books = get_all_books()

    title = input("Title: ").strip().title()
    author = input("Author: ").strip().title()
    year = input("Year: ").strip()

    book = {
        "title": title,
        "author": author,
        "year": year,
        "read": "Not Read"
        }
    
    books.append(book)

    with open("books.json", "w") as reading_list:
        json.dump(books, reading_list)
        
def get_all_books():
    with open("books.json", "r") as reading_list:
        return json.load(reading_list)

def show_books(books):
    print()

    for book in books:
        print(f"{book['title']}, by {book['author']} ({book['year']}) - {book['read']}")
    
    print()

def find_books():
    reading_list = get_all_books()
    matching_books = []

    search_term = input("Enter a book title: ").strip().lower()

    for book in reading_list:
        if search_term in book["title"].lower():
            matching_books.append(book)
    
    return matching_books

def delete_book(books, book_to_delete):
    books.remove(book_to_delete)


def mark_book_as_read(books, books_to_update):
    index = books.index(books_to_update)
    books[index]['read'] = "Read"


def update_reading_list(operation):
    books = get_all_books()
    matching_books = find_books()

    if matching_books:
        operation(books,matching_books[0])

        with open("books.json", "w") as reading_list:
            json.dump(books, reading_list)

menu_prompt = """Please enter one of the following options:

- 'a' to add a book
- 'd' to delete a book
- 'l' to list the books
- 'r' to mark a book as read
- 's' to search for a book
- 'q' to quit

What would you like to do? """

selected_option = input(menu_prompt).strip().lower()

while selected_option != "q":
    if selected_option == "a":
        add_book()
    elif selected_option == "d":
        update_reading_list(delete_book)
    elif selected_option == "l":
        reading_list = get_all_books()
        if reading_list:
            show_books(reading_list)
        else:
            print("Your reading list is empty.")
    elif selected_option == "r":
        update_reading_list(mark_book_as_read)
    elif selected_option == "s":
        matching_books = find_books()
        if matching_books:
            show_books(matching_books)
        else:
            print(f"No books with that title found.")
    else:
        print(f"'{selected_option}' is not a valid option!")
    
    selected_option = input(menu_prompt).strip().lower()
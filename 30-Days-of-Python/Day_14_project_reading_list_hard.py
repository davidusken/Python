# Day 14 Project: Reading List (Hard)
# Project details: https://teclado.com/30-days-of-python/python-30-day-14-project-hard/

# Users should be able to add a book to their reading list by providing a book title, an author's name, a year of publication, and whether or not the book has been read.
# The program should store information about all of these books in a file called books.csv, and this data should be stored in CSV format.
# Users should be able to retrieve the books in their reading list, and these books should be printed out in a user-friendly format.
# Users should be able to search for a specific book by providing a book title.
# Users should be able to mark a book as read by entering a book title. If there are multiple books with the same title, you can just mark the first matching book as read.
# Users should be able to delete books from their reading list by providing the book title for the book they want to delete. Once again, you can just delete the first matching book.
# Users should be able to select these options from a text menu, and they should be able to perform multiple operations without restarting the program. You can see an example of a working menu in the post on while loops (day 8).# Day 14 Project: Reading List (Hard Version)

# This program is written as code along and not owned or produced by me.

def add_book():
    title = input("Title: ").strip().title()
    author = input("Author: ").strip().title()
    year = input("Year: ").strip()

    with open("books.csv", "a") as reading_list:
        reading_list.write(f"{title},{author},{year},Not Read\n")
        
def get_all_books():
    books = []

    with open("books.csv", "r") as reading_list:
        for book in reading_list:
            title, author, year, read_status = book.strip().split(",")
            books.append({"title": title, "author": author, "year": year, "read": read_status})
    return books

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

        with open("books.csv", "w") as reading_list:
            for book in books:
                reading_list.write(f"{book['title']},{book['author']},{book['year']},{book['read']}\n")

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
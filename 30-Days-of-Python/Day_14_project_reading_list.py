# Day 14 Project: Reading List
# Project details: https://teclado.com/30-days-of-python/python-30-day-14-project-regular/

# Users should be able to add a book to their reading list by providing a book title, an author's name, and a year of publication.
# The program should store information about all of these books in a file called books.csv, and this data should be stored in CSV format.
# Users should be able to retrieve the books in their reading list, and these books should be printed out in a user-friendly format.
# Users should be able to search for a specific book by providing a book title.
# Users should be able to select these options from a text menu, and they should be able to perform multiple operations without restarting the program. You can see an example of a working menu in the post on while loops (day 8).

import time

def main():
    print("\nSelect operation:\n\n1. Add book\n2. View books\n3. Search for book\n4. Quit")
    userchoice = input("Enter: ").lower()
    if userchoice == "1":
        title = input("Enter book title: ").strip().title()
        author = input("Enter author: ").strip().title()
        year = input("Enter year of publication: ").strip().title()
        print("\nAdding book to list...")
        with open ("books.csv", "a") as f:
            f.write(f"{title},{author},{year}\n")

    elif userchoice == "2":
        f = get_books()
        view_books(f)
        
    elif userchoice == "3":
        searchstring = input("Enter title of book: ").strip().title()
        f = get_books()
        print("Scanning booklist...")
        time.sleep(1)
        for i in f:
            title, author, year = i.values()
            if searchstring == title:
                print(f"Match found in database for: '{searchstring}'\n")
                print(f"{title} by {author}, year of publication: {year}")
                elifchoice = input("\nReturn to main menu? [Y/N] ").lower()
                if elifchoice == "y":
                    return
            elif searchstring != title:
                print(f"'{searchstring}' does not match {title}!")

    elif userchoice == "4":
        print("Quitting...")
        quit()
        
    else:
        print("Invalid option, try again.")

def get_books():
    books = []

    with open ("books.csv", "r") as f:
        for book in f:
            title, author, year = book.strip().split(",")

            books.append({
                "title": title,
                "author": author,
                "year": year
            })
    return books

def view_books(books):
    print()

    for i in books:
        title, author, year = i.values()
        print(f"{title} by {author}, year of publication: {year}")

while True:
    main()
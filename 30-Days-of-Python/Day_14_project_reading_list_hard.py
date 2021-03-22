# Day 14 Project: Reading List (Hard)
# Project details: https://teclado.com/30-days-of-python/python-30-day-14-project-hard/

# Users should be able to add a book to their reading list by providing a book title, an author's name, a year of publication, and whether or not the book has been read.
# The program should store information about all of these books in a file called books.csv, and this data should be stored in CSV format.
# Users should be able to retrieve the books in their reading list, and these books should be printed out in a user-friendly format.
# Users should be able to search for a specific book by providing a book title.
# Users should be able to mark a book as read by entering a book title. If there are multiple books with the same title, you can just mark the first matching book as read.
# Users should be able to delete books from their reading list by providing the book title for the book they want to delete. Once again, you can just delete the first matching book.
# Users should be able to select these options from a text menu, and they should be able to perform multiple operations without restarting the program. You can see an example of a working menu in the post on while loops (day 8).# Day 14 Project: Reading List (Hard Version)

def addbook():
    title = input("Enter book title: ").strip().title()
    author = input("Enter author: ").strip().title()
    year = input("Enter year of publication: ").strip().title()
    print("\nAdding book to list...")
    with open ("books.csv", "a") as f:
        f.write(f"{title},{author},{year}\n")

def retrieve_books():
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
    for i in books:
        title, author, year = i.values()
        print(f"{title} by {author}, year of publication: {year}")

def del_book(books):
    # f = retrieve_books()
    # print(f)
    # f.remove(title)
    print(f)
    for i in books:
        title, author, year = i.values()
        f.remove(title)

def main():
    # Menu
    print("\nSelect operation:\n\n1. Add book\n2. View books\n3. Search for book\n4. Quit")
    userchoice= input("Enter: ")

    if userchoice == "1": # Add
        addbook()

    elif userchoice == "2": # View
        f = retrieve_books()
        view_books(f)

    elif userchoice == "3": # Search
        search = input("Enter book title: ").strip().title()
        f = retrieve_books()
        for i in f:
            title, author, year = i.values()
            if search == title:
                print()
                print(f"'{title}' found in list.\n\n1. View information\n2. Mark as read\n3. Delete from reading list")
                submenuchoice = input("Enter: ") 
                if submenuchoice == "1":
                    print(f"{title} by {author}, year of publication: {year}")
                elif submenuchoice == "2":
                    pass
                elif submenuchoice == "3":
                    #del_book(f)
                    # f = retrieve_books()
                    # print(f)
                    # for i in f:
                    #     title, author, year = i.values()
                    #     f.remove(title)
                    # print(f)

                    f = retrieve_books
                    f.remove(search)






    elif userchoice == "4":
        print("Quitting...")
        quit()

    else:
        print("Invalid option, try again.")

main()
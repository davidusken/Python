# Day 12 Project: Reading List
# Project details: https://teclado.com/30-days-of-python/python-30-day-12-project/

# Users should be able to add a book to their reading list by providing a book title, an author's name, and a year of publication. The program should store information about all of these books 
# in a Python list. Users should be able to display all the books in their reading list, and these books should be printed out in a user-friendly format. Users should be able to select these 
# options from a text menu, and they should be able to perform multiple operations without restarting the program. You can see an example of a working menu in the post on while loops (day 8).

booklist = [
    ("The Fellowship of the Ring", "J. R. R. Tolkien", "1954"),
    ("The Two Towers", "J. R. R. Tolkien", "1954"),
    ("The Return of the King", "J. R. R. Tolkien", "1955")
    ]

def userinterface():
    print("--- Reading list ---\n\n1. Add books to list\n2. View books in list\n3. Quit")
    userchoice = input("Enter: ")
    if userchoice == "1":
        title = input("Enter book title: ")
        author = input("Enter author: ")
        year = input("Enter year of publication: ")

        for i in booklist:
            booklist.append((title, author, year))
            return

    elif userchoice == "2":
        print("\nSelection confirmed, printing books in your list:\n")
        for i in booklist:
            print(f"{i[0]} ({i[2]}) by {i[1]}")

        elifchoice = input("\nReturn to main menu? [Y/N] ")
        if elifchoice == "y":
            return
        elif elifchoice == "n":
            quit()
    elif userchoice == "3":
        quit()
    else:
        "Something went wrong."


def main():
    while True:
        userinterface()

main()
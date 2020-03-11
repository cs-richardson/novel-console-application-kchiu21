"""
Kolton Chiu
This program uses the database novel which includes a novel name and the author,
the user will get 3 choices when the program starts. The user can view all available books,
and add new books to the database.
"""
# Imports
import sqlite3 as sq

# Identify where the database is located
con = sq.connect("noveltest.db")
c = con.cursor()


# This functions get data from table novel, and author
def find_novel():
    res = c.execute("SELECT isbn,title,name from novel JOIN author WHERE author.authorid = novel.authorid")
    data = c.fetchall()  # Gets the data from the table
    return data

# This functions get data from author
def find_author_name():
    res = c.execute("SELECT name from author")
    data = c.fetchall()  # Gets the data from the table
    return data

# This function gets all data from the database and displays it for the user
def render_novel():
    novels = find_novel()
    tbl = "~~  isbn number   ~  novel name  ~  author's name ~~\n\n|"
    for row in novels:
        for field in row:
            tbl += str(field)
            tbl += ", "
        tbl += "\n\n|"
    tbl += "---------------------------"
    print("\n\nList of novels\n\n" + tbl)
    return

# This function is used to add a new novel to the database
def add_novel():
    count = 0
    author_id = 0
    author_name = find_author_name()
    author = "test"
    tbl = "~~  author's name ~~\n\n|"
    for row in author_name:
        for field in row:
            count = count + 1
            tbl += str(count) + ". " + str(field) 
            tbl += ", "
        tbl += "\n\n|"
    tbl += "---------------------------"
    print("\n\nList of no\n\n" + tbl)
    author = input("Choose an option (1, 2, or 3) and type out author's name:\t")
    if author == "Joe":
        author_id = 1
    elif author == "Jane":
        author_id = 2
    elif author == "Jonh":
        author_id = 3
    else:
        print ("\n\### this author doesn't exist ###\n\n")
        return
    new_novel = input("Type new novel's name: ")
    new_isbn = input("Type new novel's isbn number: ")
    ins_str = 'INSERT INTO novel (isbn, authorid, title) Values (' + str(new_isbn) + ', ' + str(author_id) + ', "' + str(new_novel) + '");'
    res = c.execute(ins_str)
    con.commit()
    return


# Let the user close the program
def end_program():
    con.close()


# Main screen of program, print is outside to prevent two prints of this message
print("\n\n~~~ Welcome to Kolton's novel database ~~~")
def render_menu():
    print("~ 1. Display novels")
    print("~ 2. Add a novel to database")
    print("~ 3. Close program")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n")
    choice = int(input("Choose an option (1, 2, or 3):\t"))

    if choice == 1:
        render_novel()
    elif choice == 2:
        add_novel()
    elif choice == 3:
        end_program()
        return False
    elif choice < 0 or choice > 3:
        print ("\n******* Please choose 1, 2, or 3 *******\n")
        
    return True


# This repeats the function until the user chooses to close program
while render_menu():
    print("\n\n ~~~ Welcome to Kolton's novel database ~~~")

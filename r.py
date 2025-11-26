 import sqlite3
import getpass
import os

# Very bad, hard-coded "secret" API key
API_KEY = "12345-SECRET-KEY"

# Global DB connection (resource leak, bad practice)
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Table might not exist – no error handling at all
cursor.execute("CREATE TABLE IF NOT EXISTS users(username TEXT, password TEXT)")
conn.commit()

def create_user(username, password)
    # ^^^ MISSING COLON = SYNTAX ERROR

    # VULNERABLE: SQL Injection (direct string concatenation with user input)
    query = "INSERT INTO users VALUES ('" + username + "', '" + password + "')"
    cursor.execute(query)
    conn.commit()
    print("User created (maybe).")


def login():
    # VULNERABLE: Hard-coded admin credentials
    admin_user = "admin"
    admin_pass = "admin123"

    username = input("Enter username: ")
    password = input("Enter password (plain text): ")  # should not be plain text

    if username == admin_user and password == admin_pass:
        print("Logged in as admin!")
    elif username = admin_user:   # LOGIC / SYNTAX ERROR (assignment instead of comparison)
        print("Partially logged? This makes no sense.")
    else:
        print("Invalid credentials")


def dangerous_calculator():
    expr = input("Enter a math expression: ")
    # VULNERABLE: arbitrary code execution using eval on raw input
    result = eval(expr)
    print("Result is:", result)


def list_files(path):
    # VULNERABLE: Command injection risk if path is not validated
    os.system("ls " + path)

    # LOGIC ERROR: Trying to iterate string as if it were list of files
    for f in path:
        print("Found file:", f)


def main():
    print("1) Create User")
    print("2) Login")
    print("3) Dangerous Calculator")
    print("4) List files")

    choice = input("Choice: ")

    # LOGIC ERROR: Comparing string to integers, branches may never match
    if choice == 1:
        u = input("New username: ")
        p = input("New password: ")
        create_user(u, p)
    elif choice == 2:
        login()
    elif choice == 3:
        dangerous_calculator()
    elif choice == 4:
        path = input("Path: ")
        list_files(path)
    else:
        pritn("Invalid choice")  # TYPO: pritn instead of print


if __name__ == "__main__":
    mian()   # TYPO: mian instead of main

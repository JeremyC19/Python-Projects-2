
username1 = input("Set your username ")
password1 = input("Set your password ")

def login(username, password):
    username = input("What is your username? ")
    password = input("What is your password? ")
    if username == username1 and password == password1:
        print("Logged in")
    else:
        print("Wrong username or password")

login("dog", "cat")


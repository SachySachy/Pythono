"""This program is a website that user day and can be used to sign in"""
import os
from datetime import datetime
from flask import Flask, render_template, redirect, url_for, request
from passlib.hash import sha256_crypt

app = Flask(__name__)
app.secret_key = "key"

@app.route("/")
def home():
    """This is the base of the website"""
    output = "asd"
    return render_template("login.html", output=output)

@app.route("/registration")
def registration():
    """registration"""
    if request.method =="POST":
        username = request.form["username"]
        password = request.form["password"]
        lists = text2list()
        username_password_handler(lists,username,password)
        return redirect(url_for("login"))
    return render_template("registration.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    """Enter user password data to enter image"""
    if request.method =="POST":
        username = request.form["username"]
        password = request.form["password"]
        lists = text2list()
        if logging_id(lists,username,password):
            return redirect(url_for("user", test=username))
    failed(username)
    return render_template("login.html")

@app.route("/<test>")
def user(test):
    """test to see if data is being saved"""
    return f"<h1>{test}</h1>"

@app.route("/change")
def change():
    """Changing password"""
    return render_template("change.html")

@app.route("/images")
def images():
    """this has the data and the images"""
    return render_template("images.html")

def list2text(lists):
    """This converts array lists to the text file"""
    if os.path.exists('passfile'):
        os.remove('passfile')
    with open('passfile', "a") as fine:
        for element in lists:
            fine.writelines(element[0] + '\n')
            fine.writelines(element[1] + '\n')
    fine.close()


def failed(username):
    """this is the LOGGER logs username and time"""
    with open('logger', "a") as faill:
        now = datetime.now()
        now = str(now)
        faill.writelines(username + '\n')
        faill.writelines(now + '\n')
    faill.close()

def text2list():
    """This converts passfile to an array list"""
    lists = []
    users = []
    count = 0
    filee = open('passfile' ,"r")
    for data in filee:
        data = data.rstrip("\n")
        if (count % 2) == 0:
            users.append(data)
        else:
            users.append(data)
            lists.append(user)
            users = []
        count = count + 1
    filee.close()
    return lists

def logging_id(lists,username,password):
    """this is the logging file"""
    for users in lists:
        if users[0] == username:
            hash_pass = users[1]
            return sha256_crypt.verify(password,hash_pass)
        return False

def username_password_handler(lists, username, password):
    """This is the username and password handler"""
    username_e_f = 0
    for users in lists:
        if users[0] == username:
            username_e_f = 1
    if username_e_f == 0:
        password_status = check_password(password)
        if password_status:
            password_hash = sha256_crypt.hash(password)
            lists = add_to_list(lists,username,password_hash)
            list2text(lists)

def check_password(password):
    """This checks if the password is good"""
    password_good_f = 1
    if len(password) < 12:
        password_good_f = 0
        print("password to short")
    print("password long enough")
    capital_exists = 0
    digit_exists = 0
    for character in password:
        if character.isupper():
            capital_exists = 1
        if character.isdigit():
            digit_exists = 1
    total = password_good_f + capital_exists + digit_exists
    status = total == 3
    return status

def add_to_list(lists,username,password):
    """this adds a username and password to a list"""
    new_user = [username, password]
    lists.append(new_user)
    return lists

if __name__ == "__main__":
    app.run()

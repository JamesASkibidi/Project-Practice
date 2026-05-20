from flask import Flask, flash, redirect, render_template, request 





from database import DatabaseHandler
from lib.Is_matching import Is_matching
from lib.Is_length_valid import Is_length_valid
from lib.Is_present import Is_present
from werkzeug.security import generate_password_hash


app = Flask(__name__)





app.secret_key = 'ImInLoveWithRaff'

db = DatabaseHandler()
db.create_tables()

@app.route("/" , methods  =["POST" , "GET"])
def home():

    if request.method == "GET":
        return render_template("login.html")

    # form_data = request.form
    # username = form_data.get("username")
    # password = form_data.get("password")

    return "Logged In"



@app.route("/signup", methods=["POST" , "GET"])
def signup():

    if request.method == "GET":
        return render_template("signup.html")

    success = True

    form_data = request.form
    email = form_data.get("email")
    username = form_data.get("username")
    password = form_data.get("password")
    re_password = form_data.get("re-password")
    print(email, username , password)

    if not Is_present(username):
        success = False
        flash("No Username Given")

    if not Is_present(password):
        success = False
        flash("No Password Given")

    if not Is_present(re_password):
        success = False
        flash("No Password Confirmation Given")

    if not Is_present(email):
        email = None

    if not Is_length_valid(username , 4):
        success = False
        flash("Username must be bewteen 4 and 64 characters")

    if not Is_length_valid(password , 8):
        success = False
        flash("Password Does Not Meet Requirements")

    if not Is_matching(password , re_password):
        success = False
        flash("Passwords Do Not Match")

    if not success:
        return redirect("/signup")
    
    hashed_pswd = generate_password_hash(password)
    
    commit_success , message = db.create_user(username, hashed_pswd, email)

    if not commit_success:
        return message
    
    return "Account Created!"


# def login():

app.run(debug=True)
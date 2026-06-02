from flask import Flask, flash, redirect, render_template, request 

from database import DatabaseHandler
from lib.Is_matching import Is_matching
from lib.Is_length_valid import Is_length_valid
from lib.Is_password_valid import Is_password_valid
from lib.Is_present import Is_present
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)

app.secret_key = 'ImInLoveWithRaff'

db = DatabaseHandler()
db.create_tables()

@app.route("/" , methods  =["POST" , "GET"])
def home():

    if request.method == "GET":
        return render_template("login.html")
    
    if request.method == "POST":



        form_data = request.form
        username = form_data.get("username")
        given_password = form_data.get("username")

        success , password_hash=  db.find_password(username)

        if not success or password_hash == None:
            flash("Authentication error , please try again")
            return redirect("/")
        
        if not check_password_hash(password_hash[0], given_password):
            flash("Authentication error , incorrect password")
            return redirect("/")


        return redirect("/dashboard")

    

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

    pswd_success , message = Is_password_valid(password)
    if not pswd_success:
        success = False
        flash(message)

    if not Is_matching(password , re_password):
        success = False
        flash("Passwords Do Not Match")

    if not success:
        return redirect("/signup")
    
    hashed_pswd = generate_password_hash(password)
    
    commit_success , message = db.create_user(username, hashed_pswd, email)

    if not commit_success:
        return render_template("sign_up_failure.html")
    
    return redirect("/dashboard")


@app.route("/dashboard")

def dashboard():
    return render_template("dashboard.html")




app.run(debug=True)
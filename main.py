from flask import Flask, flash, redirect, render_template, request 





from lib.Is_matching import Is_matching
from lib.Is_length_valid import Is_length_valid
from lib.Is_present import Is_present



app = Flask(__name__)

# Source - https://stackoverflow.com/a/54433731
# Posted by Grey Li, modified by community. See post 'Timeline' for change history
# Retrieved 2026-05-18, License - CC BY-SA 4.0




app.secret_key = 'ImInLoveWithRaff'

@app.route("/")
def home():
    return render_template('signup.html')



@app.route("/signup", methods=["POST"])
def signup():

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

    if not Is_present(email):
        success = False
        flash("No Email Given")

    if not Is_present(password):
        success = False
        flash("No Password Given")

    if not Is_present(re_password):
        success = False
        flash("No Password Confirmation Given")

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
        return redirect("/")
    

    return "Account Created!"

app.run(debug=True)

from flask import Blueprint, redirect, render_template, session

from lib.Is_auth import Is_auth


private = Blueprint("private" , __name__)

@private.before_request
def private_gate():
    print("checking auth state. . .")
    if not Is_auth():
        return redirect("/")
    


@private.route("/dashboard")
def dashboard():
    
    return render_template("dashboard.html")

@private.route("/logout")
def logout():
    #clear session data
    session.clear()
    #redirect to launch page
    return redirect("/")
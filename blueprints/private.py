
from flask import Blueprint, flash, redirect, render_template, request, session

from database import DatabaseHandler
from lib.Is_auth import Is_auth
from lib.Is_length_valid import Is_length_valid


private = Blueprint("private" , __name__)
db = DatabaseHandler()

@private.before_request
def private_gate():
    print("checking auth state. . .")
    if not Is_auth():
        return redirect("/")
    


@private.route("/dashboard")
def dashboard():
    username = session.get("current_user")
    success, tasks = db.retreive_tasks(username)

    if not success:
        flash("failed to retrieve tasks")
        return redirect("/dashboard")
    
    
    return render_template("dashboard.html", tasks = tasks)

@private.route("/logout")
def logout():
    #clear session data
    session.clear()
    #redirect to launch page
    return redirect("/")

@private.route("/add_task" , methods = ["POST"  ,"GET"])
def add_task():

    if request.method == "POST":
        form_data = request.form
        description = form_data.get("description")
        username= session.get("current_user")
        if username == None:
            flash("No user found")
            return redirect("/")

        if not Is_length_valid(description , 2):
            flash("invalid Description")
            return redirect("/add_task")
        
        success, message = db.create_task(description, username)

        if not success:
            flash(message)
            return redirect("/add_task")
        
        flash("Task successfully created")
        return redirect("/add_task")
    return render_template("add_task.html")


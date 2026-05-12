from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/")
def home():
    return render_template('signup.html')



@app.route("/signup", methods=["POST"])
def signup():

    form_data = request.form
    email = form_data.get("email")
    username = form_data.get("username")
    password = form_data.get("password")
    print(email, username , password)
    return "Account Created!"

app.run(debug=True)
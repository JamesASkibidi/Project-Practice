from flask import Flask


app = Flask(__name__)

@app.route("/")
def home():
    return "hellow World"

app.run(debug=True)
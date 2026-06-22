from flask import Flask

from blueprints.private import private
from blueprints.public import public
from database import DatabaseHandler


app = Flask(__name__)

app.secret_key = 'ImInLoveWithRaff'

db = DatabaseHandler()
db.create_tables()

app.register_blueprint(public)
app.register_blueprint(private)

app.run(debug=True)
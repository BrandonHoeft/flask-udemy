# runbook: $ `flask run` from CLI for dev/test

from flask import Flask

app = Flask(__name__)

@app.route('/')  # binds a URL to a function
def welcome():
    return "My first Flask app! THIS IS ROOT!"

@app.route('/name')
def what_is_dunder():
    return f"The value of __name__ is: {__name__}"


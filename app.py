# runbook: $ `flask run` from CLI for dev/test

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])  # app.route binds a URL to a function
def rootpage():
    name = ''
    if request.method == "POST" and "username" in request.form:
        name = request.form.get("username")
    return render_template("index.html",  # looks in templates/
                           name=name)  # we're giving name variable to our

# @app.route('/name')  # by default, this is a GET request
# def what_is_dunder():
#     return f"The value of __name__ is: {__name__}"

# @app.route('/method', methods=["GET", "POST"])
# def method():
#     if request.method == "POST":
#         return "You've used a POST request"
#     else:
#         return "You're probably using a GET request, as it's a default!"

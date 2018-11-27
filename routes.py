from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/testing/")
def testing():
    return "Test complete"

@app.route("/Bloop")
def bloop():
    return "Yep"

@app.route("/<random_string>")
def random(random_string):
    return "Here's what you entered: %s" % random_string

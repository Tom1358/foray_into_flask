import os
from flask import Flask, render_template

app = Flask(__name__) # creating instance of Flask, & storing in variable 'app'
    

@app.route("/") # a decorator (pie-notation) - '/' browses root directory
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(
        host = os.environ.get("IP", "0.0.0.0"),
        port = int(os.environ.get("PORT", "5000")),
        debug = True)
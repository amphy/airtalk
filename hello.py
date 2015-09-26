from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/login")
def hello():
    return render_template("login.html")
    
@app.route("/chat")
def hello():
    return render_template("chat.html")

if __name__ == "__main__":
    app.run()

from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
from flask import jsonify
app = Flask(__name__)

@app.route("/")
def hello1():
    return render_template("index.html")

@app.route("/login/")
def hello2():
    return render_template("login.html")
    
@app.route("/chat/", methods = ['POST'])
def hello3():
    return render_template("chat.html")

@app.route("/_confirm", methods = ['POST'])
def checkEmailFlightId():
    print request.form["email"]
    return "True"#jsonify({"hi": "bye"})

if __name__ == "__main__":
    print "hello"
    app.run()

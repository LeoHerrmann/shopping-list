from flask import Flask, escape, render_template

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/groups")
def groups():
	return render_template("groups.html")

from flask import Flask, redirect, url_for, render_template
import os

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/projects/ml")
def projects_ml():
    return render_template("project_ml.html")

@app.route("/projects/dviz")
def projects_dviz():
    return render_template("project_dataviz.html")

@app.route("/projects/abtest")
def projects_abtest():
    return render_template("project_ab.html")

@app.route("/projects/webdev")
def projects_webdev():
    return render_template("project_webdev.html")




if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

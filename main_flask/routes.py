"""Routes for parent Flask app."""
from flask import current_app as app
from flask import render_template

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

@app.route("/projects/dviz/tableauSnap")
def projects_dviz_tableauSnap():
    return render_template("project_dataviz_tableauSnap.html")

@app.route("/projects/abtest")
def projects_abtest():
    return render_template("project_ab.html")

@app.route("/projects/blog")
def projects_blog():
    return render_template("project_blog.html")

@app.route("/projects/blog/computervision")
def projects_blog_computervision():
    return render_template("project_blog_computervision.html")



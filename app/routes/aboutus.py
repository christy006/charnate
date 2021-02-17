from app import app
from flask import render_template, session, redirect, request, flash

@app.route("/about")
def about():
    return render_template("aboutus.html")

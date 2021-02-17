from app import app
from flask import render_template, session, redirect, request, flash
from app.classes.data import Organization

@app.route("/education")
def education():
    return render_template("education.html")

@app.route("/health")
def health():
    return render_template("health.html")

@app.route("/environment")
def environment():
    return render_template("environment.html")

@app.route("/cultural")
def cultural():
    return render_template("cultural.html")

@app.route("/other")
def other():
    otherorgs=Organization.objects(category="Other")
    return render_template("other.html", otherorgs=otherorgs)
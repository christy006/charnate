from app import app
from flask import render_template, session, redirect, request, flash
from app.classes.data import Organization

@app.route("/education")
def education():
    educationorgs=Organization.objects(category="Education")
    return render_template("education.html", educationorgs=educationorgs)

@app.route("/health")
def health():
    healthorgs=Organization.objects(category="Health")
    return render_template("health.html", healthorgs=healthorgs)

@app.route("/environment")
def environment():
    environmentorgs=Organization.objects(category="Environment")
    return render_template("environment.html", environmentorgs=environmentorgs)

@app.route("/cultural")
def cultural():
    culturalorgs=Organization.objects(category="Cultural")
    return render_template("cultural.html", culturalorgs=culturalorgs)

@app.route("/other")
def other():
    otherorgs=Organization.objects(category="Other")
    return render_template("other.html", otherorgs=otherorgs)

@app.route("/corporations")
def corporations():
    corporations=Organization.objects(types="Corporation")
    return render_template("corporations.html", corporations=corporations)
from app import app
from flask import render_template, session, redirect, request, flash
from app.classes.data import Contact
from app.classes.forms import ContactForm

@app.route("/about")
def about():
    return render_template("aboutus.html")

@app.route("/", methods=['GET', 'POST'])
def index():
    contactform=ContactForm()
    if contactform.validate_on_submit():
        newcontact=Contact(
            fname=contactform.fname.data,
            lname=contactform.lname.data,
            email=contactform.email.data,
            message=contactform.message.data,
        )
        newcontact.save()
        flash("You have contacted us!")
        newcontact.reload()
    return render_template('index.html', form=contactform)
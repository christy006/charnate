from app import app
from flask import render_template, session, redirect, request, flash
from app.classes.data import User, Organization, Relation
from app.classes.forms import OrganizationForm
import datetime as dt

@app.route("/orgsignup",methods=['GET', 'POST'])
def orgsignup():
    orgform=OrganizationForm()
    if orgform.validate_on_submit():
        neworg=Organization(
            name=orgform.name.data,
            types=orgform.types.data,
            description=orgform.description.data,
            category=orgform.category.data,
        )
        neworg.save()
        flash("Congratulations, your organization has joined Charnate!")
        neworg.reload()
        #TODO RETURN ANOTHER TEMPLATE
    return render_template('orgform.html', form=orgform)

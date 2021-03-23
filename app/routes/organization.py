from app import app
from flask import render_template, session, redirect, request, flash, url_for
from app.classes.data import User, Organization, Relation, Contact
from app.classes.forms import OrganizationForm, ContactForm
import datetime as dt
from bson.objectid import ObjectId
import stripe 

public_key='pk_test_51IYGwLGleDgRglJ62Brbfnegzc2oOwQhbOeKqK8zhPLWITefJ1tTRERUL75dmNVvfG50VHiR2WLorgCXcS6bCcbs00nJKN9bc2'
stripe.api_key="sk_test_51IYGwLGleDgRglJ6BUZMujw6Kg9WcKosKnHLCIQVnLabES6kizYGpnZrVVobE5DqinmiYPJke6kjdDQPkv78BvOa00xGLsLnt8"

@app.route("/payment",methods=["POST"])
def payment():
    customer=stripe.Customer.create(email=requestform['stripeEmail'],source=requestform['stripeToken'])
    charge=stripe.charge.create(
        customer=customer.id,
        amount=1999,
        currency='usd',
        description=donation
    )
    flash("Thank you for your donation!")

@app.route("/org/<orgid>",methods=['GET', 'POST'])
def org(orgid):
    orgid=ObjectId(orgid)
    org=Organization.objects.get(pk=orgid)
    orgcontact=ContactForm()
    if orgcontact.validate_on_submit():
        newcontact=Contact(
            owner=org,
            fname=orgcontact.fname.data,
            lname=orgcontact.lname.data,
            email=orgcontact.email.data,
            message=orgcontact.message.data,
        )
        newcontact.save()
        flash("You have contacted us!")
        newcontact.reload()
    return render_template("org.html", org=org, form=orgcontact, public_key=public_key)
    

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

@app.route("/orgclaim/<orgid>")
def orgclaim(orgid):
    claimOrg=Organization.objects.get(pk=orgid)
    currUser=User.objects.get(pk=session["currUserId"])
    currUser.update(organization=claimOrg)
    return redirect(url_for("profile"))

@app.route("/createrelation/<orgid>")
def createrelation(orgid):
    relateOrg=Organization.objects.get(pk=orgid)
    currUser=User.objects.get(pk=session["currUserId"])
    if relateOrg.types=="Nonprofit" and currUser.organization.types=="Corporation":
        newRelation=Relation(
            nonprofit=relateOrg,
            corporation=currUser.organization
        )
        newRelation.save()
    elif relateOrg.types=="Corporation" and currUser.organization.types=="Nonprofit":
        newRelation=Relation(
            nonprofit=currUser.organization,
            corporation=relateOrg
        )
        newRelation.save()
    else:
        flash("The two organizations you picked are the same type.")


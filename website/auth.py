from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db   ##----> from __init__.py import db
from flask_login import login_user, login_required, logout_user, current_user



auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():
    data = request.form
    print(data)
    return render_template("login.html")


@auth.route("/logout")
def logout():
    return "<p> Logout </p>"


@auth.route("/signup", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        email = request.form.get("email")
        firstName = request.form.get("firstName")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        if len(email) < 4:
            flash("Email must be longer than 4 characters", category="error")
        elif len(firstName) < 2:
            flash("First name has to be at least 2 characters", category="error")
        elif password1 != password2:
            flash("Passwords do not match", category="error")
        elif len(password1) < 5:
            flash("Password must be a minimum 5 characters long", category="error")
        else:
            # if ok add to the db + success flash
            new_user = User(email=email, firstName=firstName, password=generate_password_hash(
                password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash("Account created", category="success")
            #after creating the account redirect to the home page
            return redirect(url_for('views.home'))

    return render_template("sign_up.html")

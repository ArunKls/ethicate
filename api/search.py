from flask import Blueprint, request, redirect, url_for, render_template, flash
from flask_login import login_user
from werkzeug.security import check_password_hash

from models.users import User

search_blueprint = Blueprint("search", __name__, template_folder="templates")


@search_blueprint.route("/search", methods=["GET", "POST"])
def login():
    if request.method == "POST":

        print(request.form)
        name = request.form.get("query", None)
        # remember = bool(request.form.get("remember", False))

        user = User.query.filter(User.first_name.like(name)).all()

        if not user:
            print("no user")
            return redirect(url_for("profile.profile"))

    elif request.method == "GET":
        return render_template("home.html")

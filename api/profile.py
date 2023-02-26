from flask import Blueprint, request, redirect, url_for, render_template, flash, jsonify
from flask_login import login_user, login_required, current_user
from werkzeug.security import check_password_hash

from models.users import User
from services.search_service import perform_search
from services.profile_service import update_profile_service


profile_blueprint = Blueprint("profile", __name__, template_folder="templates")


@profile_blueprint.route("/profile", methods=["GET"])
@login_required
def profile():

    return render_template("profile.html", user=current_user)


@profile_blueprint.route("/update_profile", methods=["POST"])
@login_required
def update_profile():

    data = {
        "first_name": request.form.get("first_name", None),
        "last_name": request.form.get("last_name", None),
        "public_key": request.form.get("public_key", None),
    }

    update_profile_service(data)

    return render_template("profile.html", user=current_user)

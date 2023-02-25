from database import db
from models.users import User


class Profile(db.Model):
    __tablename__ = "profiles"

    id = db.Column(db.Integer, primary_key=True)

    profile_information = db.Column(db.MutableJson)

    def __init__(self, kwargs):
        profile_information = {}

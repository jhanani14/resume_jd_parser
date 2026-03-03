# app/models.py

from datetime import datetime
from . import db
from flask_login import UserMixin


# =========================
# USER TABLE
# =========================
class User(db.Model, UserMixin):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    # Relationship → one user can have many match histories
    matches = db.relationship(
        "MatchHistory",
        backref="user",
        lazy=True,
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<User {self.username}>"


# =========================
# MATCH HISTORY TABLE
# =========================
class MatchHistory(db.Model):
    __tablename__ = "match_history"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id"),
        nullable=False
    )

    score = db.Column(db.Float, nullable=False)

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    def __repr__(self):
        return f"<MatchHistory {self.score}% - User {self.user_id}>"
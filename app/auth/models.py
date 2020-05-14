from datetime import datetime

from flask_login import UserMixin
from sqlalchemy.orm import relationship
from werkzeug.security import check_password_hash

from app import db


class User(db.Model, UserMixin):
    __tablename__ = 'crypto_user'

    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(256), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def __init__(self, address, name, email):
        self.address = address
        self.name = name
        self.email = email

    def __repr__(self):
        return f'<User {self.email}>'

    def set_password(self, password):
        self.password = password

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_by_id(id):
        return User.query.get(id)

    @staticmethod
    def get_by_email(email):
        return User.query.filter_by(email=email).first()

    @staticmethod
    def get_by_email_and_password(email, password):
        return User.query.filter_by(email=email, password=password).first()

    @staticmethod
    def get_by_address(address):
        return User.query.filter_by(address=address).first()

    @staticmethod
    def get_all():
        return User.query.all()


class Wallet(db.Model):
    __tablename__ = 'crypto_wallet'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('crypto_user.id', ondelete='CASCADE'), nullable=False)
    token = db.Column(db.String(256), nullable=False)
    balance = db.Column(db.Float, nullable=False)

    def __init__(self, user_id, token, balance):
        self.user_id = user_id
        self.token = token
        self.balance = balance

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_by_id(user_id):
        return Wallet.query.get(user_id)

    @staticmethod
    def get_all():
        return Wallet.query.all()


class Opt(db.Model):
    __tablename__ = 'crypto_opt'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('crypto_user.id', ondelete='CASCADE'), nullable=False)
    number = db.Column(db.String(500), nullable=False)

    def __init__(self, user_id, number):
        self.user_id = user_id
        self.number = number

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_by_id(user_id):
        return Opt.query.get(user_id)

    @staticmethod
    def get_by_user_id(user_id):
        return Opt.query.filter_by(user_id=user_id).all()

    @staticmethod
    def get_by_number(number):
        return Opt.query.filter_by(number=number).first()

    @staticmethod
    def get_all():
        return Opt.query.all()


class Transaction(db.Model):
    __tablename__ = 'crypto_transaction'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('crypto_user.id', ondelete='CASCADE'), nullable=False)
    user_transferred = db.Column(db.Integer, db.ForeignKey('crypto_user.id', ondelete='CASCADE'), nullable=False)
    user_by = relationship("User", foreign_keys=[user_id])
    transferred_at = relationship("User", foreign_keys=[user_transferred])
    transferred_value = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, user_id, user_transferred, transferred_value):
        self.user_id = user_id
        self.user_transferred = user_transferred
        self.transferred_value = transferred_value

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_by_id(user_id):
        return Transaction.query.get(user_id)

    @staticmethod
    def get_by_user_id(user_id):
        return Transaction.query.filter_by(user_id=user_id).all()

    @staticmethod
    def get_by_user_transferred_id(user_transferred):
        return Opt.query.filter_by(user_transferred=user_transferred).first()

    @staticmethod
    def get_all():
        return Transaction.query.all()

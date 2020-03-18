
from app import db
#wallet_address_id = db.Column(db.Integer, db.ForeignKey('wallet_user.address', ondelete='CASCADE'), nullable=False)


class Wallet(db.Model):
    __tablename__ = 'crypto_wallet'

    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(256), nullable=False)
    balance = db.Column(db.Float(256), unique=True, nullable=False)

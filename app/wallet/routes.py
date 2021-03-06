import base64
import secrets

import jwt
from flask import render_template, request, jsonify
from flask_login import login_required, current_user

from ..extensions import db
from app.auth.models import User, Wallet, Opt, Transaction
from config import BaseConfig
from . import wallet_bp
from .utils import Messages, Constants


@wallet_bp.route('/')
@login_required
def index():
    if current_user.is_authenticated:
        wallet = Wallet.query.filter_by(user_id=current_user.id).first()
    else:
        wallet = None

    return load(wallet, current_user.id)


@wallet_bp.route('/transaccion/', methods=["POST"])
def transaccion():
    # Se valida que el usuario se encuentre autenticado
    # sino lo está se envia a la página de inicio.
    if not current_user.is_authenticated:
        return message("error", Messages.SESION_EXPIRED)

    # Se obtienen los datos enviados en el formulario
    address = request.form['address']
    number_ = request.form['opt']
    transferred_value = request.form['value']
    secret = request.form['secret']

    # Se valida que el monto a transferir sea un valor valido
    if float(transferred_value) < 1:
        return message("error", Messages.INVALID_TRANSFER_VALUE)

    # Se realiza la comprobación del token, si este está expirado o
    # no es valido se levanta un error
    try:
        decoded = jwt.decode(number_, base64.b64decode(BaseConfig.TOKEN_SECRET), algorithms=['HS256'])
    except jwt.exceptions.DecodeError:
        return message("error", Messages.INVALID_TOKEN)
    except jwt.exceptions.ExpiredSignature:
        return message("error", Messages.EXPIRED_TOKEN)

    # Se obtienen los valores que conforman el Token
    wallet = decoded[Constants.WALLET]
    ammount = decoded[Constants.AMMOUNT]
    pin = decoded[Constants.PIN]

    # Se valida que los datos que están en el token sean los mismo que
    # se enviaron en el formulario.
    if ammount != transferred_value or address != wallet or pin != secret:
        return message("error", Messages.TOKEN_NOT_BELONG_TRANSACCION)

    if address:
        user_search = User.get_by_address(address)
        if user_search:
            # Si el token ya existiera se levanta un error
            if Opt.get_by_number(number_):
                return message("error", Messages.TOKEN_ALREADY_USED)
            else:
                # usuario a quien se le va descontar de su wallet el valor
                wallet_current_user = Wallet.get_by_id(current_user.id)

                # usuario a quien se le va hacer la transaccion
                wallet_to_trans = Wallet.get_by_id(user_search.id)
                if wallet_current_user.balance < float(transferred_value):
                    return message("error", Messages.VALUE_DISPOSED_FAIL)

                # Se efectua la transación.
                wallet_current_user.balance = wallet_current_user.balance - float(transferred_value)
                db.session.commit()

                wallet_to_trans.balance = wallet_to_trans.balance + float(transferred_value)
                db.session.commit()

                # Se almacena el token usado para que no vulva a usarse
                opt = Opt(user_search.id, number_)
                opt.save()

                # transaccion
                transaction = Transaction(current_user.id, user_search.id, transferred_value)
                transaction.save()

                # Se retotorna satisfactoria la transacción y se redirige a cargar la
                # información de las transacciones realizadas
                return message("success", Messages.SUCESS_TRANSACTION)
        else:
            return message("error", Messages.INVALID_WALLET)
    else:
        return message("error", Messages.INVALID_WALLET)


def message(status, message, location='/login'):
    return jsonify({"status": status, "message": message, "location": location})


def load(wallet, user_id):
    """
    This method loads the transaction information, Secret Key, 
    list of transferences and the number of wallet.
    """
    opts = Opt.get_by_user_id(user_id)
    transaccions = Transaction.get_by_user_id(user_id)
    secret = secrets.token_hex(30)
    data = {'wallet': wallet, 'opts': opts, 'transaccions': transaccions, 'secret': secret}

    return render_template('wallet/home.html', data=data)

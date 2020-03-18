from flask import render_template, request, jsonify, redirect
from flask_login import login_required, current_user

from app import db
from . import wallet_bp

from app.auth.models import User, Wallet, Opt, Transaction


@wallet_bp.route('/')
@login_required
def index():
    wallet = None
    if current_user.is_authenticated:
        wallet = Wallet.query.filter_by(user_id=current_user.id).first()
    else:
        wallet = None
    opts = Opt.get_by_user_id(current_user.id)
    transaccions = Transaction.get_by_user_id(current_user.id)
    data = {'wallet': wallet, 'opts': opts, 'transaccions': transaccions}
    return render_template('wallet/home.html', data=data)


@wallet_bp.route('/transaccion/', methods=["POST"])
def transaccion():
    address = request.form['address']
    number_ = request.form['opt']
    transferred_value = request.form['value']
    user_search = None
    if address:
        user_search = User.get_by_address(address)
        if user_search:
            if Opt.get_by_number(number_):
                response_object = {"status": "error"}
            else:
                # usuario a quien se le va hacer la transaccion
                wallet_to_trans = Wallet.get_by_id(user_search.id)
                wallet_to_trans.balance = wallet_to_trans.balance + float(transferred_value)
                db.session.commit()

                # usuario a quien se le va descontar de su wallet el valor
                wallet_current_user = Wallet.get_by_id(current_user.id)
                wallet_current_user.balance = wallet_current_user.balance - float(transferred_value)
                db.session.commit()

                # borrar opt usada
                # opt = Opt.get_by_number(number_)
                # db.session.delete(opt)
                # db.session.commit()

                # Se almacena el token usado
                # para que no vulva a usarse
                opt = Opt(user_search.id, number_)
                opt.save()

                # transaccion
                transaction = Transaction(current_user.id, user_search.id, transferred_value)
                transaction.save()
                response_object = {"status": "success"}
        else:
            response_object = {"status": "error"}
    return jsonify(response_object)



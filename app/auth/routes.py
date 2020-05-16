import binascii
import hashlib
import os

from flask import render_template, redirect, url_for, request, jsonify
from flask_login import current_user, login_user, logout_user
from werkzeug.urls import url_parse

from ..extensions import login_manager
from . import auth_bp
from .models import User, Wallet
# utils
from .utils import get_address, get_token, get_balance


@auth_bp.route("/signup/", methods=["GET", "POST"])
def show_signup_form():
    if request.method == 'GET':
        if current_user.is_authenticated:
            return redirect(url_for('wallet.index'))
        else:
            return render_template('auth/signup_form.html')
    else:
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        # Comprobamos que no hay ya un usuario con ese email
        user = User.get_by_email(email)
        if user is not None:
            return message(status='error', message=f'El email {email} ya está siendo utilizado por otro usuario')
        else:
            # Creamos el usuario y lo guardamos
            user = User(address=get_address(), name=name, email=email)
            user.set_password(password)
            user.save()

            # Wallet
            wallet = Wallet(user.id, get_token(), get_balance())
            wallet.save()

            # Dejamos al usuario logueado
            login_user(user, remember=False)
            next_page = request.args.get('next', None)
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('wallet.index')
            return message(status='success', message='', location=next_page)


@auth_bp.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        remember = request.form['remember']

        # Se valida que exista el usuario y clave
        user = User.get_by_email_and_password(email, password)


        # Si se realiza con exito la comprobación del usuario 
        # se procede a ingresar a la página principal
        if user is not None:
            login_user(user, remember=remember)
            next_page = request.args.get('next')

            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('wallet.index')
            return message(status='success', message='', location=next_page)
        else:
            return message(status='error', message='Error de acceso', location='/login')
    else:
        if current_user.is_authenticated:
            return redirect(url_for('wallet.index'))
        else:
            return render_template('auth/login_form.html')


@auth_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('wallet.index'))


@login_manager.user_loader
def load_user(user_id):
    return User.get_by_id(int(user_id))


def message(status, message, location='/login'):
    return jsonify({"status": status, "message": message, "location": location})

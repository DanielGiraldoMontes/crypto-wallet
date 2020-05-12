import base58
import binascii
import hashlib
import math
import os
import random
import secrets


def generate_opt():
    digits = "0123456789"
    opt = ""
    for i in range(4):
        opt += digits[math.floor(random.random() * 10)]
    return opt


def get_address():
    # Creacion address Wallet
    fullkey = "80" + binascii.hexlify(os.urandom(32)).decode()
    sha256a = hashlib.sha256(binascii.unhexlify(fullkey)).hexdigest()
    sha256b = hashlib.sha256(binascii.unhexlify(sha256a)).hexdigest()
    address = base58.b58encode(binascii.unhexlify(fullkey + sha256b[:8]))
    return address


def get_token():
    # Creacion tokens de un solo uso
    return secrets.token_hex(20)


def get_balance():
    # Asignacion Balance
    balance = random.randint(1, 100000)
    return balance

class Messages:
    """
    This class define utils messages to show for an error.
    """
    INVALID_TRANSFER_VALUE = "EL VALOR A TRANSFERIR NO ES VALIDO"
    INVALID_TOKEN = "EL TOKEN INTRODUCIDO NO ES VALIDO"
    INVALID_WALLET = "LA WALLET DE DESTINO NO EXISTE"
    EXPIRED_TOKEN = "EL TOKEN ESPECIFICADO YA EXPIRÓ"
    SUCESS_TRANSACTION = "TRANSACCIÓN REALIZADA EXITOSAMENTE"
    TOKEN_NOT_BELONG_TRANSACCION = "El TOKEN ESPECIFICADO NO PERTENECE A ESTA TRANSACCIÓN"
    TOKEN_ALREADY_USED = "El TOKEN ESPECIFICADO YA HA SIDO USADO"
    VALUE_DISPOSED_FAIL = "EL USUARIO NO CUENTA CON EL VALOR SUFICIENTE PARA TRANSFERIR"
    SESION_EXPIRED = "LA SESIÓN EXPIRÓ"


class Constants:
    """
    This constants class is very important for the Token - Opt validation.
    """
    PIN = "PIN"
    AMMOUNT = "MONTO"
    WALLET = "CUENTA"

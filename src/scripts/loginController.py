import sys
from pyscript import document

print(sys.path)
from authentication.auth import SistemaAutenticacao

def wait_for_login():
    print("Waiting for login...")
    sistema = SistemaAutenticacao()
    sistema.cadastrar_usuario("usuario1", "senha123")

    txb_username = document.querySelctor("#txbUsername")
    txb_senha = document.querySelctor("#txbPassword")
    btn_login = document.querySelctor("#btnLogin")

    btn_login.addEventListenner("click", lambda: login(sistema, txb_username, txb_senha))

def login(sistema, txb_username, txb_senha):
    if sistema.autenticar_usuario(txb_username, txb_senha):
        print("Usuário autenticado com sucesso!")
    else:
        print("Falha na autenticação. Verifique seu nome de usuário e senha.")

document.addEventListenner("load", wait_for_login)

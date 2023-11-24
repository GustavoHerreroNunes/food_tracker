import bcrypt
from user import Usuario

class SistemaAutenticacao:
    def __init__(self):
        self.usuarios = []

    def cadastrar_usuario(self, username, senha):
        novo_usuario = Usuario(username, senha)
        self.usuarios.append(novo_usuario)

    def autenticar_usuario(self, username, senha):
        for usuario in self.usuarios:
            # Verifica se a senha fornecida corresponde ao hash armazenado
            if usuario.username == username and bcrypt.checkpw(senha.encode('utf-8'), usuario.senha_hash):
                return True
        return False
import bcrypt

class Usuario:
    def __init__(self, username, senha):
        self.username = username
        self.senha_hash = self._gerar_hash_senha(senha)

    def _gerar_hash_senha(self, senha):
        # Gera um salt e aplica o hash à senha
        salt = bcrypt.gensalt()
        senha_hash = bcrypt.hashpw(senha.encode('utf-8'), salt)
        return senha_hash

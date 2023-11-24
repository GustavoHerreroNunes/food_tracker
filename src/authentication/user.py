import bcrypt

class Usuario:
    def __init__(self, username, senha):
        self.username = username
        self.senha_hash = self._gerar_hash_senha(senha)
        self.left = None
        self.right = None

    def _gerar_hash_senha(self, senha):
        salt = bcrypt.gensalt()
        senha_hash = bcrypt.hashpw(senha.encode('utf-8'), salt)
        return senha_hash
    
class ArvoreUsuarios:
    def __init__(self):
        self.root = None

    def inserir_usuario(self, usuario):
        self.root = self._inserir(self.root, usuario)

    def _inserir(self, node, usuario):
        if node is None:
            return usuario
        if usuario.username < node.username:
            node.left = self._inserir(node.left, usuario)
        elif usuario.username > node.username:
            node.right = self._inserir(node.right, usuario)
        return node

    def buscar_usuario(self, username):
        return self._buscar(self.root, username)

    def _buscar(self, node, username):
        if node is None or node.username == username:
            return node
        if username < node.username:
            return self._buscar(node.left, username)
        return self._buscar(node.right, username)

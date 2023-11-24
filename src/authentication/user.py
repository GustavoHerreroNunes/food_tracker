import bcrypt

class Usuario:
    def __init__(self, username, senha):
        self.username = username
        self.senha_hash = self._gerar_hash_senha(senha)
        self.left = None
        self.right = None
        self.height = 1

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
        if not node:
            return usuario

        if usuario.username < node.username:
            node.left = self._inserir(node.left, usuario)
        elif usuario.username > node.username:
            node.right = self._inserir(node.right, usuario)
        else:
            return node 

        
        node.height = 1 + max(self._get_altura(node.left), self._get_altura(node.right))

       
        balanceamento = self._get_balanceamento(node)

        
        if balanceamento > 1:
            if usuario.username < node.left.username:
                return self._rotacao_direita(node)
            else:
                node.left = self._rotacao_esquerda(node.left)
                return self._rotacao_direita(node)
        if balanceamento < -1:
            if usuario.username > node.right.username:
                return self._rotacao_esquerda(node)
            else:
                node.right = self._rotacao_direita(node.right)
                return self._rotacao_esquerda(node)

        return node

    def buscar_usuario(self, username):
        return self._buscar(self.root, username)

    def _buscar(self, node, username):
        if not node or node.username == username:
            return node
        if username < node.username:
            return self._buscar(node.left, username)
        return self._buscar(node.right, username)

    def _get_altura(self, node):
        if not node:
            return 0
        return node.height

    def _get_balanceamento(self, node):
        if not node:
            return 0
        return self._get_altura(node.left) - self._get_altura(node.right)

    def _rotacao_direita(self, z):
        y = z.left
        T3 = y.right

        
        y.right = z
        z.left = T3

       
        z.height = 1 + max(self._get_altura(z.left), self._get_altura(z.right))
        y.height = 1 + max(self._get_altura(y.left), self._get_altura(y.right))

        return y

    def _rotacao_esquerda(self, y):
        x = y.right
        T2 = x.left

        
        x.left = y
        y.right = T2

        
        y.height = 1 + max(self._get_altura(y.left), self._get_altura(y.right))
        x.height = 1 + max(self._get_altura(x.left), self._get_altura(x.right))

        return x

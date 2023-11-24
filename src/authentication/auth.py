import bcrypt
import uuid
from user import Usuario, ArvoreUsuarios

class SistemaAutenticacao:
    def __init__(self):
        self.arvore_usuarios = ArvoreUsuarios()
        self.sessoes = {}

    def cadastrar_usuario(self, username, senha):
        novo_usuario = Usuario(username, senha)
        self.arvore_usuarios.inserir_usuario(novo_usuario)

    def autenticar_usuario(self, username, senha):
        usuario = self.arvore_usuarios.buscar_usuario(username)
        if usuario and bcrypt.checkpw(senha.encode('utf-8'), usuario.senha_hash):
            # Gerar um ID de sessão único
            id_sessao = str(uuid.uuid4())
            # Associar o ID de sessão ao usuário autenticado
            self.sessoes[id_sessao] = usuario
            return id_sessao
        return None

    def obter_usuario_por_sessao(self, id_sessao):
        return self.sessoes.get(id_sessao)

from auth import SistemaAutenticacao

# Exemplo de Uso
sistema = SistemaAutenticacao()
sistema.cadastrar_usuario("usuario1", "senha123")

# Autenticar usuário
username_input = input("Digite o nome de usuário: ")
senha_input = input("Digite a senha: ")

if sistema.autenticar_usuario(username_input, senha_input):
    print("Usuário autenticado com sucesso!")
else:
    print("Falha na autenticação. Verifique seu nome de usuário e senha.")

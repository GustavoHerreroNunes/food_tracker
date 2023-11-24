from auth import SistemaAutenticacao

if __name__ == "__main__":
    sistema = SistemaAutenticacao()

    while True:
        print("\n1 - Cadastrar usuário\n2 - login do usuário\n3 - Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            username = input("Digite o nome de usuário: ")
            senha = input("Digite a senha: ")
            sistema.cadastrar_usuario(username, senha)
            print("Usuário cadastrado com sucesso!")

        elif escolha == "2":
            username_input = input("Digite o nome de usuário: ")
            senha_input = input("Digite a senha: ")

            id_sessao = sistema.autenticar_usuario(username_input, senha_input)

            if id_sessao:
                print("Usuário autenticado com sucesso! ID de Sessão:", id_sessao)

                usuario_na_sessao = sistema.obter_usuario_por_sessao(id_sessao)
                print("Usuário na sessão:", usuario_na_sessao.username)
            else:
                print("Falha na autenticação. Verifique seu nome de usuário e senha.")

        elif escolha == "3":
            break

        else:
            print("Opção inválida. Tente novamente.")

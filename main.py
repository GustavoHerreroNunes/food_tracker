from datetime import datetime
import sys

sys.path.append('./src/authentication/')
from src.authentication.auth import SistemaAutenticacao
from src.alimentos import RegistroAlimentosConsumidos
from src.arvore import ler_arvore_txt

if __name__ == "__main__":
    sistema = SistemaAutenticacao()
    alimentos = ler_arvore_txt("src/TesteArvore.txt")
    registro = RegistroAlimentosConsumidos()

    while True:
        print("\n1 - Cadastrar usuário" + 
              "\n2 - login do usuário" + 
              "\n0 - Sair")
        escolha = input("\nEscolha uma opção: ")

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
                print("\nUsuário autenticado com sucesso! ID de Sessão:", id_sessao)

                usuario_na_sessao = sistema.obter_usuario_por_sessao(id_sessao)
                print("Usuário na sessão:", usuario_na_sessao.username)

                while True:
                    print("\n1 - Today's Foods" + 
                          "\n2 - All Foods" + 
                          "\n3 - Calendar" + 
                          "\n0 - Voltar")
                    escolha = input("\nEscolha uma opção: ")

                    if escolha == "1":
                        while True:
                            print("\n1 - Adicionar alimento" + 
                                "\n2 - Ver alimentos consumidos" +
                                "\n3 - Ver total de calorias consumidas hoje" +
                                "\n0 - Voltar")
                            escolha = input("\nEscolha uma opção: ")

                            if escolha == "1":
                                data = datetime.now().strftime("%d/%m/%Y")
                                alimento = input("\nDigite o nome do alimento: ")
                                quantidade = float(input("Digite a quantidade consumida (em gramas): "))
                                registro.adicionar_consumo(alimentos, data, alimento, quantidade)

                            elif escolha == "2":
                                data = datetime.now().strftime("%d/%m/%Y")
                                consumos = registro.listar_alimentos_consumidos(data)
                                if consumos:
                                    print(f"\nAlimentos consumidos em {data}:")
                                    for consumo in consumos:
                                        print(f"  {consumo['alimento']} - {consumo['quantidade_consumida']}g, {consumo['calorias_consumidas']}cal")
                                else:
                                    print(f"\nNenhum alimento consumido. Que tal adicionar novos alimentos?")
                            elif escolha == "3":
                                data = datetime.now().strftime("%d/%m/%Y")
                                total_calorias = registro.calcular_calorias_por_dia(data)
                                print(f"\nHoje você consumiu {total_calorias}cal.")
                            elif escolha == "0":
                                print("\nVoltando...")
                                break
                            else:
                                print("\nOpção inválida. Tente novamente.")
                    
                    elif escolha == "2":
                        while True:
                            print("\n1 - Ver todos os alimentos" +
                                "\n2 - Buscar um alimento" + 
                                "\n0 - Voltar")
                            escolha = input("\nEscolha uma opção: ")

                            if escolha == "1":
                                todos_alimentos = alimentos.listar_nos()
                                print("\nTodos os alimentos:")
                                for alimento in todos_alimentos:
                                    print(f"  {alimento['alimento']} - {alimento['calorias_por_grama']}cal/g")
                            elif escolha == "2":
                                nome_alimento = input("\nDigite o nome do alimento: ")
                                resultado_busca = alimentos.buscar(nome_alimento)
                                if resultado_busca:
                                    print(f"\nAlimento encontrado: {resultado_busca.alimento} - {resultado_busca.calorias_por_grama}cal/g")
                                else:
                                    print("\nAlimento não encontrado.")
                            elif escolha == "0":
                                print("\nVoltando...")
                                break
                            else:
                                print("\nOpção inválida. Tente novamente.")
                    elif escolha == "3":
                        while True:
                            print("\n1 - Ver total de calorias consumidas em todos os dias" +
                                "\n2 - Ver total de calorias consumidas por dia" + 
                                "\n0 - Voltar")
                            escolha = input("\nEscolha uma opção: ")

                            if escolha == "1":
                                calorias_todos_dias = registro.calcular_calorias_todos_dias()
                                print("\nTotal de calorias consumidas em todos os dias:")
                                for data, calorias in calorias_todos_dias.items():
                                    print(f"  {data} - {calorias}cal")
                            elif escolha == "2":
                                data = input("\nDigite a data (dd/mm/aaaa): ")
                                calorias_por_dia = registro.calcular_calorias_por_dia(data)
                                print(f"\n{data}: {calorias_por_dia}cal")
                            elif escolha == "0":
                                print("\nVoltando...")
                                break
                            else:
                                print("\nOpção inválida. Tente novamente.")
                    else:
                        print("\nVoltando...")
                        break
            else:
                print("\nUsuário ou senha inválidos. Tente novamente.")
        elif escolha == "0":
            print("\nSaindo do sistema")
            break
                    


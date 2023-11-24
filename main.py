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
            print("\33[32mUsuário cadastrado com sucesso!\33[0m")

        elif escolha == "2":
            username_input = input("Digite o nome de usuário: ")
            senha_input = input("Digite a senha: ")

            id_sessao = sistema.autenticar_usuario(username_input, senha_input)

            if id_sessao:
                print(f"\n\33[32mUsuário autenticado com sucesso! ID de Sessão:{id_sessao}\33[0m")

                usuario_na_sessao = sistema.obter_usuario_por_sessao(id_sessao)
                print(f"Usuário na sessão: \33[1m{usuario_na_sessao.username}\33[0m")

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
                                    print(f"\n\33[1mAlimentos consumidos em {data}:\33[0m")
                                    for consumo in consumos:
                                        print(f"  \33[32m{consumo['alimento']}\33[0m - {consumo['quantidade_consumida']}g, {consumo['calorias_consumidas']}cal")
                                else:
                                    print(f"\nNenhum alimento consumido. Que tal adicionar novos alimentos?")
                            elif escolha == "3":
                                data = datetime.now().strftime("%d/%m/%Y")
                                total_calorias = registro.calcular_calorias_por_dia(data)
                                print(f"\n\33[34mHoje você consumiu {total_calorias}cal.\33[0m")
                            elif escolha == "0":
                                print("\nVoltando...")
                                break
                            else:
                                print("\n\33[31Opção inválida. Tente novamente.\33[0m")
                    
                    elif escolha == "2":
                        while True:
                            print("\n1 - Ver todos os alimentos" +
                                "\n2 - Buscar um alimento" + 
                                "\n0 - Voltar")
                            escolha = input("\nEscolha uma opção: ")

                            if escolha == "1":
                                todos_alimentos = alimentos.listar_nos()
                                print("\n\33[1mTodos os alimentos:\33[0m")
                                for alimento in todos_alimentos:
                                    print(f"  \33[32m{alimento['alimento']}\33[0m - {alimento['calorias_por_grama']}cal/g")
                            elif escolha == "2":
                                nome_alimento = input("\nDigite o nome do alimento: ")
                                resultado_busca = alimentos.buscar(nome_alimento)
                                if resultado_busca:
                                    print(f"\n\33[34mAlimento encontrado: {resultado_busca.alimento} - {resultado_busca.calorias_por_grama}cal/g\33[0m")
                                else:
                                    print("\n\33[31mAlimento não encontrado.\33[0m")
                            elif escolha == "0":
                                print("\nVoltando...")
                                break
                            else:
                                print("\n\33[31Opção inválida. Tente novamente.\33[0m")
                    elif escolha == "3":
                        while True:
                            print("\n1 - Ver total de calorias consumidas em todos os dias" +
                                "\n2 - Ver total de calorias consumidas por dia" + 
                                "\n0 - Voltar")
                            escolha = input("\nEscolha uma opção: ")

                            if escolha == "1":
                                calorias_todos_dias = registro.calcular_calorias_todos_dias()
                                print("\n\33[1mTotal de calorias consumidas em todos os dias:\33[0m")
                                for data, calorias in calorias_todos_dias.items():
                                    print(f"  \33[32m{data}\33[0m - {calorias}cal")
                            elif escolha == "2":
                                data = input("\nDigite a data \33[1m(dd/mm/aaaa)\33[1m: ")
                                calorias_por_dia = registro.calcular_calorias_por_dia(data)
                                print(f"\n\33[32m{data}\33[0m: {calorias_por_dia}cal")
                            elif escolha == "0":
                                print("\nVoltando...")
                                break
                            else:
                                print("\n\33[31mOpção inválida. Tente novamente.\33[0m")
                    elif escolha == "0":
                        print("\nVoltando...")
                        break
                    else:
                        print("\n\33[31mOpção inválida. Tente novamente.\33[0m")
            else:
                print("\n\33[31mUsuário ou senha inválidos. Tente novamente.\33[0m")
        elif escolha == "0":
            print("\nSaindo do sistema")
            break
        else:
            print("\n\33[31mOpção inválida. Tente novamente.\33[0m")
                    


# YouKcal - Global Solution

<!--Tecnologias Utilizadas e suas versões-->

[![Python Version][python-badge]][java-doc] 


> Status: :thumbsup: Finished

## Indíce :bookmark_tabs:

:cd: [Descrição](#descrição-clipboard) 

:cd: [Funcionalidades](#funcionalidades-gear)    

:cd: [Instalação](#instalação-floppy_disk)

:cd: [Contribuir](#contribuir-gift) 

## Descrição :clipboard:

<p style="text-align:justify">
YouKcal é um sistema de gestão de calorias diárias. Ele visa ser uma ferramenta de Home Personal Care, ajudando os usuários a gerenciar sua nutrição e saúde. O sistema foi desenvolvido com enfâse em eficiência e velocidade de processamento, além de contar com um sistema de autenticação de usuários.
</p>

## Funcionalidades :gear:

### Autenticação de Usuários
> **Descrição:** Um usuário cadastrado fornece suas credências de acesso, e recebe um identificador de acesso na sessão. <br> 
A senha de todos os usuários é passa por um processo de hash e salting, para garantir a segurança dos dados.
- **Classes responsáveis:**
    - ```SistemaAutenticacao```: Classe responsável por autenticar usuários no sistema.
        - **Métodos:**
            - ```cadastrar_usuario```: Recebe um username e uma senha, cria um novo usuário e o insere na árvore de usuários.
                - Observação: A senha é armazenada como um hash, utilizando a função ```bcrypt.hashpw```.
            - ```autenticar_usuario```: Recebe um username e uma senha, verifica se o usuário existe e se a senha está correta.
                - Observação: A senha é verificada utilizando a função ```bcrypt.checkpw```.
            - ```obter_usuario_por_sessao```: Recebe um ID de sessão e retorna o usuário associado a ele.
    - ```Usuario```: Classe responsável por armazenar os dados de um usuário.
        - **Atributos:**
            - ```username```: Nome de usuário (```string```)
            - ```senha_hash```: Hash da senha do usuário (```string```)
        - **Métodos:**
            - ```_gerar_hash_senha```: Recebe uma senha e retorna o hash correspondente.
                - Observação: A senha é armazenada como um hash, utilizando a função ```bcrypt.hashpw```.
    - ```ArvoreUsuarios```: Classe responsável por armazenar os usuários em uma árvore binária de busca.
        - **Atributos:**
            - ```root```: Raiz da árvore (```Usuario```)
        - **Métodos:**
            - ```inserir_usuario```: Recebe um usuário e o insere na árvore.
            - ```buscar_usuario```: Recebe um username e retorna o usuário correspondente.
            - ```numero_de_usuarios```: Retorna o número de usuários na árvore.
        - **Observação:** Métodos internos para balanceamento da árvore e inserção de nós não inclusos.
- **Bibliotecas Externas:**
    - ```bcrypt```
    - ```uuid```

### Registro de Alimentos
> **Descrição:** Existe uma lista pré-definida de alimentos, com seus respectivos valores nutricionais. O usuário pode buscar e listar todos os alimentos cadastrados.

- **Classes Responsáveis:**

    - ```NoArvore```: Classe responsável por representar um nó da árvore binária de busca.

    - ```ArvoreBinaria```: Classe responsável por representar uma árvore binária de busca com todos os alimentos cadastrados.
        - **Métodos:**
            - ```adicionar```: Recebe um alimento e a quantidade de calorias por grama e insere um novo nó na árvore.
            - ```buscar```: Recebe um alimento e retorna o nó correspondente.
            - ```imprimir_arvore```: Imprime todos os nós da árvore.
            - ```listar_nos```: Retorna uma lista com todos os nós da árvore.
            - ```buscar_calorias_por_grama```: Recebe um alimento e retorna a quantidade de calorias por grama.
            - ```calcular_calorias_por_dia```: Recebe um dicionário com os alimentos consumidos e retorna um dicionário com a quantidade de calorias por dia.
- **Funções Auxiliares:**
    - ```salvar_arvore```: Recebe o nome de um arquivo ```.txt``` e salva a árvore nele.
    - ```ler_arvore_txt```: Recebe o nome de um arquivo e retorna uma árvore com os dados do arquivo.

### Registro de Consumo
> **Descrição:** O usuário pode registrar os alimentos que consumiu em um determinado dia, e o sistema calcula a quantidade de calorias consumidas.

- **Classes Responsáveis:**
    - ```RegistroAlimentosConsumidos```: Classe responsável por registrar os alimentos consumidos pelos usuários.
    - **Métodos:**
        - ```adicionar_consumo```: Recebe uma data, um alimento e uma quantidade e registra o consumo naquela data.
        - ```listar_alimentos_consumidos```: Recebe uma data e retorna uma lista com os alimentos consumidos naquela data.
        - ```listar_todos_alimentos_consumidos```: Retorna um dicionário com todos os alimentos consumidos.
        - ```calcular_calorias_por_dia```: Recebe uma data e retorna a quantidade total de calorias consumidas naquela data.
        - ```calcular_calorias_todos_dias```: Retorna um dicionário com a quantidade total de calorias consumidas em cada data.


## Instalação :floppy_disk:

<!--Indique o passo a passo para se instalar o projeto, como também os pré-requisitos para isso-->

### Pré-requisitos

- [Python][java-download]
- [Uuid][java-download]
- [Bcrypt][java-download]

### Iniciando o projeto 
> Os comandos listados a seguir foram feitos pelo terminal do **Windows**

1. **Clone** o projeto no seu computador:

```
git clone https://github.com/GustavoHerreroNunes/food_tracker.git
```

2. Acesse a pasta raiz do projeto pelo terminal e **instale todas as bibliotecas necessárias:**

```bash
pip install uuid
pip install bcrypt
```

3. Ainda na pasta raiz do projeto, execute o arquivo ```main.py```:

```bash
py main.py
```

4. O sistema irá iniciar e realizar a criação automática de **1000 usuários de teste**. Essa operação leva tempo então para desativar essa funcionalidade, basta comentar as linhas 14-18 do arquivo ```main.py```:

```python
for i in range(1000):
        print(i)
        username = f"usuario{i}"
        senha = "senha123"
        sistema.cadastrar_usuario(username, senha)
```

5. Após a criação dos usuários, estará pronto para uso. Toda a sua navegação é feita por **menus indexados**, basta seguir as instruções na tela. Exemplo:

```
1 - Cadastrar usuário 
2 - login do usuário
0 - Sair

Escolha uma das opções:
```

## Contribuir :gift:

Se você tem alguma ideia, sugestão, ou viu algum erro, você pode [abrir uma issue][issues] e contar para gente.

<!-- Links utilizados no documento -->

<!-- Badges -->
[python-badge]: https://img.shields.io/badge/Python-3.11.4-blue?style=for-the-badge&logo=python

<!-- Documentations -->
[java-doc]: https://docs.oracle.com/en/java/javase/17/

<!-- Downloads -->
[java-download]: https://www.java.com/pt-BR/download/ie_manual.jsp?locale=pt_BR


<!-- Others -->
[issues]: https://github.com/GustavoHerreroNunes/fodd_tracker/issues
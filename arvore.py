#Definição da classe Arvore Binaria com os alimentos

class NoArvore:
    def __init__(self, alimento, calorias_por_grama):
        self.alimento = alimento
        self.calorias_por_grama = calorias_por_grama
        self.esquerda = None
        self.direita = None
        self.altura = 1

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def adicionar(self, alimento, calorias_por_grama):
        if self.raiz is None:
            self.raiz = NoArvore(alimento, calorias_por_grama)
        else:
            self.raiz = self._adicionar_recursivamente(self.raiz, alimento, calorias_por_grama)

    def _altura(self, no):
        if no is None:
            return 0
        return no.altura

    def _fator_balanceamento(self, no):
        if no is None:
            return 0
        return self._altura(no.esquerda) - self._altura(no.direita)

    def _rotacao_direita(self, y):
        x = y.esquerda
        z = x.direita

        x.direita = y
        y.esquerda = z

        y.altura = 1 + max(self._altura(y.esquerda), self._altura(y.direita))
        x.altura = 1 + max(self._altura(x.esquerda), self._altura(x.direita))

        return x

    def _rotacao_esquerda(self, x):
        y = x.direita
        z = y.esquerda

        y.esquerda = x
        x.direita = z

        x.altura = 1 + max(self._altura(x.esquerda), self._altura(x.direita))
        y.altura = 1 + max(self._altura(y.esquerda), self._altura(y.direita))

        return y

    def adicionar(self, alimento, calorias_por_grama):
        if self.raiz is None:
            self.raiz = NoArvore(alimento, calorias_por_grama)
        else:
            self.raiz = self._adicionar_recursivamente(self.raiz, alimento, calorias_por_grama)

    def _adicionar_recursivamente(self, no_atual, alimento, calorias_por_grama):
        if no_atual is None:
            return NoArvore(alimento, calorias_por_grama)

        if alimento < no_atual.alimento:
            no_atual.esquerda = self._adicionar_recursivamente(no_atual.esquerda, alimento, calorias_por_grama)
        elif alimento > no_atual.alimento:
            no_atual.direita = self._adicionar_recursivamente(no_atual.direita, alimento, calorias_por_grama)
        else:
            print(f'O alimento "{alimento}" já existe na árvore.')
            return no_atual

        no_atual.altura = 1 + max(self._altura(no_atual.esquerda), self._altura(no_atual.direita))

        fator = self._fator_balanceamento(no_atual)

        if fator > 1 and alimento < no_atual.esquerda.alimento:
            return self._rotacao_direita(no_atual)

        if fator < -1 and alimento > no_atual.direita.alimento:
            return self._rotacao_esquerda(no_atual)

        if fator > 1 and alimento > no_atual.esquerda.alimento:
            no_atual.esquerda = self._rotacao_esquerda(no_atual.esquerda)
            return self._rotacao_direita(no_atual)

        if fator < -1 and alimento < no_atual.direita.alimento:
            no_atual.direita = self._rotacao_direita(no_atual.direita)
            return self._rotacao_esquerda(no_atual)

        return no_atual
    
    def buscar(self, alimento):
        return self._buscar_recursivamente(alimento, self.raiz)

    def _buscar_recursivamente(self, alimento, no_atual):
        if no_atual is None or no_atual.alimento == alimento:
            return no_atual
        if alimento < no_atual.alimento:
            return self._buscar_recursivamente(alimento, no_atual.esquerda)
        return self._buscar_recursivamente(alimento, no_atual.direita)
    
    def imprimir_arvore(self):
        self._imprimir_recursivamente(self.raiz, 0)

    def _imprimir_recursivamente(self, no_atual, nivel):
        if no_atual is not None:
            self._imprimir_recursivamente(no_atual.esquerda, nivel + 1)
            print("   " * nivel, end="")
            print(f"{no_atual.alimento} ({no_atual.calorias_por_grama})")
            self._imprimir_recursivamente(no_atual.direita, nivel + 1)

    def listar_nos(self):
        todos_nos = []
        self._listar_nos_recursivamente(self.raiz, todos_nos)
        return todos_nos

    def _listar_nos_recursivamente(self, no_atual, todos_nos):
        if no_atual is not None:
            self._listar_nos_recursivamente(no_atual.esquerda, todos_nos)
            todos_nos.append({'alimento': no_atual.alimento, 'calorias_por_grama': no_atual.calorias_por_grama})
            self._listar_nos_recursivamente(no_atual.direita, todos_nos)

    def buscar_calorias_por_grama(self, alimento):
        no = self.buscar(alimento)
        if no:
            return no.calorias_por_grama
        else:
            return None

    def buscar_alimento(no_atual, alimento):
    if no_atual is None or no_atual.alimento == alimento:
        return no_atual
    if alimento < no_atual.alimento:
        return buscar_alimento(no_atual.esquerda, alimento)
    return buscar_alimento(no_atual.direita, alimento)

    def salvar_arvore_txt(no_atual, arquivo):
    if no_atual is not None:
        if no_atual.direita is not None:
            salvar_arvore_txt(no_atual.direita, arquivo)
        arquivo.write(f"{no_atual.alimento},{no_atual.calorias_por_grama}\n")
        if no_atual.esquerda is not None:
            salvar_arvore_txt(no_atual.esquerda, arquivo)

    def salvar_arvore(nome_arquivo, arvore):
        with open(nome_arquivo, 'w') as arquivo_txt:
            if arvore.raiz is not None:
                salvar_arvore_txt(arvore.raiz, arquivo_txt)

    def ler_arvore_txt(nome_arquivo):
    arvore = ArvoreBinaria()
    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            dados = linha.strip().split(',')
            alimento = dados[0]
            calorias_por_grama = float(dados[1])
            arvore.raiz = adicionar_no(arvore.raiz, alimento, calorias_por_grama)
    return arvore

    def adicionar_no(raiz, alimento, calorias_por_grama):
        if raiz is None:
            return NoArvore(alimento, calorias_por_grama)
        elif alimento < raiz.alimento:
            raiz.esquerda = adicionar_no(raiz.esquerda, alimento, calorias_por_grama)
        elif alimento > raiz.alimento:
            raiz.direita = adicionar_no(raiz.direita, alimento, calorias_por_grama)
        return raiz

    def adicionar_alimento_consumido(arvore, data_consumo, alimento, quantidade_consumida):
    resultado_busca = buscar_alimento(arvore.raiz, alimento)
    
    if resultado_busca:
        # Aqui você pode fazer o cálculo das calorias com base na quantidade consumida
        calorias_consumidas = resultado_busca.calorias_por_grama * quantidade_consumida
        
        if data_consumo not in alimentos_consumidos:
            alimentos_consumidos[data_consumo] = []

        alimentos_consumidos[data_consumo].append({
            'alimento': alimento,
            'quantidade_consumida': quantidade_consumida,
            'calorias_consumidas': calorias_consumidas
        })
        print(f"Alimento '{alimento}' adicionado na data {data_consumo}.")
        return calorias_consumidas
    else:
        print(f"Alimento '{alimento}' não encontrado na lista de alimentos.")
        return 0

    def calcular_calorias_por_dia(alimentos_consumidos):
        calorias_por_dia = defaultdict(int)

        for data, consumos in alimentos_consumidos.items():
            for consumo in consumos:
                calorias_por_dia[data] += consumo['calorias_consumidas']

        return calorias_por_dia



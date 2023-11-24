from collections import defaultdict

class RegistroAlimentosConsumidos:
    def __init__(self):
        self.registro = defaultdict(list)

    def adicionar_consumo(self, arvore, data, alimento, quantidade):
        resultado_busca = arvore.buscar_calorias_por_grama(alimento)
        
        if resultado_busca is not None:
            calorias_consumidas = resultado_busca * quantidade
            
            self.registro[data].append({
                'alimento': alimento,
                'quantidade_consumida': quantidade,
                'calorias_consumidas': calorias_consumidas
            })
            print(f"Alimento '{alimento}' adicionado na data {data}.")
        else:
            print(f"Alimento '{alimento}' não encontrado na lista de alimentos.")

    """
    def listar_alimentos_consumidos(self, data):
        alimentos = self.registro.get(data, [])
        if alimentos:
            print(f"Alimentos consumidos em {data}:")
            for consumo in alimentos:
                print(f"  Alimento: {consumo['alimento']}, Quantidade: {consumo['quantidade_consumida']}, Calorias: {consumo['calorias_consumidas']}")
        else:
            print(f"Nenhum alimento consumido em {data}.")

    def listar_todos_alimentos_consumidos(self):
        if self.registro:
            print("Todos os alimentos consumidos:")
            for data, alimentos in self.registro.items():
                print(f"  Data: {data}")
                for consumo in alimentos:
                    print(f"    Alimento: {consumo['alimento']}, Quantidade: {consumo['quantidade_consumida']}, Calorias: {consumo['calorias_consumidas']}")
        else:
            print("Nenhum alimento consumido.")

    """
    
    def listar_alimentos_consumidos(self, data):
        if data in self.registro:
            return self.registro[data]
        else:
            return []
        

    def listar_todos_alimentos_consumidos(self):
        return self.registro

    def calcular_calorias_todos_dias(self):
        calorias_todos_dias = defaultdict(int)

        for data, consumos in self.registro.items():
            for consumo in consumos:
                calorias_todos_dias[data] += consumo['calorias_consumidas']

        return calorias_todos_dias
    
    def calcular_calorias_por_dia(self, data):
        calorias_por_dia = 0

        for consumo_data, consumos in self.registro.items():
            if consumo_data == data:
                for consumo in consumos:
                    calorias_por_dia += consumo['calorias_consumidas']
                break

        return calorias_por_dia

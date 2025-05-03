class CarrinhoCompras:
    def __init__(self, *produtos):
        self.produtos = produtos

    def listar_produtos(self):
        for e, p in enumerate(self.produtos):
            print(f'{e+1}° produto: {p}')

c = CarrinhoCompras('Feijão', 'Arroz')
c.listar_produtos()
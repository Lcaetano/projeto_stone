class Produto:
    def __init__(self, nome_item, quatidade, preco):
        self.nome_item = nome_item
        self.quatidade = quatidade
        self.preco = preco

    def valor_produto(self):
        return self.quatidade*self.preco

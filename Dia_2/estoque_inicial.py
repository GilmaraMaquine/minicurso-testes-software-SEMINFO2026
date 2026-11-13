"""DESAFIO: versão propositalmente incompleta com defeitos para investigação."""
class Estoque:
    def __init__(self):
        self.produtos = {}

    def cadastrar_produto(self, nome, quantidade, preco):
        # Falta validar nome, duplicidade, quantidade e preço.
        self.produtos[nome] = {"quantidade": quantidade, "preco": preco}

    def movimentar(self, nome, variacao):
        # Permite que o estoque fique negativo.
        self.produtos[nome]["quantidade"] += variacao

    def total_estoque(self):
        return sum(item["quantidade"] * item["preco"] for item in self.produtos.values())

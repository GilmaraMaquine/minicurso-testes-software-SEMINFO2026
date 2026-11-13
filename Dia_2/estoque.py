"""Solução de referência do estoque da Dona Clara.

A API utiliza preços inteiros em centavos para evitar problemas de float:
  cadastrar_produto(nome, quantidade, preco_centavos)
  entrada(nome, quantidade) | saida(nome, quantidade)
  valor_produto_centavos(nome) | total_estoque_centavos()
"""
class Estoque:
    def __init__(self):
        self.produtos = {}  # nome -> {quantidade: int, preco_centavos: int}

    @staticmethod
    def _quantidade_valida(valor, permite_zero=True):
        return type(valor) is int and (valor >= 0 if permite_zero else valor > 0)

    def cadastrar_produto(self, nome, quantidade, preco_centavos):
        """RF01–RF04: cadastra sem duplicação ou valores negativos."""
        if not isinstance(nome, str) or not nome.strip():
            raise ValueError("Nome não pode ser vazio")
        if nome in self.produtos:
            raise ValueError("Produto já cadastrado")
        if not self._quantidade_valida(quantidade):
            raise ValueError("Quantidade inválida")
        if not self._quantidade_valida(preco_centavos):
            raise ValueError("Preço inválido")
        self.produtos[nome] = {"quantidade": quantidade, "preco_centavos": preco_centavos}

    def entrada(self, nome, quantidade):
        """RF05: acrescenta unidades de um produto existente."""
        self._validar_movimento(nome, quantidade)
        self.produtos[nome]["quantidade"] += quantidade

    def saida(self, nome, quantidade):
        """RF05–RF06: retira unidades apenas quando existe saldo."""
        self._validar_movimento(nome, quantidade)
        if quantidade > self.produtos[nome]["quantidade"]:
            raise ValueError("Estoque insuficiente")
        self.produtos[nome]["quantidade"] -= quantidade

    def _validar_movimento(self, nome, quantidade):
        if nome not in self.produtos:
            raise KeyError(nome)
        if not self._quantidade_valida(quantidade, permite_zero=False):
            raise ValueError("Movimentação exige quantidade inteira positiva")

    def valor_produto_centavos(self, nome):
        """RF07: valor total de um único produto."""
        if nome not in self.produtos:
            raise KeyError(nome)
        p = self.produtos[nome]
        return p["quantidade"] * p["preco_centavos"]

    def total_estoque_centavos(self):
        """RF08: soma valores de todos os produtos."""
        return sum(self.valor_produto_centavos(nome) for nome in self.produtos)

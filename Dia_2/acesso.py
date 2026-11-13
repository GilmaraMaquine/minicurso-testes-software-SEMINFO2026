"""Programa de exemplo: a função é correta para as regras explícitas."""
def verificar_acesso(idade):
    """Permite acesso a partir de 18 anos; aceita idade inteira não negativa."""
    if type(idade) is not int:
        raise TypeError("Idade precisa ser inteira")
    if idade < 0:
        raise ValueError("Idade negativa")
    return idade >= 18

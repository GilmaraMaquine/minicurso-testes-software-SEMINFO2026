"""Experimento 1: exemplo de classificação por idade (Dia 2)."""

def classificar_idade(idade):
    """Classifica idades inteiras não negativas; lança erro para valores inválidos."""
    # type(...): evita aceitar booleanos como se fossem inteiros.
    if type(idade) is not int:
        raise TypeError("Idade precisa ser um número inteiro")
    if idade < 0:
        raise ValueError("Idade não pode ser negativa")
    if idade <= 11:
        return "Infantil"
    if idade <= 17:
        return "Adolescente"
    if idade <= 59:
        return "Adulto"
    return "Idoso"

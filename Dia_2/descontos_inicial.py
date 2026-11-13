"""VERSÃO COM DEFEITOS INTENCIONAIS — NÃO É SOLUÇÃO DE REFERÊNCIA."""
def calcular_total(valor):
    # Regras: menos de 100 = sem desconto; de 100 a <500 = 5%; >= 500 = 10%.
    # Defeitos a investigar: inclusões de faixas e entrada negativa.
    if valor <= 100:
        return valor
    elif valor <= 500:
        return valor * 0.95
    return valor * 0.90

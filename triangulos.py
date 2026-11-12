"""Solução de referência do problema do Sr. João

Critério: qualquer lado não positivo ou desigualdade triangular não satisfeita
gera a classificação 'Inválido'. Os demais casos são classificados por igualdade.
"""

def classificar_triangulo(a, b, c):
    
    # O comprimento zero ou negativo invalida a figura.
    if any(lado <= 0 for lado in (a, b, c)):
        return "Inválido"
    # Em um triângulo genuíno, a soma de dois lados excede o terceiro.
    # A igualdade (ex.: 1, 2, 3) não é suficiente: é um caso de fronteira.
    if a + b <= c or a + c <= b or b + c <= a:
        return "Inválido"
    # Somente depois de validar a existência, identificamos o tipo.
    if a == b == c:
        return "Equilátero"
    if a == b or a == c or b == c:
        return "Isósceles"
    return "Escaleno"

from triangulos import classificar_triangulo

def test_isosceles():
    # Dois lados iguais e um diferente.
    assert classificar_triangulo(3, 3, 4) == "Isósceles"

def test_escaleno():
    # Três lados diferentes que satisfazem a desigualdade triangular.
    assert classificar_triangulo(3, 4, 5) == "Escaleno"

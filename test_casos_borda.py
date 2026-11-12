from triangulos import classificar_triangulo

def test_triangulo_degenerado():
    # 1 + 2 == 3: igualdade não forma triângulo.
    assert classificar_triangulo(1, 2, 3) == "Inválido"

def test_lado_zero():
    # Lados devem ser estritamente positivos.
    assert classificar_triangulo(0, 2, 2) == "Inválido"

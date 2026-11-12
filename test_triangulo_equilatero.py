from triangulos import classificar_triangulo

def test_equilatero():
    # Entrada normal: três lados iguais e positivos.
    assert classificar_triangulo(3, 3, 3) == "Equilátero"

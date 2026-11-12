import pytest
from triangulos import classificar_triangulo

@pytest.mark.parametrize("lados, esperado", [
    ((3, 3, 3), "Equilátero"),
    ((3, 3, 4), "Isósceles"),
    ((3, 4, 3), "Isósceles"),
    ((4, 3, 3), "Isósceles"),
    ((3, 4, 5), "Escaleno"),
    ((1, 2, 3), "Inválido"),  # limite da desigualdade
    ((2, 2, 4), "Inválido"),
    ((0, 2, 2), "Inválido"),
    ((-1, 3, 3), "Inválido"),
])
def test_classificar_triangulo(lados, esperado):
    assert classificar_triangulo(*lados) == esperado

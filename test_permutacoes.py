import pytest
from triangulos import classificar_triangulo

@pytest.mark.parametrize("lados", [(3, 3, 4), (3, 4, 3), (4, 3, 3)])
def test_isosceles_em_qualquer_ordem(lados):
    # Uma permutação não deve modificar a classificação.
    assert classificar_triangulo(*lados) == "Isósceles"

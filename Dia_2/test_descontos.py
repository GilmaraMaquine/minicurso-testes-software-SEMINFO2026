"""Testes do total com desconto, incluindo fronteiras."""
from decimal import Decimal
import pytest
from descontos import calcular_total

@pytest.mark.parametrize("entrada,esperado", [
    ("0","0"),("99.99","99.99"),("100.00","95.0000"),
    ("499.99","474.9905"),("500.00","450.0000"),
    ("750.00","675.0000"),
])
def test_faixas(entrada,esperado):
    assert calcular_total(entrada) == Decimal(esperado)

@pytest.mark.parametrize("entrada", ["-1", "NaN", "Infinity", "10.123"])
def test_valor_invalido(entrada):
    with pytest.raises(ValueError):
        calcular_total(entrada)

def test_texto_nao_numerico():
    with pytest.raises(TypeError):
        calcular_total("abc")

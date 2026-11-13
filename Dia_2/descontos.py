"""Solução de referência do experimento de descontos.

Entradas em reais com até 2 casas decimais. O retorno é Decimal, exato em centavos.
"""
from decimal import Decimal, InvalidOperation

def calcular_total(valor):
    """Calcula valor final da compra com desconto, retornando Decimal."""
    if isinstance(valor, bool):
        raise TypeError("Valor não pode ser booleano")
    try:
        valor = Decimal(str(valor))
    except (InvalidOperation, ValueError, TypeError):
        raise TypeError("Valor numérico inválido") from None
    if not valor.is_finite() or valor < 0:
        raise ValueError("Valor deve ser finito e não negativo")
    if valor.as_tuple().exponent < -2:
        raise ValueError("Use no máximo duas casas decimais")
    if valor < 100:
        return valor
    if valor < 500:
        return valor * Decimal("0.95")
    return valor * Decimal("0.90")

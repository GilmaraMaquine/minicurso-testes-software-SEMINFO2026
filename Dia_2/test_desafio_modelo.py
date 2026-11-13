"""Modelo para os estudantes expandirem no desafio final."""
from pathlib import Path
import sys
# Torna explícita a localização do módulo do laboratório ao executar pela raiz.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "04_estoque_dona_clara"))
from estoque import Estoque

def test_saldo_zero_permitido_no_cadastro():
    # Exemplo de teste adicional: zero no cadastro é válido.
    estoque = Estoque()
    estoque.cadastrar_produto("Caneta", 0, 250)
    assert estoque.produtos["Caneta"]["quantidade"] == 0

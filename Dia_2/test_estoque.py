"""Cobertura dos 8 requisitos funcionais do estoque."""
import pytest
from estoque import Estoque

@pytest.fixture
def estoque():
    """Cada teste recebe um estoque vazio, sem interferir nos demais."""
    return Estoque()

def test_rf01_cadastro(estoque):
    estoque.cadastrar_produto("Arroz", 10, 550)
    assert estoque.produtos["Arroz"] == {"quantidade":10,"preco_centavos":550}

def test_rf02_duplicidade(estoque):
    estoque.cadastrar_produto("Arroz", 10, 550)
    with pytest.raises(ValueError):
        estoque.cadastrar_produto("Arroz", 5, 600)

@pytest.mark.parametrize("quantidade", [-1, 1.5, True, "10"])
def test_rf03_quantidade_invalida(estoque,quantidade):
    with pytest.raises(ValueError):
        estoque.cadastrar_produto("Arroz", quantidade, 550)

@pytest.mark.parametrize("preco", [-1, 3.5, True, "550"])
def test_rf04_preco_invalido(estoque,preco):
    with pytest.raises(ValueError):
        estoque.cadastrar_produto("Arroz", 10, preco)

def test_rf05_entradas_e_saidas(estoque):
    estoque.cadastrar_produto("Arroz", 10, 550)
    estoque.entrada("Arroz", 5)
    estoque.saida("Arroz", 3)
    assert estoque.produtos["Arroz"]["quantidade"] == 12

def test_rf06_estoque_insuficiente_nao_altera_saldo(estoque):
    estoque.cadastrar_produto("Arroz", 10, 550)
    with pytest.raises(ValueError):
        estoque.saida("Arroz", 11)
    assert estoque.produtos["Arroz"]["quantidade"] == 10

def test_rf07_valor_unitario_total(estoque):
    estoque.cadastrar_produto("Arroz", 10, 550)
    assert estoque.valor_produto_centavos("Arroz") == 5500

def test_rf08_valor_geral(estoque):
    estoque.cadastrar_produto("Arroz", 10, 550)
    estoque.cadastrar_produto("Feijao", 2, 900)
    assert estoque.total_estoque_centavos() == 7300

@pytest.mark.parametrize("metodo", ["entrada", "saida"])
def test_movimentacao_zero_rejeitada(estoque,metodo):
    estoque.cadastrar_produto("Arroz", 10, 550)
    with pytest.raises(ValueError):
        getattr(estoque, metodo)("Arroz", 0)

def test_nome_vazio_rejeitado(estoque):
    with pytest.raises(ValueError):
        estoque.cadastrar_produto("  ", 1, 100)

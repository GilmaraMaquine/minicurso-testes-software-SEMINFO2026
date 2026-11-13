"""Solução da auditoria: expectativas fundamentadas nas regras."""
import pytest
from acesso import verificar_acesso

@pytest.mark.parametrize("idade,esperado",[(0,False),(15,False),(17,False),(18,True),(20,True)])
def test_acesso(idade,esperado):
    assert verificar_acesso(idade) is esperado

@pytest.mark.parametrize("idade,erro",[(-1,ValueError),(18.0,TypeError),("18",TypeError)])
def test_entradas_invalidas(idade,erro):
    with pytest.raises(erro):
        verificar_acesso(idade)

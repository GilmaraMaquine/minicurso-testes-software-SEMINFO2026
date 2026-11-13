"""EXERCÍCIO DE AUDITORIA: testes intencionalmente incorretos.

Não execute este arquivo na suíte principal como se fosse a solução.
A missão é identificar e justificar as assertivas erradas.
"""
from acesso import verificar_acesso

def caso_adulto():
    assert verificar_acesso(20) is True  # Correto

def caso_menor():
    assert verificar_acesso(15) is True  # INCORRETO: 15 não permite acesso

def caso_limite():
    assert verificar_acesso(18) is False # INCORRETO: 18 permite acesso

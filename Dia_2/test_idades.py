"""Testes parametrizados: classes de equivalência e valores-limite."""
import pytest
from idades import classificar_idade

@pytest.mark.parametrize("idade,categoria", [
    (0,"Infantil"),(11,"Infantil"),(12,"Adolescente"),
    (17,"Adolescente"),(18,"Adulto"),(59,"Adulto"),
    (60,"Idoso"),(95,"Idoso"),
])
def test_categorias_e_limites(idade,categoria):
    assert classificar_idade(idade) == categoria

@pytest.mark.parametrize("idade,erro", [
    (-1,ValueError),(12.5,TypeError),("18",TypeError),(True,TypeError)
])
def test_entradas_invalidas(idade,erro):
    with pytest.raises(erro):
        classificar_idade(idade)

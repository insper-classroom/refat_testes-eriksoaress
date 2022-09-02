import pytest
from classes.Produto import Produto

@pytest.mark.com_internet
@pytest.mark.produto
def test_busca_nome_produto_maiuscula():
    produto_teste = Produto(1, 'Tomate')
    busca = 'TOM'
    assert Produto.busca_nome(busca)[0].nome == 'Tomate'

@pytest.mark.com_internet
@pytest.mark.produto
def test_busca_nome_produto_minuscula():
    produto_teste = Produto(1, 'Tomate')
    busca = 'tom'
    assert Produto.busca_nome(busca)[0].nome == 'Tomate'
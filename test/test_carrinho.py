import pytest
from classes.Carrinho import Carrinho
from classes.Produto import Produto

@pytest.mark.com_internet
@pytest.mark.carrinho
def test_adiciona_produto_no_carrinho():
    carrinho_teste = Carrinho()
    produto_teste = Produto(1, 'Tomate')
    carrinho_teste.adicionar_item(produto_teste, 2)
    assert carrinho_teste.itens[1] == {'Tomate': '2'}

@pytest.mark.com_internet
@pytest.mark.carrinho
def test_adiciona_produto_no_carrinho():
    carrinho_teste = Carrinho()
    produto_teste = Produto(1, 'Tomate')
    carrinho_teste.adicionar_item(produto_teste, 2)
    carrinho_teste.remover_item(id=1)
    assert carrinho_teste.itens == {}
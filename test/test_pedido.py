import pytest
from classes.Carrinho import Carrinho
from classes.Endereco import Endereco
from classes.Pedido import Pedido
from classes.PessoaFisica import PessoaFisica
from classes.Produto import Produto

@pytest.mark.com_internet
@pytest.mark.pedido
def test_cria_pedido_certo():
    endereco = Endereco('18604694', 200)
    pessoa = PessoaFisica(49340635899, 'erikbtu2017@gmail.com', 'Erik')
    pessoa.adicionar_endereco('Casa', endereco)
    produto = Produto(1, 'Melancia')
    carrinho = Carrinho()
    carrinho.adicionar_item(produto, 2)
    pedido = Pedido(pessoa, carrinho)
    assert str(pedido) == "Erik - ['Casa']: {1: {'Melancia': '2'}}"

@pytest.mark.com_internet
@pytest.mark.pedido
def test_cria_pedido_sem_carrinho():
    with pytest.raises(TypeError) as excinfo:
        endereco = Endereco('18604694', 200)
        pessoa = PessoaFisica(49340635899, 'erikbtu2017@gmail.com', 'Erik')
        pessoa.adicionar_endereco('Casa', endereco)
        produto = Produto(1, 'Melancia')
        carrinho = Carrinho()
        carrinho.adicionar_item(produto, 2)
        pedido = Pedido(pessoa)
    assert "missing 1 required positional argument: 'carrinho'" in str(excinfo.value)

@pytest.mark.com_internet
@pytest.mark.pedido
def test_cria_pedido_sem_pessoa():
    with pytest.raises(TypeError) as excinfo:
        endereco = Endereco('18604694', 200)
        pessoa = PessoaFisica(49340635899, 'erikbtu2017@gmail.com', 'Erik')
        pessoa.adicionar_endereco('Casa', endereco)
        produto = Produto(1, 'Melancia')
        carrinho = Carrinho()
        carrinho.adicionar_item(produto, 2)
        pedido = Pedido(carrinho=carrinho)
    assert "missing 1 required positional argument: 'pessoa'" in str(excinfo.value)

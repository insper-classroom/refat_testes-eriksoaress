import pytest
from classes.Endereco import Endereco
from classes.PessoaFisica import PessoaFisica

@pytest.mark.com_internet
@pytest.mark.pessoafisica
def test_adiciona_endereco_da_pessoa():
    erik = PessoaFisica(49340635899, 'erikbtu2017@gmail.com', 'Erik')
    erik.adicionar_endereco('Toca', Endereco('04552040', 265))
    erik = erik.get_endereco('Toca')
    assert erik == "Rua Elvira Ferraz - 265(SP)"

@pytest.mark.com_internet
@pytest.mark.pessoafisica
def test_remove_endereco_da_pessoa():
    with pytest.raises(TypeError) as excinfo:
        erik = PessoaFisica(49340635899, 'erikbtu2017@gmail.com', 'Erik')
        erik.adicionar_endereco('Toca', Endereco('04552040', 265))
        erik.remover_endereco('Toca')
        erik = erik.get_endereco('Toca')
    assert 'KeyError' in str(excinfo)

@pytest.mark.com_internet
@pytest.mark.pessoafisica
def test_busca_nome_pessoa_maiuscula():
    erik = PessoaFisica(49340635899, 'erikbtu2017@gmail.com', 'Erik')
    pesquisa_nome = 'ER'
    assert PessoaFisica.busca_nome(pesquisa_nome)[0].nome == 'Erik'

@pytest.mark.com_internet
@pytest.mark.pessoafisica
def test_busca_nome_pessoa_minuscula():
    erik = PessoaFisica(49340635899, 'erikbtu2017@gmail.com', 'Erik')
    pesquisa_nome = 'er'
    assert PessoaFisica.busca_nome(pesquisa_nome)[0].nome == 'Erik'

@pytest.mark.com_internet
@pytest.mark.pessoafisica
def test_listar_enderecos_da_pessoa():
    erik = PessoaFisica(49340635899, 'erikbtu2017@gmail.com', 'Erik')
    erik.adicionar_endereco('Casa', Endereco(18604694, 200))
    erik.adicionar_endereco('Trabalho', Endereco('04552040', 300))
    assert erik.listar_enderecos() == ['Casa', 'Trabalho']


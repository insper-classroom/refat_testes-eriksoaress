import pytest
from classes.Endereco import Endereco

@pytest.mark.com_internet
@pytest.mark.endereco
def test_endereco_sem_numero():
    cep = '18604694'
    with pytest.raises(TypeError) as excinfo:
        endereco = Endereco(cep)
    assert "missing 1 required positional argument: 'numero'" in str(excinfo.value)

@pytest.mark.com_internet
@pytest.mark.endereco
def test_endereco_sem_cep():
    with pytest.raises(TypeError) as excinfo:
        endereco = Endereco(numero=200)
    assert "missing 1 required positional argument: 'cep'" in str(excinfo.value)

@pytest.mark.com_internet
@pytest.mark.endereco
def test_cep_string():
    cep = '18604694'
    endereco = Endereco.consultar_cep(cep)
    assert endereco['logradouro'] == 'Rua José Miguel Salomão'

@pytest.mark.com_internet
@pytest.mark.endereco
def test_cep_int():
    cep = 18604694
    endereco = Endereco.consultar_cep(cep)
    assert endereco['logradouro'] == 'Rua José Miguel Salomão'

@pytest.mark.com_internet
@pytest.mark.endereco
def test_cep_com_mais_digitos():
    cep = 186046945
    assert Endereco.consultar_cep(cep) == False

@pytest.mark.com_internet
@pytest.mark.endereco
def test_cep_com_menos_digitos():
    cep = 1860469
    assert Endereco.consultar_cep(cep) == False

@pytest.mark.com_internet
@pytest.mark.endereco
def test_cep_inexistente():
    cep = '12345678'
    endereco = Endereco.consultar_cep(cep)
    assert endereco['erro'] == 'true'

@pytest.mark.sem_internet
@pytest.mark.endereco
def test_sem_internet():
    cep = '18604694'
    with pytest.raises(TypeError) as excinfo:
        endereco = Endereco.consultar_cep(cep)
    assert "getaddrinfo failed" in str(excinfo.value)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Erik Soares - https://github.com/eriksoaress
# Created Date: 26/08/2022
# version ='1.0'
# ---------------------------------------------------------------------------

from classes.Endereco import Endereco
from classes.PessoaFisica import PessoaFisica
from classes.Carrinho import Carrinho


class Pedido:
    def __init__(self, pessoa:PessoaFisica, carrinho:Carrinho):
        self.nome = pessoa.nome
        self.itens_str = carrinho
        self.endereço = pessoa.listar_enderecos()

    def __str__(self):
        return f'{self.nome} - {self.endereço}: {self.itens_str}'

    EM_ABERTO = 1
    PAGO = 2
    pass
    
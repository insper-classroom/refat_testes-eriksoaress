#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Erik Soares - https://github.com/eriksoaress
# Created Date: 26/08/2022
# version ='1.0'
# ---------------------------------------------------------------------------

from traceback import print_tb
from classes.Endereco import Endereco
from classes.Produto import Produto
from classes.PessoaFisica import PessoaFisica

# Esta classe deverá permitir a inserção de items, bem como a atualização da quantidade de
# produtos em um item

class Carrinho:

    def __init__(self):
        # Chave é o id do Produto e o Valor é a quantidade desse item no carrinho
        self.itens = {}

    def adicionar_item(self, item:Produto, qtd):
        id = item.get_id()
        self.qtd = qtd
        self.itens[id] = {f'{item.nome}':f'{self.qtd}'}    
        # Implemente a adição do item no dicionário
        

    def remover_item(self, id):
        del self.itens[id]
        # Implemente este método
    
    def __str__(self):
        print(str(self.itens))
        return str(self.itens)
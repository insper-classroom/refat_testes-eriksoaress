#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Tiago Sanches da Silva e Fabio Miranda - https://github.com/Tiagoeem | https://github.com/mirwox
# Created Date: 15/08/2022
# version ='1.0'
# ---------------------------------------------------------------------------

from classes.PessoaFisica import PessoaFisica

class Produto:
    lista_produtos = []
    def __init__(self, id_produto, nome=''):
        self.__id_produto = id_produto
        self.__nome = nome
        Produto.lista_produtos.append(self)

    def set_id(self, idnovo_produto):
        self.__id_produto = idnovo_produto

    def get_id(self):
        return self.__id_produto
    
    def __str__(self):
        return f'{self.__id_produto} - {str(self.__nome)}'

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome_novo):
        if nome_novo[0] != 'T':
            self.__nome = nome_novo

    @nome.getter
    def nome(self):
        return self.__nome

    def busca_nome(pesquisa):
        produtos_correspondentes = []
        for produto in Produto.lista_produtos:
            if pesquisa.lower() in produto.nome.lower():
                produtos_correspondentes.append(produto)
        return produtos_correspondentes
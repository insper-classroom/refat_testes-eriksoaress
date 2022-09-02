#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Tiago Sanches da Silva e Fabio Miranda - https://github.com/Tiagoeem | https://github.com/mirwox
# Created Date: 15/08/2022
# version ='1.0'
# ---------------------------------------------------------------------------

from classes.Endereco import Endereco


class PessoaFisica:
    lista_pessoas = []
    '''Esta classe implementa uma pessoa no contexto de uma compra em e-commerce.
    
    As propriedades email e cpf estão privadas para previnir o usuário da classe de 
    acessar e alterar diretamente a propriedade sem uma verificação.
    '''

    def __init__(self, cpf, email, nome='Visitante'):
        self.nome = nome
        self.__email = email
        self.__cpf = cpf
        self.__enderecos = {}
        PessoaFisica.lista_pessoas.append(self)

    # escolher o estilo de retorno

    def __str__(self):
        return self.nome

    def adicionar_endereco(self, apelido_endereco, end:Endereco):
        self.apelido_endereco = apelido_endereco
        self.__end = end
        self.__enderecos[f'{apelido_endereco}'] = self.__end
        pass

    def remover_endereco(self, apelido_endereco):
        del self.__enderecos[f'{apelido_endereco}']

    def get_endereco(self, apelido_endereco):
        return self.__enderecos[f'{apelido_endereco}']
    
    def busca_nome(pesquisa_nome):

        pessoas_correspondentes = []
        for pessoa in PessoaFisica.lista_pessoas:
            if pesquisa_nome.lower() in pessoa.nome.lower():
                pessoas_correspondentes.append(pessoa)
        return pessoas_correspondentes


    def listar_enderecos(self):
        enderecos_lista = []
        for end in self.__enderecos:
            enderecos_lista.append(end)
        return enderecos_lista
    

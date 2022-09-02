from operator import truediv


class Pagamento:
    def __init__(self, pedido):
        self.pedido = pedido 

    def processa_pagamento(self):
        return f'Processando pagamento'
    # Função dummy que sempre dá o pagamento como aprovado
    def pagamento_aprovado(self):
        return True

    
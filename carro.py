import veiculo

class Carro(veiculo.Veiculo):
    def __init__(self, cor, tipo_combustivel, potencia, qtd_portas):
        super().__init__(cor, tipo_combustivel, potencia)
        self.qtd_portas = qtd_portas
        self.velocidade = 0
        self._qtd_combustivel = 0

    def abastecer(self, qtd_combustivel):
        print('O método foi chamado a partir da classe carro')
        self._qtd_combustivel += qtd_combustivel
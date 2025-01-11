import veiculo

class Carro(veiculo.Veiculo):
    def __init__(self, cor, tipo_combustivel, potencia, qtd_portas):
        super().__init__(cor, tipo_combustivel, potencia)
        self.qtd_portas = qtd_portas
        self._libras = 20

    def abastecer(self, qtd_combustivel):
        print("O método foi chamado a partir da classe Carro")
        self._qtd_combustivel += qtd_combustivel

    def pintar(self, cor):
        if cor == "preto":
            print("O carro não pode ser pintado de preto")
        else:
            self._cor = cor

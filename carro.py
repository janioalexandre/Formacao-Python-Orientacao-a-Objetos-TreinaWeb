class Carro():
    """Essa é a classe carro, Essa classe é utilizada para instanciar novos carros em nosso programa"""
    def __init__(self, cor, qtd_portas, tipo_combustivel, potencia):
        self.cor = cor
        self.qtd_portas = qtd_portas
        self.tipo_combustivel = tipo_combustivel
        self.potencia = potencia
        self.qtd_combustivel = 0
        self.is_ligado = 0
        self.velocidade = 0

    def __del__(self):
        print('O objeto foi removido da memória. :)')

    def abastecer(self, qtd_combustivel):
        """O método abastecer recebe como parêmetro a quantidade de combustível e incrementa no atributo qtd_combustivel do objeto carro"""
        self.qtd_combustivel += qtd_combustivel
    
    def ligar (self):
        if self.is_ligado:
            print('O carro já está ligado')
        else:
            self.is_ligado = True
            print('O carro foi ligado')
            
    def desligado(self):
        if self.is_ligado == False:
            print('O carro já está desligado')
        else:
            self.is_ligado = False

    def acelerar(self, velocidade=10):
        if self.is_ligado:
            self.velocidade += velocidade
        else:
            print('O carro precisa estar ligado para acelerar')

class Veiculo():
    """Essa é a classe Veiculo. Esta classe é utilizada para instanciar novos veiculos em nosso sistema."""
    def __init__(self, cor, tipo_combustivel, potencia):
        self.cor = cor
        self.tipo_combustivel = tipo_combustivel
        self.potencia = potencia
        self.qtd_combustivel = 0
        self.is_ligado = False
        self.velocidade = 0
    
    def __del__(self):
        print('O objeto foi removido da memória. :)')

    def abastecer(self, qtd_combustivel):
        """O método abastecer recebe como parâmetro a quantidade de combustível que será abastecida no carro."""
        self.qtd_combustivel += qtd_combustivel

    def ligar(self):
        if self.is_ligado:
            return 'O veiculo já está ligado'
        else:
            self.is_ligado = True
            print('O veiculo foi ligado')
    
    def desligar(self):
        if self.is_ligado == False:
            print('O veiculo já está desligado')
        else:
            self.is_ligado = False
            print('O veiculo foi desligado')
    
    def acelerar(self, velocidade=10):
        if self.is_ligado:
            self.velocidade += velocidade
        else:
            print('O veiculo precisa estar ligado para acelerar')

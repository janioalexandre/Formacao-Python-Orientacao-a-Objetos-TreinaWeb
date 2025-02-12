class Veiculo():
    """Essa é a classe Veiculo. Esta classe é utilizada para instanciar novos veiculos em nosso sistema."""
    def __init__(self, cor, tipo_combustivel, potencia):
        self.__cor = cor
        self.__tipo_combustivel = tipo_combustivel
        self.__potencia = potencia
        self._qtd_combustivel = 0
        self.__is_ligado = False
        self.__velocidade = 0
    
    def __del__(self):
        print('O objeto foi removido da memória. :)')

    def pintar(self, cor):
        self.__cor = cor
        print(f'A cor do veiculo foi alterada para {cor}')

    def abastecer(self, qtd_combustivel):
        """O método abastecer recebe como parâmetro a quantidade de combustível que será abastecida no carro."""
        self.__qtd_combustivel += qtd_combustivel

    def ligar(self):
        if self.__is_ligado:
            return 'O veiculo já está ligado'
        else:
            self.__is_ligado = True
            print('O veiculo foi ligado')
    
    def desligar(self):
        if self.__is_ligado == False:
            print('O veiculo já está desligado')
        else:
            self.__is_ligado = False
            print('O veiculo foi desligado')
    
    def acelerar(self, velocidade=10):
        if self.__is_ligado:
            self.__velocidade += velocidade
        else:
            print('O veiculo precisa estar ligado para acelerar')

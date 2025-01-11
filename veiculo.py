import abc

class Veiculo():
    """Essa é a classe carro, Essa classe é utilizada para instanciar novos carros em nosso programa"""
    def __init__(self, cor, tipo_combustivel, potencia):
        self._cor = cor
        self.__tipo_combustivel = tipo_combustivel
        self.__potencia = potencia
        self._qtd_combustivel = 0
        self._is_ligado = 0
        self._velocidade = 0
        self._libras = 0

    def __del__(self):
        print('O objeto foi removido da memória. :)')

    @abc.abstractmethod
    def pintar(self, cor):
        """O método pintar recebe uma string cor e atribui ao atributo cor do objeto carro"""
        self._cor = cor

    @property
    def cor(self):
        """O método cor retorna a cor do objeto carro"""
        return self._cor

    def abastecer(self, qtd_combustivel):
        """O método abastecer recebe como parêmetro a quantidade de combustível e incrementa no atributo qtd_combustivel do objeto carro"""
        self.__qtd_combustivel += qtd_combustivel
    
    def ligar (self):
        if self._is_ligado:
            print('O veiculo já está ligado')
        else:
            self._is_ligado = True
            print('O veiculo foi ligado')
            
    def desligado(self):
        if self._is_ligado == False:
            print('O veiculo já está desligado')
        else:
            self._is_ligado = False

    def acelerar(self, velocidade=10):
        if self._is_ligado:
            self._velocidade += velocidade
        else:
            print('O veiculo precisa estar ligado para acelerar')

import carro

uno_vermelho = carro.Carro('preto', 4, 'gasolina', 2.0, 0, False, 0)
uno_vermelho.ligar()
uno_vermelho.abastecer(10)
uno_vermelho.acelerar()
print(f"A quantidade de combustível no carro é {uno_vermelho.qtd_combustivel}")
print(f"A velocidade do carro é {uno_vermelho.velocidade}")
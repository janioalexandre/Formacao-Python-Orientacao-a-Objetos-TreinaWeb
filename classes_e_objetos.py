import carro, moto

uno_vermelho = carro.Carro('preto', 4, 'gasolina', 2.0)
# help(carro.Carro)
# help(uno_vermelho.abastecer)
uno_vermelho.ligar()
uno_vermelho.abastecer(10)
uno_vermelho.acelerar()
uno_vermelho.pintar("preto")
print(uno_vermelho.cor)
print(f"A quantidade de combustível no carro é {uno_vermelho._qtd_combustivel}")
print(f"A velocidade do carro é {uno_vermelho._velocidade}")

moto_vermelha = moto.Moto('vermelha', 'gasolina', 1.0, 2)
moto_vermelha.ligar()
moto_vermelha.abastecer(30)
moto_vermelha.abastecer(10)
print(moto_vermelha._is_ligado)

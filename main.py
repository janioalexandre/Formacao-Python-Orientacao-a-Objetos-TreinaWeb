import carro, moto

prisma_vermelho = carro.Carro('vermelho', 'flex', 1.0, 4)
prisma_vermelho.ligar()
help(prisma_vermelho.abastecer)
# help(carro.Carro)
prisma_vermelho.abastecer(50)
prisma_vermelho.abastecer(10)
print(prisma_vermelho.velocidade)
print(f"A quantidade de combustível do carro é: {prisma_vermelho.qtd_combustivel}")

moto_vermelha = moto.Moto('vermelho', 'gasolina', 1.0, 2)
moto_vermelha.ligar()
moto_vermelha.abastecer(30)
moto_vermelha.abastecer(10)
print(moto_vermelha.is_ligado)

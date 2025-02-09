import carro

prisma_vermelho = carro.Carro('vermelho', 4, 'flex', 1.0, 0, False, 0)
prisma_vermelho.ligar()
prisma_vermelho.abastecer(20)
prisma_vermelho.abastecer(10)
print(f"A quantidade de combustível do carro é: {prisma_vermelho.qtd_combustivel}")

onix_preto = carro.Carro('preto', 4, 'flex', 1.0, 0, False, 0)
onix_preto.ligar()
onix_preto.acelerar()
print(f"A velocidade do carro é: {onix_preto.velocidade}")
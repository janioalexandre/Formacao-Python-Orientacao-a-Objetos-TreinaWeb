import carro

prisma_vermelho = carro.Carro('vermelho', 4, 'flex', 1.0)
prisma_vermelho.ligar()
help(prisma_vermelho.abastecer)
# help(carro.Carro)
prisma_vermelho.abastecer(10)
print(f"A quantidade de combustível do carro é: {prisma_vermelho.qtd_combustivel}")
del prisma_vermelho

onix_preto = carro.Carro('preto', 4, 'flex', 1.0)
onix_preto.ligar()
onix_preto.acelerar()
print(f"A velocidade do carro é: {onix_preto.velocidade}")

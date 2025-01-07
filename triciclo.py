import veiculo, moto

class Triciclo(veiculo.Veiculo, moto.Moto):
    
    print(super().qtd_passageiros)
    

nome_motorista = input("Digite o nome do motorista: ")
distancia = float(input("Digite a distância da viagem em quilômetros: "))
velocidade = float(input("Digite a velocidade média da viagem em km/h: "))

tempo = distancia / velocidade


print("O motorista", nome_motorista, "levará aproximadamente", tempo, "horas para fazer a viagem.")
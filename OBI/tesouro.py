num_moedas_arca = int(input())
num_marinheiros = int(input())

total_tripulantes = num_marinheiros + 2 # o Capitão conta como dois tripulantes
moedas_marinheiros = num_moedas_arca / total_tripulantes # calculo de quantas moedas cada marinheiro 
# irá receber
moedas_capitao = moedas_marinheiros * 2 # o Capitão recebe o dobro de moedas 
print("{:.0f}".format(moedas_capitao))
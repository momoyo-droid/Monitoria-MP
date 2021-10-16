# Programa que calcula se o atleta precisa diminuir, aumentar ou manter seu ritmo de exercício.

freq_cardiaca_repouso = int(input())
freq_cardiaca_atual = int(input())
capacidade_oxig = int(input())

if(freq_cardiaca_atual > freq_cardiaca_repouso*3 or capacidade_oxig < 95 ):
    print("diminuir")
elif(freq_cardiaca_atual < freq_cardiaca_repouso*2 and capacidade_oxig > 97):
    print("aumentar")
else:
    print("manter")
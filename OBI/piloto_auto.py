# Programa que calcula a distância da traseira de um carro para outro.
# caso o carro precise acelerar, resultado: 1
# caso o carro precise desacelarar, resultado: -1
# caso o carro precise manter a velocidade, resultado: 0

traseira_A = int(input())
traseira_B = int(input())
traseira_C = int(input())

if(traseira_B-traseira_A < traseira_C-traseira_B):
    print("1")
elif(traseira_B-traseira_A > traseira_C-traseira_B):
    print("-1")
else:
    print("0")

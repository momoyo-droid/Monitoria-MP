# Solução para o código que calcula quantas viagens deve-se fazer com caixar de tamanhos diferentes

tam_caixa_a = int(input())
tam_caixa_b = int(input())
tam_caixa_c = int(input())

if(tam_caixa_a == tam_caixa_b and tam_caixa_b == tam_caixa_c):
    print("3")
elif(tam_caixa_a < tam_caixa_b and tam_caixa_b < tam_caixa_c):
    print("1")
elif(tam_caixa_a == tam_caixa_b and tam_caixa_a + tam_caixa_b < tam_caixa_c):
    print("1")
else:
    print("2")
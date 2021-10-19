# Solução que calcula a quantidade de camisetas entregues aos premiados

n_premiados = int(input())

qtd_p = 0
qtd_m = 0

tamanhos = [int(i) for i in input().split()]   
p = int(input())
m = int(input())

qtd_p = tamanhos.count(1)
qtd_m = tamanhos.count(2)

if(p >= qtd_p and m >= qtd_m):
    print("S")
else:
    print("N")

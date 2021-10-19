# Solução do código que calcula em quantos dias a Dona Lesma conseguirá alcançar o topo do muro
altura_muro = int(input())
dist_sobe = int(input())
dist_escorrega = int(input())

n_dias = 0
dist_dia = 0

while(1):
    n_dias += 1
    dist_dia = dist_dia + dist_sobe
    if dist_dia >= altura_muro:
        break
    dist_dia = dist_dia - dist_escorrega

print(n_dias)

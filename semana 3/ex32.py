cima = input()
baixo = input()
esq = input()
dirr = input()
subst = input()
# a s w d -> esq, baixo, cima, dir

# T B L E d -> yes
# T B E R a -> yes

if(cima == 'E' and baixo == 'B' and esq == 'L' and dirr == 'R' and subst == 'w'):
    print("yes!")
elif(cima == 'T' and baixo == 'E' and esq == 'L' and dirr == 'R' and subst == 's'):
    print("yes!")
elif(cima == 'T' and baixo == 'B' and esq == 'E' and dirr == 'R' and subst == 'a'):
    print("yes!")
elif(cima == 'T' and baixo == 'B' and esq == 'L' and dirr == 'E' and  subst == 'd'):
    print("yes!")
else:
    print("next player...")
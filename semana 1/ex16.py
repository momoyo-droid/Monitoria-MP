# Solution to the code that calculates how many black and white squares have a board of size n
n = int(input())

total_quadrados = pow(n,2)

casa_p = int(total_quadrados/2)

casa_b = total_quadrados - casa_p

print("{} casas brancas e".format(casa_b),"{} casas pretas".format(casa_p))
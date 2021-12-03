import math
a, b, c = map(int, input().split())
delta = (b**2)-(4*a*c)
raiz_delta = math.sqrt(delta)
x_1 = ((-1*b) + raiz_delta) / 2*a
x_2 = ((-1*b) - raiz_delta) / 2*a

print("{:.1f} {:.1f}".format(x_1,x_2))
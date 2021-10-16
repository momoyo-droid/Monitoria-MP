# Code solution for calculating the area of ​​geometric figures: 
# right triangle, circle, trapezoid, square, rectangle

a, b, c = [float(i) for i in input().split()]


pi = 3.14159

area_tri_rect = (a*c)/2
area_circ = pow(c, 2)*pi
area_trapezium = (a+b)*c/2
area_square = pow(b, 2)
area_rect = a*b

print("TRIANGULO: {:.3f}".format(area_tri_rect))
print("CIRCULO: {:.3f}".format(area_circ))
print("TRAPEZIO: {:.3f}".format(area_trapezium))
print("QUADRADO: {:.3f}".format(area_square))
print("RETANGULO: {:.3f}".format(area_rect))
# Code solution for calculating the distance between two points
import math

x1, y1 =[float(i) for i in input().split()]
x2, y2 =[float(i) for i in input().split()]


distance = math.sqrt(pow(x2-x1, 2) + pow(y2-y1, 2))
print("{:.4f}".format(distance))
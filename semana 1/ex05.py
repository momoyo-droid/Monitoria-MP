# Code solution to find the highest number among three

a, b, c = [int(i) for i in input().split()]

greatestAB = ((a+b+abs(a-b))/2)

greatestABC = ((greatestAB+c+abs(greatestAB - c))/2)

print("{:.0f}".format(greatestABC),"eh o maior")
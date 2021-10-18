# Solution for code that prints x numbers per line to a y value

x, y = [int(i) for i in input().split()]

for i in range(1,y+1):
    print(i, end = " ")
    if(i % x == 0):
        print()
print()
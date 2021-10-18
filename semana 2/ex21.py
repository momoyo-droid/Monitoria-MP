# Solution code that calculates division of X by Y

n = int(input())

for i in range(n):
    x,y = map(float, input().split())
    if(y == 0):
        print("divisao impossivel")
    else:
        result = x/y
        print("{:.1f}".format(result))
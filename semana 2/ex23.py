# Solution code that calculates the highest read value and the input position.

j = 0

for i in range(100):
    n = int(input())
    if(i == 0):
        highest = n
        j = i
    if(n > highest):
        highest = n
        j = i+1

print(highest)
print(j)
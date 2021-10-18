# Solution code for fibonacci sequence

n = int(input())

v = []

for num in range(0, n):

    if(num <= 1):
        v.append(num)
        print("{}".format(v[num]), end = " ")
    else:
        fn = v[num - 1] + v[num - 2]
        v.append(fn)
        if(num == n-1):
            print("{}".format(fn), end="")
            break
        
        print("{}".format(fn), end=" ")

print()
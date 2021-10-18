# Solution for code that performs a sequence of values ​​(smallest to biggest) 
# and calculates the sum between them

while(1):
    m,n = map(int, input().split())
    if(m == 0 or n == 0 or m < 0 or n < 0):
        print(end = " ")
        break
    
    sum = 0
    for i in range(n,m+1):
        sum += i
        print(i, end=" ")
    
    print("Sum={}".format(sum))

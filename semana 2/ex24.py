# Solution for the code that calculates which are the divisors of a number, 
# performs the sum between each one of them and checks if the result is equal to the number starts x

n_input = int(input())

for i in range(1,n_input+1):
    x = int(input())
    divisors = 0
    
    for j in range(1,x):
        if(x % j == 0):
            divisors += j
            
    if(divisors == x):
        print(x,"eh perfeito")
    else:
        print(x,"nao eh perfeito")
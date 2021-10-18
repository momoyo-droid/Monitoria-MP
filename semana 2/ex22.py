# Solution to code that calculates how many numbers are positive and the average of positive numbers

count_positive_numbers = 0
average = 0

for i in range(6):
    x = float(input())
    if(x > 0):
        count_positive_numbers += 1
        average += x
    
print(count_positive_numbers, "valores positivos")
print("{:.1f}".format(average/4))
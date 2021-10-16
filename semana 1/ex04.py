# Code Solution for Calculating Gasoline Expenses on a Trip

hour = int(input())
speed = int(input())

distance = hour * speed

result_liters = distance/12.0

print("{:.3f}".format(result_liters))
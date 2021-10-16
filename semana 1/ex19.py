# Solution to the code that calculates salary with bonus employee's
seller_name = input()
fixed_salary = float(input())
sale_total = float(input())

total_salary = ((15/100) * sale_total) + fixed_salary
print("TOTAL = R$ {:.2f}".format(total_salary))

# Solution to the code that calculates salary employee's

n_employees = int(input())
worked_hours = int(input())
amount_per_hour = float(input())

print("NUMBER =", n_employees)

salary = worked_hours*amount_per_hour
print("SALARY = U$ {:.2f}".format(salary))

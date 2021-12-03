bin_num = []
count = 0
j = 3
for i in range(4):
    bin_num.append(int(input()))
for i in range(4):
    count += bin_num[i]*(2**j)
    j -= 1


print(count)

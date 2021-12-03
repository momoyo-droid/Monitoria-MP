strings = []
for i in range(3):
    strings.append(input())

for i in range(3):
    for j in range(3):
        if(strings[i] == strings[j]):
            continue
        print(strings[i]+strings[j])
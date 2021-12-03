name = input()
grades = []
count = 0

for i in range(5):
    grades.append(float(input()))
    count += grades[i]
    
print("Ciências da Natureza:", grades[0])
print("Ciências Humanas:", grades[1])
print("Linguagens e Códigos:", grades[2])
print("Matemática:", grades[3])
print("Redação:", grades[4])
print(name,"obteve",count,"pontos.")
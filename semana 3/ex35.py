count = 0
for i in range(6):
    face = input()
    if(face == 'P'):
        count += 1

if(count == 6):
    print("Sena!")
else:
    print("Jogue de novo...")

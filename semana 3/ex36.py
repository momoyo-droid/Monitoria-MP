character = input()
character_conv = character.upper()

if(character_conv == 'A'):
    print("LEFT")
elif(character_conv == 'S'):
    print("DOWN")
elif(character_conv == 'D'):
    print("RIGHT")
elif(character_conv == 'W'):
    print("UP")
else:
    print("?")
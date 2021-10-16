# Solution of the code that calculates who is the middle nephew of uncle Patinhas
age_h, age_z, age_l = [int(i) for i in input().split()]


# case Huguinho age's
if(age_h > age_z and age_h < age_l or age_h < age_z and age_h > age_l):
    print("huguinho")
# case Zezinho age's
elif(age_z > age_h and age_z < age_l or age_z < age_h and age_z > age_l):
    print("zezinho")
# case luisinho age's
elif(age_l > age_h and age_l < age_z or age_l < age_h and age_l > age_z):
    print("luisinho")
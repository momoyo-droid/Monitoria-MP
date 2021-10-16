# Solution of the code that calculates the average grade

a = float(input())
b = float(input())

a_media = (a * 3.5)/11
b_media = (b * 7.5)/11

total_media = a_media + b_media
print("MEDIA = {:.5f}".format(total_media))
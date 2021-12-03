minutes = int(input())
to_complete = 1

hours = minutes // 60
aux = hours

if(aux >= 1):
    aux *= 60
    to_complete = minutes - aux
    print("{} minutos = {} horas e {} minutos".format(
        minutes, hours, to_complete))
else:
    print("{} minutos = {} horas e {} minutos".format(
        minutes, hours, to_complete))

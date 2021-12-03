name = input()
school_year = int(input())
key = input()

if(school_year == 3 and key == 'P'):
    print(name,"selecionada! (3o ano em escola publica)")
elif(school_year != 3):
    print(name,"NAO selecionada (ANO sem prioridade)")
else:
    print(name,"NAO selecionada (NAO escola publica)")
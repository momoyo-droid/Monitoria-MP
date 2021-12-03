name = input()
last_name = input()
doc = int(input())

if(doc == 1):
    school = input()
    if(school == 'P'):
        print(name,last_name,"selecionada (com prioridade)")
    elif(school == 'O'):
        print(name,last_name,"não selecionada (sem prioridade)")
else:
    print(name,last_name,"não selecionada (documentação incompleta)")

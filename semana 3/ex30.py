name = input()
last_name = input()
school = input()
percentage_scholarship = int(input())

if(school == 'O' and percentage_scholarship == 100):
    print(name, last_name,"selecionada (com prioridade)")
elif(school == 'P' and percentage_scholarship == 0):
    print(name, last_name,"selecionada (com prioridade)")
elif(school == 'O' and percentage_scholarship < 100):
    print(name, last_name,"não selecionada (turma lotou com alunas de escola pública, ou com alunas de outras escolas com 100% de bolsa)")
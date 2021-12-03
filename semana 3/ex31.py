name = input()
school = input()
has_scholarship = input()
school_year = int(input())

if(school == 'P' and has_scholarship == 'N' and school_year == 3):
    print(name, "selecionada (com prioridade)")
elif(school == 'O' and has_scholarship == 'S' and school_year == 3):
    print(name, "selecionada (com prioridade)")
elif(school == 'O' and has_scholarship == 'N' and school_year == 3):
    print(name, "não selecionada (turma lotou com alunas de escola pública, ou com alunas de outras escolas com bolsa)")
else:
    print(name, "não selecionada (turma lotou com alunas do 3o ano)")

#DIA E MES VALIDOS
dia = int(input("Dia: "))
mes = int(input("Mês: "))

#Duas estratégias:
# checar as data inválidas
# checar as data válidas
#caso nenhuma das validações seja contemplada,
#significa exatamente o contrário

if dia < 1 or dia > 31 or mes < 1 or mes > 12:
    print("Data inválida!")
elif mes == 2 and dia > 28:
    print("Data inválida!")
elif dia == 31 and (mes == 4 or mes == 6 or mes == 9 or mes == 11):
    print("Data inválida!")
else:
    print("Data válida!")






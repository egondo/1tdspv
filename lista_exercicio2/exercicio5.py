dias_uteis = int(input("Dias úteis: "))
horas_trab = int(input("Horas trabalhadas: "))
sal_hora = float(input("Salario por hora: "))

jornada_obrigatoria = dias_uteis * 8

if horas_trab <= jornada_obrigatoria:
    sal_mensal = horas_trab * sal_hora
else:
    horas_extra = horas_trab - jornada_obrigatoria
    valor_extra = horas_extra * sal_hora * 0.5
    print(f"Valor hora extra R$ {valor_extra}")
    sal_mensal = horas_trab * sal_hora + valor_extra

print(f"Salário mensal R$ {sal_mensal}")
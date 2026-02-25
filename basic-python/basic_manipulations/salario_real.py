salario = int(input('Salario: '))
imposto = float(input('Imposto em % (ex: 27.5): '))
print("Valor real:{0}".format(salario - (salario * imposto * 0.01)))

if imposto < 10:
    print("Imposto considerado baixo, iremos te taxar")
elif imposto >= 10. and imposto <= 15.:
    print("Estamos Chegando a um consenso, seu imposto irá subir mais")
elif imposto >= 15 and impost < 100:
    print("ta na média, queremos dinheiro companheiro")
else:
    print("Imposto inválido!")
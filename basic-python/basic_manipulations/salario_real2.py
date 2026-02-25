def salario_descontado_imposto(salario, imposto=27.):
    return salario - (salario * imposto * 0.01)

salario = int(input("Informe o seu salario: "))
while True:
    entrada = input('Imposto ou (S) para sair: ')
    if entrada.upper() == 'S':
        break
    if not entrada:
        valor_real = salario_descontado_imposto(salario)
    else:
        try:
            imposto_digitado = float(entrada)
            #se digitou algo passa o valor para funcao
            valor_real = salario_descontado_imposto(salario, imposto_digitado)
        except ValueError:
            print('OPS! Digite apenas Numeros')
            continue
    print("Valor Real {0}".format(valor_real))
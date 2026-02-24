salario = int(input('Salario: '))
imposto = 27.
while True:
    entrada = input('Imposto ou (S) para sair: ')
    
    if not entrada:
        imposto = 27.
        
    elif entrada == 'S':
        break
    #verificação e validação de entrada apenas de numbers
    else: 
        try:
            impost = float(entrada)
        except ValueError:
            print("Ops! Digite apenas Numeros!")
            continue
        
        valor_real = salario - (salario * imposto * 0.01)
        print("Valor real: {0}".format(valor_real))
            
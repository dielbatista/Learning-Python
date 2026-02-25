"""**UNPACKING DOS ARGUMENTOS
    o Unpacking é o processo que é executado dentro da função, e não na chamada.
    podemos usar a sintaxe *args ou **kwargs como argumentos para o unpacking
    dos parametros posicionados ou nomeados
"""
#args method
def unpacking_experiment(*args):
    arg1 = args[0]
    arg2 = args[1]
    others = args[2:]
    print(arg1)
    print(arg2)
    print(others)
unpacking_experiment(1, 2, 3, 4, 5, 6)

#kwargs method
def unpacking_experiment_1(**kwargs):
    print(kwargs)
    unpacking_experiment_1(named="Test", other="Other")
    {'other': 'Other', 'named': 'test'}
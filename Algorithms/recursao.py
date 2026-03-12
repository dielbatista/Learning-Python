#Exemplo de como Procurar um item dentro de uma lista usando recursão.

#ABORDAGEM 1

#abordagem usa um loop while para buscar 
#pegue uma caixa e olhe dentro dela
def pesquisa_iterativa(caixa_principal):
    pilha = main_box.crie_pilha()
    while pilha is not vazia:
        caixa = pilha.pegeue_caixa()
        for item in caixa:
            if item in caixa:
                if item.e_uma_caixa:
                    pilha.empilhe(item)
                elif item.e_uma_chave:
                    print ("Chave encontrada!") 
                    
#ABORDAGEM RECURSIVA
def pesquisa_recursiva(caixa):
    for item in caixa:
        if item in caixa:
            if item.e_uma_caixa:
                pesquisa_recursiva(item)
            elif item.e_uma_chave:
                print ("Chave encontrada!")
                
                
#cuidado ao usar recursão pois pode causar um estouro de pilha (stack overflow) se a profundidade da recursão for muito grande.
#ou um loop infinito se a condição de parada não for bem definida.

def regressiva(i):
    print(i)
    if i <= 0:
        return
    else:
        regressiva(i-1) 
#

nomes = [
    "Ana Beatriz",
    "Bruno Henrique",
    "Carlos Eduardo",
    "Daniela Rocha",
    "Felipe Alves",
    "Gabriel Santos",
    "Lucas Pereira",
    "Mariana Costa",
    "Rafael Oliveira",
    "Thiago Martins"
]
#Quanto maior a lista, maior a diferença.

#Exemplo:

#n	                  log₂(n)
# 10	                   4
# 100	                   7
# 1.000	                   10
# 1.000.000	               20

def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista)-1
    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]
        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None        
print(pesquisa_binaria(nomes, "Thiago Martins"))

#Visualizando na prática

#Lista com 10 elementos:

#1ª divisão → 10 / 2 = 5
#2ª divisão → 5 / 2 = 2
#3ª divisão → 2 / 2 = 1
#4ª divisão → 1 / 2 ≈ 0

#Ou seja:

#No máximo 4 comparações grandes
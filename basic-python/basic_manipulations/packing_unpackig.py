#receiving a arbitrary number of arguments (packin & unpacking)
#page 38 to 40

from datetime import date

d = (2026, 2, 25)
date_1 = date(*d)
print(date_1)

"""
o que aconteceu aqui é que se date 
espera parametros
year, month, day e temos uma lista ou 
tupla com valores que 
casam essa ordem, podemos usar a sintax do 
*tupla para sinalizar
a coleção deve ter suas posições casadas com parâmetros.recebidos
"""
"""Caso o packing seja sinalizado, mas a coleção tenha mais elementos
que o parametros da função, vamos recebe um TypeError"""
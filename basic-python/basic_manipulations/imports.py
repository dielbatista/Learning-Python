"""*IMPORTANDO MÓDULOS
Outra Manipulação básica é a importação de módulos.
Nesse caso, utilizamos o comando from/import, sinalizando no from
o modulo, e depois do import, informamos que objeto queremos importar 
"""
#from unittest import TestCase
#from unittest import mock
#podemos usar o recurso do alias com o from/import também:
#from math import log2 as 12
#print(12(1024))

import calendar
cal = calendar.calendar(2026)
print(cal)
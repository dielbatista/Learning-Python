"""O packing também vale para parametros nomeados.
muitas vezes é comum que os parametros estejam ja 
disponveis em um dicionario,
sem o packing, teríamos algo como"""

def new_user(active=False, admin=False):
    print(active)
    print(admin)
    
config = {"active": False,
          "admin": True}
new_user(config.get('active'),config.get('admin'))

"""Porém, queremos algo mais elegante, e enxuto.
Podemos usar o packing com os parametros nomeados:"""

def new_user(active = False, admin = False):
    print(active)
    print(admin)
    
config = {"active": False,
          "admin": True}
new_user(**config) #sintaxe mais enxuta

#page 35 to 36 same book Python Escreva seus primeiros programas 
lista = [0,1,2,3,4,5,6,7,8,9,] #simple list

for i in lista :
    print(i)
    
#we can use the range() function
#classic method for(i = 0; i < n; i++) exists in C,JAVA,JS
for i in range(5): #range 5 method
    print(i)
    
    
#enumarate function enumarates an element
impostos = ['MEI','Simples']
for i, imposto in enumerate(impostos):
    print(i, imposto)

#the for command works on(sequences,lists,strings or iterable obj)
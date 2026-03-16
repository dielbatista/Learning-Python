#For iteration on a dict data structure.
alunos = {
    'João': 8.5,
    'Maria': 9.0,
    'Pedro': 7.5,
    'Ana': 9.5,
    'Lucas': 6.0
}
for aluno, nota in alunos.items():
    
    if alunos[aluno] >= 7.0:
        print(f'{aluno} passou com nota {nota}')
    else:
        print(f'{aluno} reprovou com nota {nota}')
        
#also we can iterate a list

numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)


#now we can iterate a tuple

person = ("Jane", 30, "Data Scientist", "Deutschland")
for field in person:
    print(field)    
    
#iterating a string    
text = "Hello, World!"
for character in text:
    print(character)
    
#iterating a number by the range() function
for i in range(10):
    print(i)
    
#break statement example

numbers_break = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7
for number in numbers_break:
    print(f'Processing {number}...')
    if number == target:
        print(f'Target {target} found! Stopping the loop.')
        break
    print(number)
    
#the Continue Statement example
for number in numbers_break:
    if number % 2 == 0:
        continue
    print(f'Odd number: {number}')  

#for loops can have else statements that execute after the loop finishes normally (without a break)
numbers_else = [1, 2, 3, 4, 5]
target_else = 55
for number in numbers_else:
    if number == target_else:
        print(f'Target {target_else} found!')
        break
else:
    print(f'Target {target_else} not found in the list.')
"""an example its if we trying to find a number or a string 
n a list and if we find it we print a message and break the loop, but if we dont find it we print another message after the loop finishes. """


#nested for loops example
for number in range(1, 11):
    for product in range(number, number * 10, number):
        print(f"{product:>4d}", end=" ")
    print()  # Print a newline after each row
    
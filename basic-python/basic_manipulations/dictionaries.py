#Dictionaies are used to store data in key-value pairs. They are mutable and unordered.

printers = {
    "HP": "LaserJet Pro MFP M227fdw",
    "Canon": "PIXMA TR4520",}
print(printers)
printers["Epson"] = "EcoTank ET-4760"

print(printers['HP'])

#The dict() constructor builds dictionaries directly from sequences of key-value pairs:

printers = dict(HP="LaserJet Pro MFP M227fdw", Canon="PIXMA TR4520")
print(printers) 

#Looping Techniques

"""When looping throug a sequence, the position index and corresponding value can be retrieved at the same time using the item() method."""
Knights = {'Aragorn': 'Strider', 'Legolas': 'Greenleaf', 'Gimli': 'Son of Gloin'}
for k, v in Knights.items():
    print(k, v)

"""When looping throug a sequence, the position index and corresponding value can be retrieved at the same time using the enumerate() method."""
for k, v in enumerate(['tic', 'tac', 'toe']):
    print(k, v)
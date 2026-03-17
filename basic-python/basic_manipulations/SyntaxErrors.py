"""!Erros and Exceptions!
Until now error messagens haven't been more than mentioned,
but if you have tried out the examples you have problably seen some.
There are(at least) two distinguishable types of errors in Python:
- Syntax Errors:"""

#1. The Missing Colon (:)

while True print("Hello, World!")
#File "<stdin>", line 6
while True print("SyntaxError: invalid syntax")

    #SyntaxError: Invalid syntax 
      ^

# 2. Misplaced or Missing Quotes
#This happens when you start a string with one type of quote and end it with another, or forget to close it entirely.
print("Hello World') # Mixed " and '
# OR
print("Hello World)  # Missing end quote

#3. Invalid Variable Names
2nd_place = "Silver"


#Mistake	          Error Type	         Why?
#1st_place = 10	      SyntaxError	         Variable names cannot start with numbers.
#my-var = 5	          SyntaxError	         Hyphens are interpreted as subtraction.
#print(xyz)	          NameError            	 xyz was never assigned a value.
#pass = True	      SyntaxError	         pass is a reserved Python keyword."""


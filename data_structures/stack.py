"""
Basic operations of Stack
Push: add an element to the top of a stack
Pop: remove an element from the top of the stack
isEmpty: check if the stack is empty
isFull: check if the stack is full
Peel: Get the value of the top element without removing it"""

#creating a stack
def create_stack():
    stack = []
    return stack

#checking if the stack is empty
def check_empty(stack):
    return len(stack) == 0

# adding items into the stack
def push(stack, item):
    stack.append(item)
    print("pushed item:" + item)


# Removing an element from the stack    
def pop(stack):
    if(check_empty(stack)):
        return ("stack is empty ")
    
    return stack.pop()

stack = create_stack()
push(stack, str(1))
push(stack, str(2))
push(stack, str(3))
push(stack, str(4))

print("poped item: "+ pop(stack))
print("stack after popping and element: "+ str(stack))

"""Stack Time complexity
For the array-based implementation of a stack, the push and pop operations
take constant time, i.e.0(1)"""
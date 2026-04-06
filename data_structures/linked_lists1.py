"""LINKED LISTS are a lesser-known cousin of lists. they're not as popular or as cool,
and you might not even remember them from your algorithms class. But in the right context, they 
can really shine."""

"""How to create a linked list
first  things first, create a class to represent your linked list:
"""

class LinkedList:
    def __init__(self):
        self.head = None

"""The only information you need to store for a linked list is where the list starts(the head
of the list).)"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
"""In the above class definition, you can see the two main elements of every single node: data
and next. You can also add a __repr__ to both classes to have a more helpful representation of the objects:"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __repr__(self):
        return self.data
    
class LinkedList:
    def __init__(self):
        self.head = None
        
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
    
    
    
"""Have a look at an example of using the above classes to quickly create a linked list with three nodes:"""

llist = LinkedList()

first_node = Node("A")

llist.head = first_node

second_node = Node("B")
third_node = Node("C")

first_node.next = second_node
second_node.next = third_node
print(llist)

"""By defning nodes data's data and next values, you can create a linked list quite quickly.
these LinkedList and Node classes are the starting points for our implementation. From now on,
it's all about increasing their functionality."""

def __init__(self, nodes=None):
    self.head = None
    if nodes is not None:
        node = Node(data=nodes.pop(0))
        self.head = node
        for elem in nodes:
            node.next = Node(data=elem)
            node = node.next
            
"""With the above modification, creating linked lists to use in the examples below will be much faster"""

"""!HOW TO  TRAVERSE A LINKED LIST!

One of the common things you will do with a linked list is to traverse it. Traversing means
going through every single node, starting the head of the linked list and ending  on the
node that has a next value of None."""

def __iter__(self):
    node = self.head
    while node is not None:
        yield node
        node = node.next

"""The method above goes through every the list and yields every single node.
the most important thing to remember about this __iter__ is taht you need to always validate that the current
node is not None. When that condition is True, it means you've reached the end of your linked list."""


llist = LinkedList(["A", "B", "C", "D"])
print(llist)


for node in llist:
    print(node)
"""How to insert a new Node
There are different ways to inser new nodes into a linked lists, each with its own
implementation and level of complexity. That's why you'll see them split into specific
methods for inserting at the beginning, end, or between nodes of a list."""

"""Inserting a new node at the beginning of a list is probably the most straightforward insertion
since you don't have to traverse the whole list to do it. it's all about creating a new node and the pointing
the head of the list to it."""

from xml.dom import Node

from data_structures.linked_lists1 import LinkedList


from data_structures.linked_lists1 import LinkedList


def add_first(self, node):
    node.next = self.head
    self.head = node
    
    
"""Inserting a new node at the end of the list forces you to traverse the whole linked list first and to add 
the new node when you reach the end. You can't just append to the end as you would with a normal list because in a linked list 
you don't know which node is last.

Here's an example implementation of a function for inserting a node to the end of a linked list:"""

def add_last(self, node):
    if self.head is None:
        self.head = node
        return

    for current_node in self:
        pass
    current_node.next = node
    

"""Inserting Between Two Nodes adds yet another layer of a complexity to the linked
list's already complex insertions because there are two different approaches that you can use:

1. Inserting after an existing node
2. Inserting before an existing node"""

def add_after(self, target_node_data, new_node):
    if self.head is None:
        raise Exception("List is empty")
    
    for node in self:
        if node.data == target_node_data:
            new_node.next = node.next
            node.next = new_node
            return
    
    raise Exception("Node with data '%s' not found " % target_node_data)

"""in the above code, you're traversing the linked list looking for the node with data indicating
where you want to insert a new node"""

llist = LinkedList()
llist.add_after("a", Node("b"))

llist = LinkedList(["a", "b", "c", "d"])
print(llist)

#a -> b -> c -> d -> None   

llist.add_after("c", Node("cc"))
print(llist)

#a -> b -> c -> cc -> d -> None

llist.add_after("f", Node("g"))



"""Trying to add_user() on an empty list results in an exception. The same happens when
you try to add after a nonexistent node. Everything else works as expected.

Now, if you want to implement add_before(), then it will look something like this:"""

def add_before(self, target_node_data, new_node):
    if self.head is None:
        raise Exception("List is empty")
    
    if self.head.data == target_node_data:
        return self.add_first(new_node)
    
    prev_node = self.head
    for node in self:
        if node.data == target_node_data:
            prev_node.next = new_node
            new_node.next = node 
            return
        prev_node = node
    
    raise Exception("Node with data '%s' not found " % target_node_data)



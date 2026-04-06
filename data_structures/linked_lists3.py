"""How to Remove a Node
To remove a node from a linked list, you first need to traverse the list until you find the node
you want to remove. Once you find the target, you want to link its previous and text nodes.
This re-linking is what removes the target node from the list.

That means you need to keep track of the previous node as you travers the list. have a look at an example implementation
"""

def remove_node(self, head, target_node_data):
    if self.head is None:
        raise Exception("List is empty")
    
    if self.head.data == target_node_data:
        self.head = self.head.next
        return
    
    previous_node = self.head
    for node in self:
        if node.data == target_node_data:
            previous_node.text = node.next
            return
        previous_node = node
    
    raise Exception("Node with data '%s' not found" % target_node_data)
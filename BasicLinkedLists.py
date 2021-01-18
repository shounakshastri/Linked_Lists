# We will use two classes. One class denotes the Linked List and the other class 
# denotes the node.

class LinkedList:
    def __init__(self):
        self.head = None
    
    # __repr__ is used to display objects of a class in a human readable format.
    # This section of both classes is optional and is simply used for explanation
    # purposes.

    def __repr__(self): # Optional
        node = self.head
        nodes = []
        while node is not None:
             nodes.append(node.data)
             node = node.next
        nodes.append("None")
        return " -> ".join(nodes) # This will display the linkedlist as a -> b -> None


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self): # Optional
        return self.data

llist = LinkedList()
print(llist) # o/p => None

first_node = Node("a")
llist.head = first_node
print(llist) # o/p => a -> None

second_node = Node("b")
first_node.next = second_node
third_node = Node("c")
second_node.next = third_node
print(llist) # o/p => a -> b -> c -> None
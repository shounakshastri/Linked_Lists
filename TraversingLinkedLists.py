class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, nodes = None):
        self.head = None
        if nodes is not None:
            node = Node(data = nodes.pop(0))
            self.head = node
            for ii in nodes:
                node.next = Node(data = ii)
                node = node.next
    def __repr__(self): # Optional
        node = self.head
        nodes = []
        while node is not None:
             nodes.append(node.data)
             node = node.next
        nodes.append("None")
        return " -> ".join(nodes) # This will display the linkedlist as a -> b -> None

    # Here we will add an iterable method which will help us define linkedlists like normal lists.
    # Check this li nke for the explanation of "yield" -> https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

# Now we will create the LinkedList like a normal list.

llist = LinkedList(["a", "b", "c", "d", "e"])
print(llist) # o/p => a -> b -> c -> d -> e -> None

for ii in llist:
    print(ii)

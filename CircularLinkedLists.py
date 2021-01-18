# Application of a circular linked list include:
# 
# Going around each player’s turn in a multiplayer game
# Managing the application life cycle of a given operating system
# Implementing a Fibonacci heap

# Can start traversing the list from any node. Also high chance of entering an infinite loop if the stopping
# condition is not nmentioned.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class circularLinkedList:
    def __init__(self):
        self.head = None
    
    def traverse(self, starting_point = None):
        if starting_point == None: starting_point = self.head

        node = starting_point
        while node is not None and (node.next != starting_point):
            yield node
            node = node.next
        yield node

    def print_list(self, starting_point = None):
        nodes = []
        for node in self.traverse(starting_point):
            nodes.append(node.data)
        return " -> ".join(nodes)

cllist = circularLinkedList()
cllist.print_list()

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
a.next = b
b.next = c
c.next = d
d.next = a
#cllist.head = a
print(cllist.print_list(a))
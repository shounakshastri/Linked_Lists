# Here we will optimize the code to include the Node class in the Linkedlist class

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, nodes = None):
        self.head = None
        if nodes is not None:
            node = Node(data = nodes.pop[0])
            self.head = node
            for ii in nodes:
                node.next = Node(data = ii)
                node = node.next

# This code is faster to execute as compared to the code in BasicLinkedlists.py


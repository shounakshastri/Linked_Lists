class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

# Everythong else is the same as singly linked lists.
# Doubly linked lists are used as to implement the Collections.deque (pronounced: deck) which helps it insert or delete an elements from both ends of the queue with
# constant O(1) performance.
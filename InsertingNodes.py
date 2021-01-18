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

    def add_at_beginning(self, node):
        node.next = self.head
        self.head = node

    def add_at_end(self, node):
        if not self.head:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

    # Inserting between two nodes

    def add_after(self, target_node_data, new_node):
        if not self.head:
            raise Exception("List is empty!")
        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return
        raise Exception("Node with data '%s' not found" % target_node_data)

    def add_before(self, target_node_data, new_node):
        if not self.head:
            raise Exception("List is empty!")
        
        # if the target_data is the foirst element in the list, then we can reuse our previous function
        if self.head.data == target_node_data:
            return self.add_at_beginning(new_node)
        
        # if not, then
        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                previous_node.next = new_node
                new_node.next = node
                return
            previous_node = node
        
        raise Exception("Node with '%s' not found" % target_node_data)

    # Removing a node
    def remove_node(self, target_node_data):
        if not self.head:
            raise Exception("List is empty!")

        if self.head.data == target_node_data:
            self.head = self.head.next
            return

        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next
                return
            previous_node = node
        
        raise Exception("Node with '%s' not found" % target_node_data)



llist = LinkedList(["c", "d", "f"])
print(llist)

llist.add_at_beginning(Node("b"))
print(llist)

llist.add_at_beginning(Node("a"))
print(llist)

llist.add_at_end(Node("g"))
print(llist)

llist.add_at_end(Node("h"))
print(llist)

llist.add_after("d", Node("e"))
print(llist)

llist.add_before("d", Node("p"))
print(llist)

llist.remove_node("p")
print(llist)
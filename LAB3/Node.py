class Node:
    def __init__(self, filename, id):
        self.filename = filename
        self.next = None  # the pointer initially points to nothing
        self.id = id

    def traverse(self):
        node = self  # start from the head node
        while node is not None:
            print(node.val)  # access the node value
            node = node.next  # move on to the next node

    def get_id(self):
        return self.id

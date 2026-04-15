class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

def count_nodes(head):
    count = 0
    curr = head

    
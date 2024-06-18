class Node:
    def __init__(self, data):
        """Initialize a node with data and next pointer as None."""
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        """Initialize an empty linked list."""
        self.head = None

    def append(self, data):
        """Append a new node with the given data to the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        """Print the linked list in a readable format."""
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("null")

    def search(self, key):
        """Search for a node with the given key in the list."""
        current_node = self.head
        while current_node:
            if current_node.data == key:
                return True
            current_node = current_node.next
        return False

# Create a linked list and add nodes
linked_list = LinkedList()
linked_list.append(3)
linked_list.append(5)
linked_list.append(13)
linked_list.append(2)

# Print the linked list
linked_list.print_list()

# Search for a node in the linked list
key_to_search = 13
if linked_list.search(key_to_search):
    print(f"Node with data {key_to_search} found.")
else:
    print(f"Node with data {key_to_search} not found.")

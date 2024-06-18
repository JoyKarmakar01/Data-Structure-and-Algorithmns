class Node:
    def __init__(self, data=None):
        """Initialize a node with data and next pointer as None."""
        self.data = data
        self.next = None

class HeaderLinkedList:
    def __init__(self):
        """Initialize an empty header linked list with a header node."""
        self.header = Node()  # The header node does not contain meaningful data.

    def traverse(self):
        """Access each element of the header linked list."""
        elements = []
        current_node = self.header.next  # Start with the first actual element
        while current_node:
            elements.append(current_node.data)
            current_node = current_node.next
        return elements

    def insert(self, data, position=None):
        """Insert a new node with the given data at the specified position."""
        new_node = Node(data)
        current_node = self.header
        current_position = 0
        while current_node.next and (position is None or current_position < position):
            current_node = current_node.next
            current_position += 1
        new_node.next = current_node.next
        current_node.next = new_node

    def delete(self, data):
        """Delete the first node with the given data."""
        current_node = self.header
        while current_node.next:
            if current_node.next.data == data:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next

    def search(self, key):
        """Search for a node with the given key in the list."""
        current_node = self.header.next  # Start with the first actual element
        while current_node:
            if current_node.data == key:
                return True
            current_node = current_node.next
        return False

    def sort(self):
        """Sort the nodes of the header linked list."""
        if not self.header.next or not self.header.next.next:
            return
        sorted_list = None
        current_node = self.header.next
        while current_node:
            next_node = current_node.next
            sorted_list = self._sorted_insert(sorted_list, current_node)
            current_node = next_node
        self.header.next = sorted_list

    def _sorted_insert(self, head, node):
        """Helper function to insert a node into a sorted header linked list."""
        if not head or node.data < head.data:
            node.next = head
            return node
        else:
            current = head
            while current.next and current.next.data < node.data:
                current = current.next
            node.next = current.next
            current.next = node
        return head

    def print_list(self):
        """Print the header linked list in a readable format."""
        current_node = self.header.next  # Start with the first actual element
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("null")

# Test cases
if __name__ == "__main__":
    # Create a header linked list and add nodes
    header_list = HeaderLinkedList()
    header_list.insert(3)
    header_list.insert(5)
    header_list.insert(13)
    header_list.insert(2)

    # Print the header linked list
    print("Initial list:")
    header_list.print_list()

    # Test traverse method
    print("\nTraversed list:", header_list.traverse())

    # Test insert method
    header_list.insert(1, 0)  # Insert at head (position 0)
    header_list.insert(7, 3)  # Insert at position 3
    print("\nList after insertions:")
    header_list.print_list()

    # Test search method
    key_to_search = 13
    if header_list.search(key_to_search):
        print(f"\nNode with data {key_to_search} found.")
    else:
        print(f"\nNode with data {key_to_search} not found.")

    # Test delete method
    header_list.delete(5)
    print("\nList after deleting 5:")
    header_list.print_list()

    # Test sort method
    header_list.sort()
    print("\nList after sorting:")
    header_list.print_list()

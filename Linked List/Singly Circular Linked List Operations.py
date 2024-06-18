class Node:
    def __init__(self, data):
        """Initialize a node with data and next pointer as None."""
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        """Initialize an empty circular linked list."""
        self.head = None

    def traverse(self):
        """Access each element of the circular linked list."""
        elements = []
        if not self.head:
            return elements
        current_node = self.head
        while True:
            elements.append(current_node.data)
            current_node = current_node.next
            if current_node == self.head:
                break
        return elements

    def insert(self, data, position=None):
        """Insert a new node with the given data at the specified position."""
        new_node = Node(data)
        if not self.head:
            new_node.next = new_node
            self.head = new_node
            return
        if position is None or position == 0:
            new_node.next = self.head
            current_node = self.head
            while current_node.next != self.head:
                current_node = current_node.next
            current_node.next = new_node
            self.head = new_node
            return
        current_node = self.head
        current_position = 0
        while current_node.next != self.head and current_position < position - 1:
            current_node = current_node.next
            current_position += 1
        new_node.next = current_node.next
        current_node.next = new_node

    def delete(self, data):
        """Delete the first node with the given data."""
        if not self.head:
            return
        if self.head.data == data:
            if self.head.next == self.head:
                self.head = None
                return
            current_node = self.head
            while current_node.next != self.head:
                current_node = current_node.next
            current_node.next = self.head.next
            self.head = self.head.next
            return
        current_node = self.head
        while current_node.next != self.head:
            if current_node.next.data == data:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next

    def search(self, key):
        """Search for a node with the given key in the list."""
        if not self.head:
            return False
        current_node = self.head
        while True:
            if current_node.data == key:
                return True
            current_node = current_node.next
            if current_node == self.head:
                break
        return False

    def sort(self):
        """Sort the nodes of the circular linked list."""
        if not self.head or self.head.next == self.head:
            return
        sorted_list = None
        current_node = self.head
        start = self.head
        while True:
            next_node = current_node.next
            sorted_list = self._sorted_insert(sorted_list, current_node)
            current_node = next_node
            if current_node == start:
                break
        self.head = sorted_list
        current_node = self.head
        while current_node.next != self.head:
            current_node = current_node.next
        current_node.next = self.head

    def _sorted_insert(self, head, node):
        """Helper function to insert a node into a sorted circular linked list."""
        if not head:
            node.next = node
            return node
        if node.data < head.data:
            current = head
            while current.next != head:
                current = current.next
            current.next = node
            node.next = head
            return node
        current = head
        while current.next != head and current.next.data < node.data:
            current = current.next
        node.next = current.next
        current.next = node
        return head

    def print_list(self):
        """Print the circular linked list in a readable format."""
        if not self.head:
            print("null")
            return
        current_node = self.head
        while True:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
            if current_node == self.head:
                break
        print("head")

# Test cases
if __name__ == "__main__":
    # Create a circular linked list and add nodes
    circular_list = CircularLinkedList()
    circular_list.insert(3)
    circular_list.insert(5)
    circular_list.insert(13)
    circular_list.insert(2)

    # Print the circular linked list
    print("Initial list:")
    circular_list.print_list()

    # Test traverse method
    print("\nTraversed list:", circular_list.traverse())

    # Test insert method
    circular_list.insert(1, 0)  # Insert at head
    circular_list.insert(7, 3)  # Insert at position 3
    print("\nList after insertions:")
    circular_list.print_list()

    # Test search method
    key_to_search = 13
    if circular_list.search(key_to_search):
        print(f"\nNode with data {key_to_search} found.")
    else:
        print(f"\nNode with data {key_to_search} not found.")

    # Test delete method
    circular_list.delete(5)
    print("\nList after deleting 5:")
    circular_list.print_list()

    # Test sort method
    circular_list.sort()
    print("\nList after sorting:")
    circular_list.print_list()

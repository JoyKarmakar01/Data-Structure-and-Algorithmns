class Node:
    def __init__(self, data):
        """Initialize a node with data, next, and prev pointers as None."""
        self.data = data
        self.next = None
        self.prev = None

class DoublyCircularLinkedList:
    def __init__(self):
        """Initialize an empty doubly circular linked list."""
        self.head = None

    def traverse(self):
        """Access each element of the doubly circular linked list."""
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
            new_node.prev = new_node
            self.head = new_node
            return
        if position is None or position == 0:
            new_node.next = self.head
            new_node.prev = self.head.prev
            self.head.prev.next = new_node
            self.head.prev = new_node
            self.head = new_node
            return
        current_node = self.head
        current_position = 0
        while current_node.next != self.head and current_position < position - 1:
            current_node = current_node.next
            current_position += 1
        new_node.next = current_node.next
        new_node.prev = current_node
        current_node.next.prev = new_node
        current_node.next = new_node

    def delete(self, data):
        """Delete the first node with the given data."""
        if not self.head:
            return
        current_node = self.head
        while True:
            if current_node.data == data:
                if current_node.next == current_node:
                    self.head = None
                    return
                current_node.prev.next = current_node.next
                current_node.next.prev = current_node.prev
                if current_node == self.head:
                    self.head = current_node.next
                return
            current_node = current_node.next
            if current_node == self.head:
                break

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
        """Sort the nodes of the doubly circular linked list."""
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
        while current_node.next != sorted_list:
            current_node = current_node.next
        current_node.next = self.head
        self.head.prev = current_node

    def _sorted_insert(self, head, node):
        """Helper function to insert a node into a sorted doubly circular linked list."""
        if not head:
            node.next = node
            node.prev = node
            return node
        if node.data < head.data:
            node.next = head
            node.prev = head.prev
            head.prev.next = node
            head.prev = node
            return node
        current = head
        while current.next != head and current.next.data < node.data:
            current = current.next
        node.next = current.next
        node.prev = current
        current.next.prev = node
        current.next = node
        return head

    def print_list(self):
        """Print the doubly circular linked list in a readable format."""
        if not self.head:
            print("null")
            return
        current_node = self.head
        while True:
            print(current_node.data, end=" <-> ")
            current_node = current_node.next
            if current_node == self.head:
                break
        print("head")

# Test cases
if __name__ == "__main__":
    # Create a doubly circular linked list and add nodes
    circular_list = DoublyCircularLinkedList()
    circular_list.insert(3)
    circular_list.insert(5)
    circular_list.insert(13)
    circular_list.insert(2)

    # Print the doubly circular linked list
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

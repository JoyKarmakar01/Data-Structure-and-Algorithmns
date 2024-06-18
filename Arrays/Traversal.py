def traverse_array(arr):
    """
    Traverses the array and prints each element.

    Parameters:
    arr (list): The array to traverse.
    """
    for index, element in enumerate(arr):
        print(f"Element at index {index}: {element}")

# Example usage
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print("Traversing the array:")
    traverse_array(arr)


# Test cases
def test_traverse_array():
    print("Test Case 1:")
    traverse_array([1, 2, 3])  # Should print elements with indices 0, 1, 2
    
    print("\nTest Case 2:")
    traverse_array([10, 20, 30, 40])  # Should print elements with indices 0, 1, 2, 3
    
    print("\nTest Case 3:")
    traverse_array([])  # Should not print anything (empty array)
    
    print("\nTest Case 4:")
    traverse_array([5])  # Should print the single element with index 0

# Run tests
test_traverse_array()






































# import array
# arr = array.array('i', [1, 2, 3, 4, 5])
# # Traversing over arr[]
# for x in arr:
#     print(x, end=" ")
def insert_element(arr, position, element):
    """
    Inserts an element into the array at the specified position.

    Parameters:
    arr (list): The array to insert the element into.
    position (int): The position to insert the element at (0-based index).
    element: The element to insert.

    Returns:
    list: The array with the element inserted.
    """
    if position < 0 or position > len(arr):
        raise IndexError("Position out of range")

    arr.insert(position, element)
    return arr

# Example usage
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print("Original array:", arr)

    # Insert element 10 at position 2
    position = 2
    element = 10
    arr = insert_element(arr, position, element)
    print(f"Array after inserting {element} at position {position}:", arr)

# Test cases
def test_insert_element():
    assert insert_element([1, 2, 3], 0, 10) == [10, 1, 2, 3], "Test case 1 failed"
    assert insert_element([1, 2, 3], 3, 10) == [1, 2, 3, 10], "Test case 2 failed"
    assert insert_element([1, 2, 3], 1, 10) == [1, 10, 2, 3], "Test case 3 failed"
    assert insert_element([], 0, 10) == [10], "Test case 4 failed"
    
    print("All test cases passed!")

# Run tests
test_insert_element()

def delete_element(arr, position):
    """
    Deletes an element from the array at the specified position.

    Parameters:
    arr (list): The array to delete the element from.
    position (int): The position to delete the element from (0-based index).

    Returns:
    list: The array with the element deleted.
    """
    if position < 0 or position >= len(arr):
        raise IndexError("Position out of range")

    # Delete the element at the specified position
    del arr[position]
    
    return arr

# Example usage
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print("Original array:", arr)

    # Delete element at position 2
    position = 2
    arr = delete_element(arr, position)
    print(f"Array after deleting element at position {position}:", arr)


# Test cases
def test_delete_element():
    assert delete_element([1, 2, 3], 0) == [2, 3], "Test case 1 failed"
    assert delete_element([1, 2, 3], 2) == [1, 2], "Test case 2 failed"
    assert delete_element([1, 2, 3], 1) == [1, 3], "Test case 3 failed"
    assert delete_element([10], 0) == [], "Test case 4 failed"
    
    print("All test cases passed!")

# Run tests
test_delete_element()

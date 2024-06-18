def linear_search(arr, target):
    """
    Performs a linear search to find the target element in the array.

    Parameters:
    arr (list): The array to search through.
    target: The element to search for.

    Returns:
    int: The index of the target element if found, otherwise -1.
    """
    for index, element in enumerate(arr):
        if element == target:
            return index
    return -1

# Example usage of linear search
if __name__ == "__main__":
    arr = [4, 2, 3, 1, 5]
    target = 3
    result = linear_search(arr, target)
    if result != -1:
        print(f"Element {target} found at index {result} using linear search.")
    else:
        print(f"Element {target} not found using linear search.")


# Test cases
def test_search_functions():
    # Linear Search Test Cases
    print("Linear Search Test Cases:")
    print(linear_search([4, 2, 3, 1, 5], 3) == 2)  # Expected output: 2
    print(linear_search([4, 2, 3, 1, 5], 6) == -1)  # Expected output: -1

# Run tests
test_search_functions()
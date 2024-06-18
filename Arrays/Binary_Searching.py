def binary_search(arr, target):
    """
    Performs a binary search to find the target element in the sorted array.

    Parameters:
    arr (list): The sorted array to search through.
    target: The element to search for.

    Returns:
    int: The index of the target element if found, otherwise -1.
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Example usage of binary search
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    target = 3
    result = binary_search(arr, target)
    if result != -1:
        print(f"Element {target} found at index {result} using binary search.")
    else:
        print(f"Element {target} not found using binary search.")


# Test cases
def test_search_functions():
    # Binary Search Test Cases (array must be sorted)
    print("\nBinary Search Test Cases:")
    print(binary_search([1, 2, 3, 4, 5], 3) == 2)  # Expected output: 2
    print(binary_search([1, 2, 3, 4, 5], 6) == -1)  # Expected output: -1

# Run tests
test_search_functions()

def bitonic_sort(arr, up=True):
    if len(arr) <= 1:
        return arr
    first = bitonic_sort(arr[:len(arr) // 2], True)
    second = bitonic_sort(arr[len(arr) // 2:], False)
    return _bitonic_merge(first + second, up)

def _bitonic_merge(arr, up):
    if len(arr) == 1:
        return arr
    _bitonic_compare(arr, up)
    first = _bitonic_merge(arr[:len(arr) // 2], up)
    second = _bitonic_merge(arr[len(arr) // 2:], up)
    return first + second

def _bitonic_compare(arr, up):
    dist = len(arr) // 2
    for i in range(dist):
        if (arr[i] > arr[i + dist]) == up:
            arr[i], arr[i + dist] = arr[i + dist], arr[i]

# Example usage
arr = [3, 7, 4, 8, 6, 2, 1, 5]
print("Sorted array is:", bitonic_sort(arr))

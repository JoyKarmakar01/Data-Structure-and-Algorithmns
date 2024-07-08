# 📚 Sorting Algorithms in Data Structures 📚

Welcome to the comprehensive guide on sorting algorithms! Below, you'll find definitions, pros, cons, and step-by-step approaches for various sorting algorithms. Let's dive in! 🏊‍♂️

## 📋 Contents
1. [Bubble Sort](#1_Bubble_Sort.py)
2. [Selection Sort](#2_Selection_Sort.py)
3. [Insertion Sort](#3_Insertion_Sort.py)
4. [Merge Sort](#4_Merge_Sort.py)
5. [Quick Sort](#5_Quick_Sort.py)
6. [Heap Sort](#6_Heap_Sort.py)
7. [Radix Sort](#7_Radix_Sort.py)
8. [Bucket Sort](#8_Bucket_Sort.py)
9. [Shell Sort](#9_Shell_Sort.py)
10. [Counting Sort](#10_Counting_Sort.py)
11. [Tim Sort](#11_Tim_Sort.py)
12. [Comb Sort](#12_Comb_Sort.py)
13. [Pigeonhole Sort](#13_Pigeonhole_Sort.py)
14. [Cycle Sort](#14_Cycle_Sort.py)
15. [Cocktail Shaker Sort](#15_Cocktail_Shaker_Sort.py)
16. [Gnome Sort](#16_Gnome_Sort.py)
17. [Bitonic Sort](#17_Bitonic_Sort.py)
18. [Odd-Even Sort](#18_Odd-Even_Sort.py)
19. [Pancake Sort](#19_Pancake_Sort.py)
20. [Strand Sort](#20_Strand_Sort.py)

---

## 🔵 Bubble Sort

### Definition
Bubble Sort is a simple comparison-based sorting algorithm. It repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.

### Pros
- Easy to implement 🤓
- Stable sort 🛡️

### Cons
- Inefficient on large lists 🐢
- High time complexity (O(n^2)) ⏳

### Step-by-Step Approach
1. Compare each pair of adjacent elements.
2. Swap them if they are in the wrong order.
3. Repeat until the list is sorted.

---

## 🔍 Selection Sort

### Definition
Selection Sort is an in-place comparison-based algorithm. It divides the input list into two parts: the sorted part and the unsorted part. It repeatedly selects the smallest (or largest) element from the unsorted part and moves it to the sorted part.

### Pros
- Simple to understand 🧠
- No additional memory required 🗂️

### Cons
- Not stable 😕
- Inefficient for large lists 🐢

### Step-by-Step Approach
1. Find the minimum element in the unsorted part.
2. Swap it with the first unsorted element.
3. Move the boundary between sorted and unsorted parts one element to the right.
4. Repeat until the entire list is sorted.

---

## 🖊️ Insertion Sort

### Definition
Insertion Sort is a simple sorting algorithm that builds the final sorted array one item at a time. It is much less efficient on large lists compared to more advanced algorithms such as quicksort, heapsort, or merge sort.

### Pros
- Efficient for small datasets 🌱
- Stable sort 🛡️

### Cons
- Inefficient on large lists 🐢
- High time complexity (O(n^2)) ⏳

### Step-by-Step Approach
1. Iterate from the second element to the end of the list.
2. Compare the current element with the previous elements.
3. Shift elements to the right to make room for the current element.
4. Insert the current element in its correct position.

---

## 🔄 Merge Sort

### Definition
Merge Sort is an efficient, stable, comparison-based, divide and conquer sorting algorithm. Most implementations produce a stable sort, meaning that the order of equal elements is the same in the input and output.

### Pros
- Stable sort 🛡️
- Efficient for large datasets 🚀
- Time complexity: O(n log n) ⏱️

### Cons
- Requires additional memory for temporary arrays 🧮
- Slower for small datasets compared to algorithms like quicksort 🐢

### Step-by-Step Approach
1. Divide the list into two halves.
2. Recursively sort each half.
3. Merge the two sorted halves into a single sorted list.

---

## ⚡ Quick Sort

### Definition
Quick Sort is an efficient, in-place, comparison-based sorting algorithm. It works by selecting a 'pivot' element and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot.

### Pros
- Efficient for large datasets 🚀
- In-place sort (no additional memory required) 🗂️
- Time complexity: O(n log n) on average ⏱️

### Cons
- Not stable 😕
- Worst-case time complexity: O(n^2) ⏳

### Step-by-Step Approach
1. Select a pivot element.
2. Partition the list into two sub-lists: elements less than the pivot and elements greater than the pivot.
3. Recursively sort the sub-lists.
4. Combine the sorted sub-lists and the pivot into a single sorted list.

---

## 🏰 Heap Sort

### Definition
Heap Sort is a comparison-based sorting algorithm that uses a binary heap data structure. It's similar to selection sort, but it uses a priority queue to find the maximum element efficiently.

### Pros
- Time complexity: O(n log n) ⏱️
- In-place sort 🗂️

### Cons
- Not stable 😕
- More complex to implement compared to simple algorithms 🧩

### Step-by-Step Approach
1. Build a max heap from the input data.
2. Remove the largest element (the root) and place it at the end of the list.
3. Reduce the size of the heap by one and heapify the root element.
4. Repeat until all elements are sorted.

---

## 🌈 Radix Sort

### Definition
Radix Sort is a non-comparative sorting algorithm. It sorts the elements by processing individual digits. It processes each digit either starting from the least significant digit (LSD) or the most significant digit (MSD).

### Pros
- Linear time complexity: O(nk) where k is the number of digits ⏱️
- Suitable for large datasets 🚀

### Cons
- Not a comparison sort 😕
- Requires additional memory 🧮

### Step-by-Step Approach
1. Find the maximum number to know the number of digits.
2. Iterate through each digit.
3. Sort elements based on the current digit using counting sort.
4. Repeat until all digits are processed.

---

## 🪣 Bucket Sort

### Definition
Bucket Sort is a sorting algorithm that works by distributing the elements into a number of buckets. Each bucket is then sorted individually, either using a different sorting algorithm or recursively applying the bucket sort.

### Pros
- Efficient for uniformly distributed data 🌍
- Linear time complexity: O(n + k) where k is the number of buckets ⏱️

### Cons
- Not suitable for large range of values 😕
- Requires additional memory for buckets 🧮

### Step-by-Step Approach
1. Create an empty array of buckets.
2. Distribute the elements into buckets based on their values.
3. Sort each bucket.
4. Concatenate all buckets to form the sorted list.

---

## 🐚 Shell Sort

### Definition
Shell Sort is an in-place comparison sort. It is a generalization of insertion sort that allows the exchange of items that are far apart.

### Pros
- More efficient than insertion sort for large datasets 🚀
- Simple implementation 🧠

### Cons
- More complex to understand compared to insertion sort 🧩
- Time complexity: O(n^2) in the worst case ⏳

### Step-by-Step Approach
1. Choose a gap sequence.
2. Perform a gapped insertion sort for each gap.
3. Reduce the gap and repeat until the gap is 1.

---

## 📏 Counting Sort

### Definition
Counting Sort is an integer sorting algorithm. It operates by counting the number of objects that have distinct key values, and using arithmetic to determine the positions of each key.

### Pros
- Linear time complexity: O(n + k) where k is the range of input ⏱️
- Efficient for small ranges of integers 🌱

### Cons
- Not suitable for large ranges of values 😕
- Requires additional memory for the count array 🧮

### Step-by-Step Approach
1. Find the maximum element in the input list.
2. Initialize a count array of size max+1.
3. Count the occurrences of each element.
4. Modify the count array by adding the previous counts.
5. Build the output array by placing elements at their correct positions.

---

## 🕰️ Tim Sort

### Definition
Tim Sort is a hybrid sorting algorithm derived from merge sort and insertion sort. It is used in Java's Arrays.sort() as well as Python's sorted() and sort().

### Pros
- Efficient for real-world data 🚀
- Stable sort 🛡️
- Time complexity: O(n log n) ⏱️

### Cons
- Requires additional memory for temporary arrays 🧮
- More complex to implement compared to simple algorithms 🧩

### Step-by-Step Approach
1. Divide the list into small segments.
2. Sort each segment using insertion sort.
3. Merge the sorted segments using merge sort.

---

## 🔀 Comb Sort

### Definition
Comb Sort is an improvement over bubble sort. It eliminates turtles, or small values near the end of the list, by using a gap value greater than 1.

### Pros
- More efficient than bubble sort 🚀
- Simple to implement 🧠

### Cons
- Not stable 😕
- Inefficient compared to advanced algorithms 🐢

### Step-by-Step Approach
1. Initialize the gap size to the list length.
2. Reduce the gap size using the shrink factor (usually 1.3).
3. Perform a bubble sort with the current gap size.
4. Repeat until the gap size is 1 and the list is sorted.

---

## 🕊️ Pigeonhole Sort

### Definition
Pigeonhole Sort is a non-comparison sorting algorithm. It is suitable for sorting lists of elements where the number of possible key values is approximately the same as the number of elements.

### Pros
- Linear time complexity: O(n + range) ⏱️
- Simple to understand and implement 🧠

### Cons
- Not suitable for large ranges of values 😕
- Requires additional memory proportional to the range 🧮

### Step-by-Step Approach
1. Find the minimum and maximum values in the list.
2. Create an array of pigeonholes for each possible key value.
3. Distribute the elements into their respective pigeonholes.
4. Concatenate the elements from the pigeonholes to form the sorted list.

---

## 🔄 Cycle Sort

### Definition
Cycle Sort is an in-place, unstable sorting algorithm. It is optimal in terms of the total number of writes to the original array and is useful when memory writes are costly.

### Pros
- Minimizes the number of memory writes 📝
- Time complexity: O(n^2) ⏱️

### Cons
- Not stable 😕
- Inefficient for large datasets 🐢

### Step-by-Step Approach
1. Iterate through the list and determine the correct position of each element.
2. Swap elements to their correct positions.
3. Repeat until all elements are correctly positioned.

---

## 🍹 Cocktail Shaker Sort

### Definition
Cocktail Shaker Sort is a variation of bubble sort. It sorts the list in both directions on each pass through the list.

### Pros
- More efficient than bubble sort 🚀
- Simple to implement 🧠
- Stable sort 🛡️

### Cons
- Inefficient for large datasets 🐢
- Time complexity: O(n^2) ⏱️

### Step-by-Step Approach
1. Pass through the list from left to right, swapping adjacent elements if they are in the wrong order.
2. Pass through the list from right to left, swapping adjacent elements if they are in the wrong order.
3. Repeat until the list is sorted.

---

## 🧝 Gnome Sort

### Definition
Gnome Sort is a simple sorting algorithm similar to insertion sort, but moving elements to their proper place in a manner reminiscent of the way a gnome sorts flower pots.

### Pros
- Simple to understand and implement 🧠
- Stable sort 🛡️

### Cons
- Inefficient for large datasets 🐢
- Time complexity: O(n^2) ⏱️

### Step-by-Step Approach
1. Compare the current element with the previous element.
2. If they are in the wrong order, swap them and move one step backward.
3. If they are in the correct order, move one step forward.
4. Repeat until the list is sorted.

---

## 🔀 Bitonic Sort

### Definition
Bitonic Sort is a parallel algorithm for sorting. It works by recursively sorting two halves of the list in opposite directions and then merging them into a bitonic sequence.

### Pros
- Suitable for parallel processing 🖥️
- Time complexity: O(log^2 n) ⏱️

### Cons
- Not stable 😕
- Requires additional memory for temporary arrays 🧮

### Step-by-Step Approach
1. Divide the list into two halves.
2. Sort one half in ascending order and the other half in descending order.
3. Merge the two halves into a bitonic sequence.
4. Recursively sort the bitonic sequence.

---

## 🔄 Odd-Even Sort

### Definition
Odd-Even Sort, also known as Brick Sort, is a parallel version of bubble sort. It compares and swaps adjacent elements in alternating phases.

### Pros
- Simple to implement 🧠
- Suitable for parallel processing 🖥️

### Cons
- Inefficient for large datasets 🐢
- Time complexity: O(n^2) ⏱️

### Step-by-Step Approach
1. Compare and swap adjacent elements in the odd phase.
2. Compare and swap adjacent elements in the even phase.
3. Repeat until the list is sorted.

---

## 🥞 Pancake Sort

### Definition
Pancake Sort is a sorting algorithm that sorts a sequence by repeatedly flipping portions of the sequence, similar to flipping pancakes in a stack so the largest pancake ends up at the top.

### Pros
- Simple concept and visualization 🧠
- Useful for educational purposes and understanding the concept of flipping operations 🍽️

### Cons
- Not efficient for large datasets, with a time complexity of O(n^2) in the worst case ⏳
- Not used in practice for large-scale sorting tasks 🚫

### Step-by-Step Approach
1. Identify the largest unsorted element.
2. Flip the stack to move the largest element to the top.
3. Flip the stack again to move the largest element to its correct position.
4. Repeat for the next largest unsorted element until the entire stack is sorted.

---

## 🧵 Strand Sort

### Definition
Strand Sort is a sorting algorithm that works by repeatedly pulling sorted sublists from the original list and merging them into a new sorted list.

### Pros
- Intuitive and easy to understand 🧠
- Can be efficient for certain types of data 🗂️

### Cons
- Not suitable for in-place sorting as it requires extra space for the sorted list 🗃️
- Time complexity can vary, but typically around O(n^2) ⏳

### Step-by-Step Approach
1. Start with an empty list for the sorted result.
2. Extract a sublist from the unsorted list that is already sorted.
3. Merge the sorted sublist into the sorted result list.
4. Repeat the process until the original list is empty.


## 🎉 Conclusion

Sorting algorithms are fundamental in computer science and data structures. Each algorithm has its strengths and weaknesses, making them suitable for different types of datasets and applications. Choose the right algorithm based on your specific needs and constraints! 🚀

Feel free to reach out for any questions or contributions! 🌟
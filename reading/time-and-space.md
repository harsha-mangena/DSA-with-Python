# Time and Space Complexity Guide

This README provides an overview of time and space complexities, crucial concepts in algorithm design and analysis. It includes definitions, common complexities, and Python code examples to help understand how these complexities affect algorithm performance.

## Table of Contents
- [Time Complexity](#time-complexity)
- [Space Complexity](#space-complexity)

## Time Complexity

Time complexity refers to the amount of time an algorithm takes to run as a function of the length of the input. It's typically expressed using Big O notation, which provides an upper bound on the time.

### Common Time Complexities

1. **O(1) - Constant Time:**
   - Execution time remains constant, regardless of the input size.
   - *Python Example:* Accessing a specific element in an array.
     ```python
     def get_element(arr, index):
         return arr[index]
     ```

2. **O(log n) - Logarithmic Time:**
   - Execution time increases logarithmically with the input size.
   - *Python Example:* Binary search in a sorted array.
     ```python
     def binary_search(arr, target):
         low, high = 0, len(arr) - 1
         while low <= high:
             mid = (low + high) // 2
             if arr[mid] < target:
                 low = mid + 1
             elif arr[mid] > target:
                 high = mid - 1
             else:
                 return mid
         return -1
     ```

3. **O(n) - Linear Time:**
   - Execution time increases linearly with the input size.
   - *Python Example:* Finding the maximum element in an unsorted array.
     ```python
     def find_max(arr):
         max_value = arr[0]
         for num in arr:
             if num > max_value:
                 max_value = num
         return max_value
     ```

4. **O(n log n) - Linearithmic Time:**
   - Combines linear and logarithmic behavior.
   - *Python Example:* Sorting an array using merge sort.
     ```python
     def merge_sort(arr):
         if len(arr) > 1:
             mid = len(arr) // 2
             L = arr[:mid]
             R = arr[mid:]

             merge_sort(L)
             merge_sort(R)

             i = j = k = 0
             while i < len(L) and j < len(R):
                 if L[i] < R[j]:
                     arr[k] = L[i]
                     i += 1
                 else:
                     arr[k] = R[j]
                     j += 1
                 k += 1

             while i < len(L):
                 arr[k] = L[i]
                 i += 1
                 k += 1

             while j < len(R):
                 arr[k] = R[j]
                 j += 1
                 k += 1
         return arr
     ```

5. **O(n^2) - Quadratic Time:**
   - Execution time is proportional to the square of the input size.
   - *Python Example:* Bubble sort.
     ```python
     def bubble_sort(arr):
         n = len(arr)
         for i in range(n):
             for j in range(0, n-i-1):
                 if arr[j] > arr[j+1]:
                     arr[j], arr[j+1] = arr[j+1], arr[j]
         return arr
     ```

6. **O(2^n) - Exponential Time:**
   - Execution time doubles with each addition to the input data set.
   - *Python Example:* Naive solution for the Fibonacci sequence.
     ```python
     def fibonacci(n):
         if n <= 1:
             return n
         else:
             return fibonacci(n-1) + fibonacci(n-2)
     ```

7. **O(n!) - Factorial Time:**
   - Execution time grows factorially with the input size.
   - *Python Example:* Generating all permutations of a list.
     ```python
     from itertools import permutations

     def generate_permutations(lst):
         return list(permutations(lst))
     ```

## Space Complexity

Space complexity measures the total amount of memory that an algorithm uses relative to the input size. Like time complexity, it's often expressed in Big O notation.

### Common Space Complexities

1. **O(1) - Constant Space:**
   - The algorithm uses a fixed amount of memory space, regardless of the input size.
   - *Python Example:* Swapping two numbers using a temporary variable.
     ```python
     def swap(a, b):
         temp = a
         a = b
         b = temp
         return a, b
     ```

2. **O(n) - Linear Space:**
   - The space required increases linearly with the input size.
   - *Python Example:* Copying elements of an array into a new array.
     ```python
     def copy_array(arr):
         new_arr = arr[:]
         return new_arr
     ```

3. **O(n^2) - Quadratic Space:**
   - Space complexity increases as the square of the input size.
   - *Python Example:* Creating a two-dimensional array (matrix).
     ```python
     def create_matrix(rows, cols):
         return [[0 for _ in range(cols)] for _ in range(rows)]
     ```

     ## Quiz: Test Your Understanding

Test your understanding of time and space complexities with these tricky questions:

1. **Question 1:** What is the time complexity of an algorithm that involves a single loop from 1 to n where within each iteration, a constant-time operation is performed?

2. **Question 2:** Consider a recursive function that splits an array into two halves at each step. What is the time complexity of this function?

3. **Question 3:** What is the space complexity of an iterative Fibonacci sequence implementation?

4. **Question 4:** How does the space complexity change if a recursive algorithm is optimized using memoization?

5. **Question 5:** Given an algorithm that sorts an array using bubble sort, what is its time complexity?

6. **Question 6:** If an algorithm's runtime doubles with each additional element in the input, what is its time complexity?

7. **Question 7:** What is the space complexity of an algorithm that creates a new integer array of size n?

8. **Question 8:** An algorithm involves two nested loops, each running from 1 to n. What is the time complexity of this algorithm?

9. **Question 9:** What time complexity category does binary search belong to?

10. **Question 10:** If an algorithm includes two consecutive loops (not nested) that run from 1 to n, what is its time complexity?



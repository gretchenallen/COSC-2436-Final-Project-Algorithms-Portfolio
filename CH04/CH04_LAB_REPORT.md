# Lab 04: Quicksort

## Student Information
- **Name:** Gretchen Allen
- **Date:** 02/19/2026

## Quicksort Concepts

### Divide and Conquer
Quicksort implements the divide and conquer technique by breaking down a problem such as an unsorted array into smaller and smaller arrays until the base case is reached. After this, all of the sub-solutions are then added back together to solve the original problem.

### The Three Steps
1. **Choose pivot:** Chooses an element from the array which will be compared against all other elements
2. **Partition:** Divides the array into two separate, smaller arrays based on the location of the pivot.
3. **Recurse and combine:** Recursively applies the quicksort algorithm on each of the sub-arrays until they are each sorted, then combines the two halves with the pivot in between to produce the completely sorted array.

## Tracing Quicksort

### Trace: quicksort([3, 5, 2, 1, 4])
Step 1:  [3, 5, 2, 1, 4]
         Pivot: 3
         Less: [2, 1]
         Greater: [5, 4]
         
Step 2:  [2, 1]
         Pivot: 2
         Less: [1]
         Greater: []
         
Step 3:  [1] (Base Case)
         
Step 4:  [] (Base Case)
         
Step 5:  Result of Less: [1, 2]

Step 6:  [5, 4]
         Pivot: 5
         Less: [4]
         Greater: []
         
Step 7:  [4] (Base Case)
         
Step 8:  [] (Base Case)
         
Step 9:  Result of Greater: [4, 5]

Step 10: Final result: [1, 2, 3, 4, 5]

## Complexity Analysis

| Case | Time Complexity | Why? |
|------|----------------|------|
| Best | O(n log n) | The best case occurs when the (randomly chosen) pivot divides the list into two equal halves. When this occurs, it takes O(log n) time to reach the height of the recursion tree, times the "n" number of elements at each level. |
| Average | O(n log n) | Even though the pivot will not divide the list into equal halves every time as in the best case scenario, the statistical average of the random pivots will still result in roughly equal partitions and will run at O(n log n) time similar to best case. |
| Worst | O(n²) | In the worst case scenario the pivot is always the smallest or largest element in the list. This means that only one element will be eliminated with each recursion call, and the height of the recursion tree will be O(n), which is still multiplied by "n" number of elements at each recursion level. |

## Reflection Questions

1. What happens if the array is already sorted and you always pick the first element as pivot?
   It doesn't matter whether the array is already sorted or not; if the first element is always picked this results in the worst-case time complexity of O(n²). 

3. How could you improve pivot selection to avoid worst-case performance?
   There are a few different methods that can be used to improve pivot selection, such as selecting the median of the first, middle, and last elements as pivot, randomly selecting the pivot, or implementing additional algorithms.
   These algorithms could include the "median of medians" algorithm or other sorting algorithms such as quicksort, which would assist in division into small partitions.

5. How does quicksort compare to other sorting algorithms you know (e.g., bubble sort, merge sort)?
   Quicksort and bubble sort have very different uses; while bubble sort is simple and easy to implement, it is not efficient for large datasets with a time complexity of O(n). Quicksort, while being a bit more complicated to implement than bubble sort, is very efficient with datasets of any size and is a practical choice for many applications.
   Quicksort and merge sort both run at O(n log n) time so are both a good choice for larger datasets. Quicksort does generally run a bit faster due to due to lower memory usage and better use of cache. However, merge sort offers higher stability than quicksort and thus a more consistent runtime, with a tradeoff in additional space used. 

7. Why do we use `array[1:]` instead of `array` when building the less and greater lists?
   Doing so avoids including the pivot in the list partitions.

# Lab 3: Recursion

## Student Information
- **Name:** Gretchen Allen
- **Date:** 02/12/2026

## Recursion Concepts

### Two Parts of Every Recursive Function
1. **Base Case:** The condition that stops the recursive calls, returning a specific value directly to prevent infinite loops.
2. **Recursive Case:** 
When the function calls itself with a smaller or simpler input, steering towards the base case.

### The Call Stack
In a function such as fact(x), the call stack works by storing each additional function call as the recursive function calls itself. Once the base case is met, the stack unwinds itself in the order last in first out, returning the values from each function call step by step. 

## Function Analysis

| Function | Base Case | Recursive Case | Time Complexity |
|----------|-----------|----------------|-----------------|
| countdown | i <= 0 | countdown(i-1) | O(n) |
| fact | x <= 1 | x * fact(x-1) | O(n) |
| recursive_sum | empty list | first + sum(rest) | O(n) |
| recursive_count | empty list | 1 + count(rest) | O(n) |
| recursive_max | single item | max(first, max(rest)) | O(n) |

## Reflection Questions

1. What happens if you forget the base case?
The function will continue to call itself indefinitely, resulting in a stack overflow error.

2. Why is the naive Fibonacci implementation inefficient?
It uses a recursive approach without memorization, causing repeated calculations.

3. Draw the call stack for fact(4).
fact(4)
  → 4 * fact(3)
    → 3 * fact(2)
      → 2 * fact(1)   
        → returns 1        ← Base case!
      → returns 2 * 1 = 2
    → returns 3 * 2 = 6
  → returns 4 * 6 = 24

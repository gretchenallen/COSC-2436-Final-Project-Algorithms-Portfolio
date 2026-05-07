# Lab 2: Selection Sort

## Student Information
- **Name:** Gretchen Allen
- **Date:** 02/07/2026

## Algorithm Summary

### Selection Sort
- **Time Complexity:** O(n²)
- **Space Complexity:** O(1)
- **How it works:** Selection sort works by looking at the smallest (or largest, depending on how the list needs to be sorted) element of the unsorted list and swapping it with the first unsorted element. This process is repeated until there are no remaining unsorted elements.

## Array vs Linked List Analysis

| Operation | Array | Linked List | Why? |
|-----------|-------|-------------|------|
| Read      | O(1)  | O(n)        |Arrays          provide random access, linked lists must be accessed sequentially   |
| Insert    | O(n)  | O(1)        |With arrays, everything needs to be shifted when either an insertion or deletion is made.      |
| Delete    | O(n)  | O(1)        | For linked lists, you simply need to change what the previous element points to.     |

## Test Results
Sorting cities by population (smallest first)...
Selection Sort: 190 comparisons, 19 swaps

Top 5 smallest cities:
  McAllen: 142,210
  Pasadena: 151,950
  Killeen: 153,095
  Brownsville: 183,392
  McKinney: 195,308

## Reflection Questions

1. Why is selection sort O(n²)?
In order to sort an entire list, the program must check each item on the list as many times as there are items on the list, or n x n times.

2. When would you choose a linked list over an array?
When frequent insertions and/or deletions are required, such as a first-in, first-out situation like an ordering system at a restaurant.

3. Why does Python use arrays (lists) as the default sequence type?
One main reason for this is the flexibility afforded by python lists in that they are able to dynamically grow and shrink in size as needed. 

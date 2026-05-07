# Chapter 1 Lab Report: Binary Search

## Student Information
- **Name:** Gretchen Allen
- **Date:** 05/07/2026
- **Course:** COSC 2436

## Algorithm Summary

### Linear Search
Linear search works by examining elements in a list one by one until the target item is either found or the end of the list is reached. If the item is found, the algorithm will return the index where that item is located; if the item is not on the list the algorithm returns "none".
The time complexity of linear search is O(n), so in the worst case scenario each item in a list would have to be examined once. Linear search is best used when the list of items is short, as the runtime quickly becomes too high as the size of the list grows.

### Binary Search
Binary search works by dividing a list in half and comparing the middle element to the target element. If it's a match, the index of the element is returned. If not, the algorithm will then search only one half of the list; if the target element is smaller then the smaller half of the list will be checked, and if the target element is larger then the larger half of the list will be checked. This process continues until the target element is either found or there is no more unsearched elements.
The time complexity of binary search is O(log n), making it a very efficient algorithm for large sets of data. However, binary search is only effective on lists of data that are already sorted, which means that if the data needs to first be sorted then the computation runtime for that process must also be taken into account.

## Test Results

Searching in a sorted list of 128 numbers

Searching for: 1
Linear search time: 0.00000238 seconds
Binary search time: 0.00000286 seconds
Linear search result: 0
Binary search result: 0
Binary search is 0.83x faster

Searching for: 64
Linear search time: 0.00000310 seconds
Binary search time: 0.00000072 seconds
Linear search result: 63
Binary search result: 63
Binary search is 4.33x faster

Searching for: 128
Linear search time: 0.00000358 seconds
Binary search time: 0.00000215 seconds
Linear search result: 127
Binary search result: 127
Binary search is 1.67x faster

Searching for: 50
Linear search time: 0.00000215 seconds
Binary search time: 0.00000143 seconds
Linear search result: 49
Binary search result: 49
Binary search is 1.50x faster

Searching for: 100
Linear search time: 0.00000310 seconds
Binary search time: 0.00000167 seconds
Linear search result: 99
Binary search result: 99
Binary search is 1.86x faster

Searching for: 25
Linear search time: 0.00000191 seconds
Binary search time: 0.00000143 seconds
Linear search result: 24
Binary search result: 24
Binary search is 1.33x faster

Searching for: 75
Linear search time: 0.00000238 seconds
Binary search time: 0.00000238 seconds
Linear search result: 74
Binary search result: 74
Binary search is 1.00x faster

Searching for: 10
Linear search time: 0.00000143 seconds
Binary search time: 0.00000143 seconds
Linear search result: 9
Binary search result: 9
Binary search is 1.00x faster

Searching for: 90
Linear search time: 0.00000310 seconds
Binary search time: 0.00000167 seconds
Linear search result: 89
Binary search result: 89
Binary search is 1.86x faster

Searching for: 200
Linear search time: 0.00000358 seconds
Binary search time: 0.00000167 seconds
Linear search result: None
Binary search result: None
Binary search is 2.14x faster

Lab Challenge Answer:
Maximum steps for binary search in 128 items:
log2(128) = 7 steps maximum

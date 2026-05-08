# Lab Report

## Student Information
- **Name:** Gretchen Allen
- **Date:** 05/07/2026

## Key Concepts
- Describe what a hash table is and how it works.
  A hash table is a data structure used for storing key-value pairs. It uses a hash function which turns each key into an index, and stores the key-value pair at that location in an array.
  
- Explain linear probing and its role in handling collisions.
  Linear probing is a distinct method for handling collisions in which the next available slot is found so that the key-value pair can be inserted at that location.

## Tracing Exercise
- Trace through the example where keys 'apple', 'banana', and 'orange' are inserted.
- Show the state of the hash table after each insertion.

  Initial State

All slots are None.

After Inserting "apple"

Compute hash: hash("apple") % 10 -> index 3.

Insert ("apple", 100) at index 3.

 Index | Key-Value
 
  0   | None
  
  1   | None
  
  2   | None 
  
  3   | ("apple", 100) 
  
  4   | None
  
  5   | None
  
  6   | None 
  
  7   | None 
  
  8   | None 
  
  9   | None
  
  After Inserting "banana"
  
Compute hash: hash("banana") % 10 -> index 3 (collision).

Linear probing: Next available slot at index 4.

Insert ("banana", 200) at index 4.

Index | Key-Value

  0   | None
  
  1   | None
  
  2   | None
  
  3   | ("apple", 100)
  
  4   | ("banana", 200)
  
  5   | None
  
  6   | None
  
  7   | None
  
  8   | None
  
  9   | None
  
  After Inserting "orange"
  
Compute hash: hash("orange") % 10 -> index 9.

Insert ("orange", 300) at index 9.

| Index | Key-Value |

|  0   | None |

  1   | None
  
  2   | None
  
  3   | ("apple", 100)
  
  4   | ("banana", 200)
  
  5   | None
  
  6   | None
  
  7   | None
  
  8   | None
  
  9   | ("orange", 300)

## Complexity Analysis
| Operation | Average Case | Worst Case |
|---|---|---|
| Insert | O(1) | O(n) |
| Search | O(1) | O(n) |

## Reflection Questions
1. What are the advantages of using a hash table?
   A hash table provides fast lookups and inserts, both at a constant time complexity or O(1). They can also be dynamically resized, can handle various data types as input, and are able to efficiently handle collisions. 
3. How does the hash function affect the performance of a hash table?
   A hash function that is well-designed will distribute keys evenly throughout the table, which reduces the likelihood that clustering and collisions will occur.
   The hash function should also scale as needed for different table sizes without any significant performance loss.
5. What are other collision resolution techniques besides linear probing?
6. Other techniques include:
7. Quadratic Probing:
Instead of checking the next slot, it checks the slots at increasing quadratic intervals (i.e., 1^2, 2^2, 3^2, etc.).
Double Hashing:
Uses a second hash function to calculate the interval between probes, reducing clustering and improving distribution.
Separate Chaining:
Each index in the hash table array points to a linked list or another data structure. All elements that hash to a particular index are stored in that list.
Cuckoo Hashing:
Uses multiple hash functions and allows a key to be stored in one of several possible locations, relocating existing keys if necessary.

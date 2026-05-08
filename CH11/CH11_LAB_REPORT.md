# Chapter 11: Dynamic Programming — Lab Report

## Student Information
- **Name:** Gretchen Allen
- **Date:** 05/08/2026
- **Course:** COSC 2436

## Algorithm Summary
- **How it works:** Dynamic programming works by breaking a problem into smaller subproblems and finding the optimal solution for each subproblem. Each of these solutions are then added up to find the optimal solution to the bigger problem.
  For a problem such as the knapsack problem, this is usually accomplished using a 2D grid where the rows contain the items to be considered and the columns represent the weight capacity.
- **Time complexity:** O(n*W) where n is the number of items and W is the weight capacity.
- **When to use it:** This algorithm is best used when the number of items and capacity are manageable values since it will not scale well for very large numbers due to its O(n*W) time complexity.
- Scenarios such as resource allocation in project planning with a limited budget, or the maximization of cargo loading in a vehicle with weight constraints are ideal situations in which to use dynamic programming.
  
## Test Results
                   1           2           3           4           5           6
GUITAR          $1500(G)    $1500(G)    $1500(G)    $1500(G)    $1500(G)    $1500(G)
STEREO          $1500(G)    $1500(G)    $1500(G)    $3000(S)   $4500(GS)   $4500(GS)
LAPTOP          $1500(G)    $1500(G)    $2000(L)   $3500(GL)   $4500(GS)   $4500(GS)
iPHONE          $2000(i)   $3500(Gi)   $3500(Gi)   $4000(Li)  $5500(GLi)  $6500(GSi)
BOOK            $2000(i)   $3500(Gi)   $3500(Gi)   $4000(Li)  $5500(GLi)  $6500(GSi)
GOLD BAR       $30000(G)  $32000(iG) $33500(GiG) $33500(GiG) $34000(LiG)$35500(GLiG)


## Reflection Questions

Dynamic programming provides an efficient solution to optimization problems, especially in comparison to methods such as brute force, which examines every item against every other item and results in O(n^2) time complexity.
This algorithm is effective for many types of real-world problems in which optimization under predefined constraints is needed. 

## Challenges Encountered
It was initially difficult to conceptualize that each cell of the 2D grid corresponds to a decision within the algorithm's process. After going over multiple examples of this algorithm in action and observing how the value changes in each step, I was able to correctly implement the code for the decision-making process.

# Lab Report #10 Truck Packing

Student Information
## Name: Gretchen Allen
## Date: 05/01/2026
## Algorithm Analysis: Greedy Truck Packing Algorithm

## Algorithm Understanding
- What type of problem is this algorithm solving?
Optimization problem

- Is this greedy algorithm guaranteed to produce the optimal solution? Why or why not?
No, it is not guaranteed to produce the optimal solution because this algorithm evaluates the best choice at a given moment without considering future implications. This may lead to locally optimal but not globally optimal solutions.

- What is the greedy choice made in this algorithm?
Boxes are selected based on their volume in descending order.

## Implementation Questions
- Why do we sort the boxes in descending order of volume before packing?
By packing the largest boxes first, the available space in the truck is used up as much as possible from the start. Doing this helps avoid leaving large areas of empty space that would not be efficiently used by smaller boxes.

- What would happen if we sorted the boxes in ascending order instead?
The space would not be used as efficiently by starting with smaller boxes first. The available space could become fragmented and larger boxes may not fit later on which would have easily fit in the beginning.

- Why do we keep track of used_volume?
To know whether or not there is still space available in the truck for subsequent boxes.

## Extension: Dimension Constraints
- Why is checking only volume not sufficient for real-world packing?
Many aspects of real-world packing depend on more than just volume, such as the shape, dimensions, and orientation of the boxes.

- Give an example where a box fits by volume but not by dimensions.
You could have a truck that is 12 feet long, 8 feet wide, and 10 feet tall. A box could be 16ft x1ft x3ft, which would not exceed the volume of the truck but would not fit since a dimension of 16 feet is longer than the longest dimension of the truck.

- How would you modify the algorithm to check dimension constraints before packing a box?
Add a function that can check each dimension of each box (length, height, and width), and then integrate this function into the packing logic.

## Reflection Questions
- What is a limitation of this greedy approach? Provide a scenario where it fails to find the optimal solution.
If you had an available volume of 50 cubic units, and boxes A, B, C, and D with volumes 30, 15, 10, and 10 cubic units respectively, the greedy algorithm would select boxes A and B without considering boxes C and D. The greedy approach in this scenario doesn't acknowledge potential combinations that might better utilize the available space.

- How is this problem related to the Knapsack Problem?
Both problems seek to optimize items within a given capacity, except the truck packing problem seeks to optimize volume while the knapsack problem seeks to optimize monetary value. 

- What type of algorithm would guarantee an optimal solution for this problem? What is the tradeoff?
You could utilize dynamic programming for this problem, which would break it down into smaller subproblems and systematically explore different combinations to find the optimal solution. The drawback to dynamic programming is it would become computationally expensive with a large number of boxes and become infeasible to run.

- If the truck had weight limits in addition to volume, how would the algorithm need to change?
The box class would need to be extended to include a weight attribute, which would then need to be included in the packing logic by keeping track of used_weight.

- Why are greedy algorithms often preferred despite not always being optimal?
Greedy algorithms are generally simple to implement and are less computationally intensive, which makes them very scalable for large datasets. In many cases, the "good enough" solution is close enough to optimal that it's worth the speed and ease of implementation.

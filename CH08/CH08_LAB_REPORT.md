## Lab Report #8 Balanced Trees

### Student Information
- **Name:** Gretchen Allen
- **Date:** 4/6/2026

### Algorithm Analysis

#### AVL Trees
- **Balance Factor Range:** The difference between the height of the left subtree and the height of the right subtree, going from -1 to 1.
- **Why rebalance?** If a tree's height on one side becomes skewed in relation to the other side, it loses efficiency in operations like insertion, deletion, and lookup and could cause them to degrade to O(n) time complexity.
- **Time Complexity (all operations):** O(log n)

#### Rotation Cases
| Case | Imbalance | Fix |
|------|-----------|-----|
| LL   | Node becomes left-heavy due to an insertion in the left subtree of its left child.          | Right rotation around unbalanced node    |
| RR   | Node becomes right-heavy due to an insertion in the right subtree of its right child         | Left rotation around unbalanced node    |
| LR   | Node is left-heavy, but the heavy subtree is on the right side of its left child          | Left rotation on left child, followed by a right rotation on the unbalanced node    |
| RL   | Node is right-heavy, but the heavy subtree is on the left side of its right child          | Right rotation on the right child, followed by a left rotation on the unbalanced node    |

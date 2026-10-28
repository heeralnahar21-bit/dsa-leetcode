## 01. Cycle Length in Linked List

The problem can be found at the following link: [Question Link](https://www.geeksforgeeks.org/problems/find-length-of-loop/1)

### Problem Description

**Task:** Given the head of a linked list. A linked list contains a cycle if its last node is connected to a previous node. If the given list contains a cycle, return the length of the cycle. Otherwise, return 0.

> **Note:** Internally, the driver code uses an integer x to represent the position (1-based indexing) of the node to which the last node is connected. If x = 0, it means last node points to null which indicating there is no loop.

#### Examples

##### Example 1

- **Output:**
```text
4
```
- **Explanation:** There exists a loop in the linked list 2 - > 3 - > 4 - > 5, the length of the loop is 4.

##### Example 2

- **Output:**
```text
3
```
- **Explanation:** There exists a loop in the linked list 19 - > 33 - > 10, the length of loop is 3.

##### Example 3

- **Input:**
```text
Output: 0
```
- **Explanation:** There is no loop.

### Time and Auxiliary Space Complexity

- **Expected Time Complexity:** O(n)
- **Expected Auxiliary Space Complexity:** O(1)

### Accepted Solutions (1)

#### Solution 1 (Python)

- **Submitted:** 2026-10-03 18:07:57
- **Status:** Correct
- **Marks:** 4

```python
''' Structure of Linked List Node
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None
'''
class Solution:
    def lengthOfLoop(self, head):
        mp={}
        count=0
        curr=head
        while curr:
            if curr in mp:
                return count-mp[curr]
            mp[curr]=count
            count+=1
            curr=curr.next
        return 0
```

*Generated on: 10/29/2026, 1:46:16 AM*
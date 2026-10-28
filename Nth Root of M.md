## 01. Nth Root of M

The problem can be found at the following link: [Question Link](https://www.geeksforgeeks.org/problems/find-nth-root-of-m5843/1)

### Problem Description

**Task:** You are given 2 numbers n and m, the task is to find ^n√m (n^th root of m). If the root is not integer then return -1.

#### Examples

##### Example 1

- **Input:**
```text
n = 3, m = 8
```
- **Output:**
```text
2
```
- **Explanation:** 2³ = 8

##### Example 2

- **Input:**
```text
n = 3, m = 9
```
- **Output:**
```text
-1
```
- **Explanation:** 3rd root of 9 is not integer.

##### Example 3

- **Input:**
```text
n = 4, m = 16
```
- **Output:**
```text
2
```
- **Explanation:** 2⁴ = 16

### Time and Auxiliary Space Complexity

- **Expected Time Complexity:** O(n log m)
- **Expected Auxiliary Space Complexity:** O(1)

### Accepted Solutions (2)

#### Solution 1 (Python)

- **Submitted:** 2026-08-23 16:13:55
- **Status:** Correct
- **Marks:** 0

```python
class Solution:
    def nthRoot(self, n, m):
       # code here
        low=0
        high=m
        while low<=high:
            mid=low+(high-low)//2
            power = 1
            for i in range(1,n+1):
                power =power*mid
                if power>m:
                   break
            if power==m:
                return mid
            elif power<m:
                low=mid+1
            else:
                high=mid-1
        return -1
```

#### Solution 2 (Python)

- **Submitted:** 2026-08-23 15:56:14
- **Status:** Correct
- **Marks:** 4

```python
class Solution:
    def nthRoot(self, n, m):
       # code here
        low=0
        high=m
        while low<=high:
            mid=low+(high-low)//2
            power = 1
            for i in range(1,n+1):
                power =power*mid
                if power>m:
                   break
            if power==m:
                return mid
            elif power<m:
                low=mid+1
            else:
                high=mid-1
        return -1
```

*Generated on: 10/29/2026, 1:56:41 AM*
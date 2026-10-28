## 01. Ceil in Sorted Array

The problem can be found at the following link: [Question Link](https://www.geeksforgeeks.org/problems/ceil-in-a-sorted-array/1)

### Problem Description

**Task:** Given a sorted array arr[] (which may contain duplicate elements) and an integer x, find the 0-based index of the first element greater than or equal to x. This element is called the ceil of x.If no such element exists, return -1.Note: If multiple occurrences of the ceil exist, return the index of its first occurrence.Examples:Input: arr[] = [1, 2, 8, 10, 11, 12, 19], x = 5

#### Examples

##### Example 1

- **Output:**
```text
0
```
- **Explanation:** Smallest number greater than 0 is 1, whose indices are 0 and 1. The index of the first occurrence is 0.

### Time and Auxiliary Space Complexity

- **Expected Time Complexity:** O(log n)
- **Expected Auxiliary Space Complexity:** O(1)

### Accepted Solutions (1)

#### Solution 1 (Python)

- **Submitted:** 2026-10-27 11:48:45
- **Status:** Correct
- **Marks:** 2

```python
class Solution:
    def findCeil(self, arr, x):
        # code here
        ceil=-1
        low=0
        high=len(arr)-1
        while low<=high:
            mid=(low+high)//2

            if arr[mid]>=x:
                ceil=mid
                high=mid-1
            else:
                low=mid+1
        return ceil
```

*Generated on: 10/29/2026, 1:32:34 AM*
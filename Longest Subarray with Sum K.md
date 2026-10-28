## 01. Longest Subarray with Sum K

The problem can be found at the following link: [Question Link](https://www.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809/1)

### Problem Description

**Task:** Given an array arr[] containing integers and an integer k, your task is to find the length of the longest subarray where the sum of its elements is equal to the given value k. If there is no subarray with sum equal to k, return 0.Examples:Input: arr[] = [10, 5, 2, 7, 1, -10], k = 15

#### Examples

##### Example 1

- **Output:**
```text
0
```
- **Explanation:** No subarray with sum = 5 is present in arr[].

### Time and Auxiliary Space Complexity

- **Expected Time Complexity:** O(n)
- **Expected Auxiliary Space Complexity:** O(n)

### Accepted Solutions (1)

#### Solution 1 (Python)

- **Submitted:** 2026-09-27 15:30:10
- **Status:** Correct
- **Marks:** 4

```python
class Solution:
    def longestSubarray(self, arr, k):  
        prefix_sum=0
        mp={}
        max_len=0
        for i in range(len(arr)):
            prefix_sum+=arr[i]

            if prefix_sum==k:
                max_len=i+1
            if prefix_sum-k in mp:
                length=i-mp[prefix_sum-k]
                max_len=max(max_len,length)

            if prefix_sum not in mp:
                mp[prefix_sum]=i
        return max_len
```

*Generated on: 10/29/2026, 1:55:49 AM*
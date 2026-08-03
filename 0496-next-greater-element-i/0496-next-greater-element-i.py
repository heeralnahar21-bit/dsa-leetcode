class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nge = {}
        stack = []
        n = len(nums2)
        for i in range(n - 1, -1, -1):

            while len(stack) != 0 and stack[-1] <= nums2[i]:
                stack.pop()
            if stack:
                nge[nums2[i]] = stack[-1]
            else:
                nge[nums2[i]] = -1

            stack.append(nums2[i])
        ans = []
        for nums in nums1:
            ans.append(nge[nums])
        return ans

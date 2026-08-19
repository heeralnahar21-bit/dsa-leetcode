class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        current_max = nums[0]
        current_min = nums[0]
        ans = nums[0]

        for i in range(1, len(nums)):
            new_max = max(nums[i], current_max * nums[i], current_min * nums[i])
            new_min = min(nums[i], current_max * nums[i], current_min * nums[i])

            current_max = new_max
            current_min = new_min
            ans = max(ans, current_max)

        return ans

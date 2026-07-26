class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans = set()
        n = len(nums)
        i = 0
        for i in range(n):
            seen = set()
            for j in range(i + 1, n):
                third = -(nums[i] + nums[j])
                if third in seen:
                    triplet = tuple(sorted([nums[i], nums[j], third]))
                    ans.add(triplet)
                seen.add(nums[j])
        return list(ans)

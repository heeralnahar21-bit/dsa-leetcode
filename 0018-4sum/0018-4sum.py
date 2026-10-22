class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        ans=set()
        for a in range(len(nums)):
            for b in range(a+1,len(nums)):
                seen=set()
                for c in range(b+1,len(nums)):
                    fourth=target-(nums[a]+nums[b]+nums[c])
                    if fourth in seen:
                        ans.add(tuple(sorted([nums[a],nums[b],nums[c],fourth])))
                    seen.add(nums[c])
        return [list(t) for t in ans]
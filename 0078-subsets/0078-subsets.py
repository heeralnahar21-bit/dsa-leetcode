class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        ans=[]
        def backtrack(i,current):
            
            if i == len(nums):
                ans.append(current[:])
                return
            current.append(nums[i])
            backtrack(i + 1, current)

            
            current.pop()
            backtrack(i + 1, current)
            
        backtrack(0,[])
        return ans
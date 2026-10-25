class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest=0
        y=set(nums)
        
        for x in y:
            if x-1 not in y:
            
                count=1
                while x+1 in y:
                    count+=1
                    x+=1
                longest=max(longest,count)
        return longest
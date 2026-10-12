class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        freq={}
        max_len=0
        for right in range(len(s)):
            while freq.get(s[right],0)>0:
                
                freq[s[left]]-=1
                left+=1
            freq[s[right]]=freq.get(s[right],0)+1
            max_len=max(max_len,right-left+1)
        return max_len


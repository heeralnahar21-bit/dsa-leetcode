class Solution:
    def frequencySort(self, s: str) -> str:
        d={}
        for ch in s:
            d[ch]=d.get(ch,0)+1
        arr=sorted(d,key=lambda ch:d[ch],reverse=True)
        ans=""
        for ch in arr:
            ans+=ch*d[ch]
        return ans

        
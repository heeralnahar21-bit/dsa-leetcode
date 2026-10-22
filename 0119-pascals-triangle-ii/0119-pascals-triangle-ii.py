class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        ans=[]
        val=1
        for cols in range(rowIndex+1):
            ans.append(val)
            val=(val*(rowIndex-cols))//(cols+1)
        return ans
    
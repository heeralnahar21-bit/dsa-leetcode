class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans=[]
        def Backtracking(s,open,close):
            if len(s)==2*n:
                ans.append(s)
                return 
            if open<n:
                Backtracking(s+"(",open+1,close)
            if close<open:
                Backtracking(s+")",open,close+1)
        Backtracking("",0,0)
        return ans
        
        
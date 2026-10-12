class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        window_sum=sum(cardPoints[:k])
        
        max_score=window_sum
        for i in range(k):
            window_sum-=cardPoints[k-i-1]
            window_sum+=cardPoints[len(cardPoints)-1-i]
            max_score=max(window_sum,max_score)
        return max_score
        
        
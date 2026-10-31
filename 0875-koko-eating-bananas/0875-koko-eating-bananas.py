class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        low=1
        high=max(piles)
        while low<=high:
            mid=(low+high)//2
            total=0
            for pile in piles:
                total+=(pile+mid-1)//mid
            if total<=h:
                    high=mid-1
            else:
                    low=mid+1
        return low
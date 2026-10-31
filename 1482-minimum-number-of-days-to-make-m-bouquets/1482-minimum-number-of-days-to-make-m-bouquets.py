class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        if m*k>len(bloomDay):
            return -1
        def canmake(day):
            bouquet=0
            count=0
            for flower in bloomDay:
                if flower<=day:
                    count+=1
                    if count==k:
                        bouquet+=1
                        count=0
                else:
                    count=0
            return bouquet>=m
        low=min(bloomDay)
        high=max(bloomDay)
        while low<=high:
            mid=(low+high)//2
            if canmake(mid):
                high=mid-1
            else:
                low=mid+1
        return low

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count=0
        for i in range(len(flowerbed)):
            if flowerbed[i]==0:
                right_side=(flowerbed[i-1]==0) or (i==0)
                left_side=(i==len(flowerbed)-1) or (flowerbed[i+1]==0)
                if right_side and left_side:
                    flowerbed[i]=1
                    count+=1
        return count>=n
        
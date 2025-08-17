class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count=0
        i=1
        f=[0]+flowerbed+[0]
        len1=len(f)
        while i<len1-1:
            if f[i]==0 and f[i-1]==0 and f[i+1]==0:
                count+=1
                f[i]=1
                i+=2
            else:
                i+=1
        return count>=n
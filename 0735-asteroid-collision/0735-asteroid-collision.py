class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        a=asteroids #for convient shake
        result=[] 
        for i in range(len(a)):
            if a[i]>0:
                result.append(a[i])
            elif a[i]<0:
                while result and result[-1]>0 and abs(a[i])>result[-1]:
                    result.pop()
                if result and result[-1]>0 and abs(a[i])==result[-1]:
                    result.pop()
                elif not result or result[-1]<0:
                    result.append(a[i])
        return result
                
                
"""
If positive add 
If negative 
    not Empty, Top element +ve, Ab(current element)>Ab(Top element)
"""
                

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        result=[]
        for ast in asteroids:
            while result and result[-1]>0 and ast<0:
                last=result.pop() #pops the element (can add it back or not)
                if last>-ast: #if the result is positive then add it back
                    result.append(last) #add it back
                    break 
                elif last==-ast:
                    break #don't add anything 
            else:
                result.append(ast)
        return result



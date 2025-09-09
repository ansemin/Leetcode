class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        diff=[]
        for i in range(len(s)):
            if s[i]!=goal[i]:
                diff.append(i)
        if not diff:
            return len(set(s))<len(s)
        print(diff) #[0,1]
        if len(diff)==2:
            i,j=diff
            return s[i]==goal[j] and goal[i]==s[j]
        return False 

            
         



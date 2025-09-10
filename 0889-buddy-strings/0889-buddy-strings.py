class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        #1st False case: Length is different
        if len(s)!=len(goal):
            return False 
        if s==goal:
            return len(set(s))<len(s)
        #Track indices of difference
        diff=[]
        for i,j in enumerate(s):
            if s[i]!=goal[i]:
                diff.append(i)
        # False case, all the same indices 
        if not diff:
            return False
        # False case, more than one difference
        if len(diff)!=2:
            return False  
        i,j=diff
        return s[i]==goal[j] and s[j]==goal[i]


        
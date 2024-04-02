class Solution:
    def reverseVowels(self, s: str) -> str:

        vow=['a','e','i','o','u','A','E','I','O','U']
        new=[]

        for i in s:
            if i in vow:
                new.append(i)
        new.reverse()
        
        ss=list(s)
        s=''
        
        x=0
        for i in range(len(ss)):
            if ss[i] in vow:
                ss[i]=new[x]
                x+=1
        
        for i in ss:
            s=s+i
        return s
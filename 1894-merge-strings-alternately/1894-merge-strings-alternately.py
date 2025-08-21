class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1,word2=list(word1),list(word2)
        i,j,n,m=0,0,len(word1),len(word2)
        output=""
        while i<n or j<m:
            if i<n:
                output+=word1[i]
                i+=1
            if j<m:
                output+=word2[j]
                j+=1
        return output

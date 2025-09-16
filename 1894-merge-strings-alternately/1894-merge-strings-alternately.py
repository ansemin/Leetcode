class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i=0
        j=0
        result=""
        longerword=max(word1,word2, key=len)
        while i<min(len(word1),len(word2)):
            result+=word1[i]
            i+=1
            result+=word2[j]
            j+=1
        result+=longerword[i:]
        return result
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        """
               i
        word1=abcd
               j    
        word2=pq


        """
        # result=[]
        # word1,word2=list(word1),list(word2)
        # min_w=min(word1,word2)
        max_w=max(word1,word2, key=len)
        i,j=0,0
        result=""
        while i < min(len(word1),len(word2)):
            result+=word1[i]+word2[j]
            i+=1
            j+=1
            if i == min(len(word1),len(word2)):
                result+=max_w[i:]
        return result

            
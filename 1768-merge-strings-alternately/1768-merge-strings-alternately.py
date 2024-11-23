class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merged=""
        for i, j in zip(word1, word2):
            merged+=i+j
            
        merged+=word1[len(word2):]+word2[len(word1):]
        
        return merged
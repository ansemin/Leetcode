class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # the sky is blue -> ['the', 'sky']
        words=s.split()
        reversed_words=words[::-1] # ['sky','the']
        result=' '.join(reversed_words) # 'sky the'
        return result 

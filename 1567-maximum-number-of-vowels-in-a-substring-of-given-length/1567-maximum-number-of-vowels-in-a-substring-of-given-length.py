class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # s=list(s)
        vowel="aeiou"
        max_count=0 #initialize the count 
        # print(max_count)
        # initialization first window 
        for i in range(0, k):
            if s[i] in vowel:
                max_count+=1
        # print(max_count)
        current=max_count #initialize the current count
        for start in range(k,len(s)):
            if s[start-k] in vowel:
                current-=1
            if s[start] in vowel: 
                current+=1
            max_count=max(current,max_count)
        return max_count
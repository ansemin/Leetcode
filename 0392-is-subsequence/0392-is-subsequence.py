class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i,j=0,0
        output=""
        if len(s)==0:
            return True 
        while i < len(t):
            if j<len(s) and t[i]==s[j] :
                output+=t[i]
                i+=1
                j+=1
            else:
                i+=1
        return output==s
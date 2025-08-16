class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        len1, len2= len(str1),len(str2)
        for i in range(min(len1,len2),0,-1):
            if len1%i ==0 and len2%i==0:
                base=str1[:i]
                f1,f2=len1//len(base), len2//len(base)
                if f1*base==str1 and f2*base==str2:
                    return base
        return ""
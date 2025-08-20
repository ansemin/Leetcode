class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        """                     
                        g
                            i
        # chars = ["a","a","b","b","c","c","c"]
                            j
        # chars= ["a","1", "b"]
        """
        i=0
        j=0
        while i < len(chars):
            group=1
            while (i+group)<len(chars) and chars[i+group]==chars[i]:
                group+=1
            chars[j]=chars[i]
            j+=1
            if group >1:
                temp=str(group)
                chars[j:j+len(temp)]=list(temp)
                j+=len(temp)

            i+=group
        return j


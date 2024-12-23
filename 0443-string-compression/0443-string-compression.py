class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        write=0 #keeps track of where to write the compressed character
        read=0 # scans through the array to idenitfy the group of repeating character

        while read < len(chars):
            char=chars[read]
            count=0

            while read <len(chars) and chars[read]==char:
                read+=1
                count+=1
            
            chars[write]=char
            write+=1

            if count>1:
                for digit in str(count):
                    chars[write]=digit
                    write+=1
            # print(char)
            # print(chars[:write])
            # print(write)

        return write

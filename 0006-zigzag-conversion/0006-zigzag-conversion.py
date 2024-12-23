class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows ==1:
            return s
        rows= [""]*min(numRows, len(s))
        current_row=0
        going_down=False

        for c in s:
            # print('add {} to row {}'.format(c, current_row))
            rows[current_row] +=c
            if current_row ==0 or current_row==numRows-1:
                going_down = not going_down 
            current_row +=1 if going_down else -1
            # print('rows after adding {}: {}'.format(c, rows))
        result="".join(rows)
        return result
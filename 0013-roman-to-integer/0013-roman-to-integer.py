class Solution(object):
    def romanToInt(self, s):
        roman_dict = {'I': 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000, "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
        num = 0
        i = 0

        while i < len(s):
            # Check if we have a valid two-character Roman numeral
            if i + 1 < len(s) and s[i:i+2] in roman_dict:
                num += roman_dict[s[i:i+2]]
                i += 2
            else:
                num += roman_dict[s[i]]
                i += 1

        return(num)
            


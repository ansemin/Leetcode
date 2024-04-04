class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcd(a: int, b: int) -> int:
            """Calculate the Greatest Common Divisor (GCD) of two numbers."""
            while b != 0:
                a, b = b, a % b
            return a
        
        def checkDivides(x: str, s: str) -> bool:
            """Check if string x divides string s completely."""
            return x * (len(s) // len(x)) == s
        
        # Calculate the GCD of the lengths of str1 and str2
        lengthGCD = gcd(len(str1), len(str2))
        
        # Extract the potential divisor substring
        potentialDivisor = str1[:lengthGCD]
        
        # Verify if the potential divisor divides both str1 and str2
        if checkDivides(potentialDivisor, str1) and checkDivides(potentialDivisor, str2):
            return potentialDivisor
        else:
            return ""
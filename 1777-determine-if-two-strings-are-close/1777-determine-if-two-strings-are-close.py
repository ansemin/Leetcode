from collections import Counter 
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1)!=len(word2):
            return False 
        hash1, hash2=Counter(word1),Counter(word2)
        return set(hash1.keys())==set(hash2.keys()) and sorted(hash1.values())==sorted(hash2.values())
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # Create a reference set 
        cond=set(word1)
        # 1st condition: length has to be same
        if len(word1)!=len(word2):
            return False 
        # 2nd condition: all the characters of word2 contained in word1
        for i in range(len(word1)):
            if not word2[i] in cond:
                return False 
        # Create frequency counter dict 
        hash1=dict()
        hash2=dict() 
        for index in range(len(word1)):
            hash1[word1[index]]=hash1.get(word1[index],0)+1
            hash2[word2[index]]=hash2.get(word2[index],0)+1
        print(f'hash1 {hash1} hash2 {hash2}')
        if sorted(hash1.keys())==sorted(hash2.keys()) and sorted(hash1.values())==sorted(hash2.values()):
            return True
        else:
            return False 
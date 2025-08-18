class Solution:
    def reverseVowels(self, s: str) -> str:
        s_list=list(s) # ["I", "c","e", "C","r","e","A","m"]
        cc=[]
        vowels=["A","a","E","e","I","i","O","o","U","u"]
        for i in range(len(s_list)):
            if s_list[i] in vowels:
                cc.append(s_list[i])
        # print(f"1st Result: {cc}")
        cc=cc[::-1] # list[start, end, order]
        # print(f'reversed {cc}')
        # print(f"compare result {s_list}")
        i=0
        j=0
        while i <len(s_list):
            if s_list[i] in vowels:
                s_list[i]=cc[j]
                j+=1 
            i+=1
        # print(f"Final reuslt {s_list}")
        s="".join(s_list)
        return s





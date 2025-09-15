class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        for i in range(len(s)):
            if s[i]!="]":
                stack.append(s[i])
                print('1st')
                print('stack:', stack)
                print('s[i]:', s[i])
            else:
                last=""
                while stack and stack[-1]!="[":
                    char=stack.pop()
                    last=char+last
                stack.pop()
                print('2nd')
                print('stack', stack)
                print('Last:', last)
                k=""
                while stack and stack[-1].isdigit():
                    temp_k=stack.pop()
                    print('inner k', temp_k)
                    k=temp_k+ k
                print(temp_k)
                stack.append(int(k)*last)
        return "".join(stack)
                

            
        
             

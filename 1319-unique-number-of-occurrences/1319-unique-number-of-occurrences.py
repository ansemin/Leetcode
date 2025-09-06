class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arrset=set(arr) # 1 2 3
        result=dict() 
        # build a dict
        for num in arr:
            if num in arrset:
                result[num]=result.get(num,0)+1
        print(result) #new dict contain in this result 
        values=set(list(result.values()))
        keys=set(list(result.keys()))
        print(f'values {values} keys {keys}')
        return len(values)==len(keys) 


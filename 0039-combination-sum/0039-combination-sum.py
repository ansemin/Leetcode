class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        
        def backtrack(start, target, path, result):
            if target==0:
                result.append(list(path))
                return
            if target<0:
                return
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, target-candidates[i],path, result)
                path.pop()

        result=[]
        backtrack(0,target,[],result)
        return result
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # Get a column based list
        t=list(zip(*grid))
        count=0
        for i in grid:
            for j in t:
                if tuple(i)==j:
                    count+=1
        return count 
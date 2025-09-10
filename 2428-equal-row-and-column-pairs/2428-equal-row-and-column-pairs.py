from collections import Counter
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # Get a column based list
        t=list(zip(*grid))
        count=0
        # transform the grid into tuple 
        for i,j in enumerate(grid):
            grid[i]=tuple(j)

        ngrid=Counter(grid)
        for i in t:
            if i in ngrid:
                count+=ngrid.get(i)
        return count 
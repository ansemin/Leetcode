class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # Get a column based list
        t=list(zip(*grid))
        count=0
        # transform the grid into tuple 
        for i,j in enumerate(grid):
            grid[i]=tuple(j)

        for i in grid:
            for j in t:
                if i==j:
                    count+=1
        return count 
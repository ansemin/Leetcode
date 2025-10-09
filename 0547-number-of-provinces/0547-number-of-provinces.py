from collections import deque
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        visited=set()
        province=0
        for i in range(n):
            if i not in visited:
                province+=1
                queue=deque([i])
                visited.add(i)
                while queue:
                    current_city=queue.popleft()
                    for neighbor in range(n):
                        if isConnected[current_city][neighbor]==1 and neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
        return province
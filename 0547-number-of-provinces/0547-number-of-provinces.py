class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        from collections import deque 
        # Initial the counter and visited memory
        province=0
        visited=set()
        for i in range(len(isConnected)):
            if i not in visited:
                # Increase the increment
                province+=1
                # Set to queue for exploration
                queue=deque([i])
                # Add this to visited
                visited.add(i)
                while queue:
                    # Extract the index of the current city
                    current_city=queue.popleft()
                    for city in range(len(isConnected)):
                        if isConnected[current_city][city]==1 and city not in visited:
                            queue.append(city)
                            visited.add(city)
                
        return province


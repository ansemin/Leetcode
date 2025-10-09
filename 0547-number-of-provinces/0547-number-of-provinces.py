class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        from collections import deque 
        visited=set()
        counter=0
        for i in range(len(isConnected)):
            if i not in visited:
                visited.add(i)
                counter+=1
                # we need to the explore all relevant cities related to this ith city to ensure which cities links to this city as province 
                queue=deque([i])
                while queue:
                    # Extract the current city
                    current_city=queue.popleft()
                    for city in range(len(isConnected)):
                        if isConnected[current_city][city]==1 and city not in visited:
                            # mark it as seen 
                            visited.add(city)
                            # repeat for the next connecting city
                            queue.append(city)
        return counter
                        
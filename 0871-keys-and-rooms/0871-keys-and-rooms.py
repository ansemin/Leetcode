from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited={0}
        # Initialization
        queue=deque([0])
        while queue:
            current_key=queue.popleft()
            next_keys=rooms[current_key]
            for key in next_keys:
                if not key in visited:
                    visited.add(key)
                    queue.append(key)
        return len(visited)==len(rooms)


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited={0}
        queue=deque([0])
        while queue:
            current=queue.popleft()
            total_keys=rooms[current]
            for key in total_keys:
                if not key in visited:
                    visited.add(key)
                    queue.append(key)
        return len(visited)==len(rooms)
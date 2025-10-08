class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited={0}
        queue=deque([0])
        while queue:
            key_to_current_room=queue.popleft()
            keys_to_next_room=rooms[key_to_current_room]
            for key in keys_to_next_room:
                if not key in visited:
                    visited.add(key)
                    queue.append(key)
        return len(visited)==len(rooms)
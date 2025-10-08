class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        nums_rooms=len(rooms)
        # Track visited room 
        visited={0}
        # initialize with the starting position of the room,0
        queue=deque([0])
        while queue:
            # print('-------start------')
            # print(f'queue is {queue}')
            # print('------------------')
            current_room=queue.popleft()
            # print(f'current room is {current_room}')
            keys_in_room=rooms[current_room]
            # print(f'total keys are {keys_in_room}')
            for key in keys_in_room:
                # print(f'the key is {key}')
                if key not in visited:
                    visited.add(key)
                    queue.append(key)
            # print(f'visited is {visited}')
            # print('-----end of iteration----')
        return len(visited)==nums_rooms

                
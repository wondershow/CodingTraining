class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # each item [room_available_time, room_number, room_usage_count]
        available_rooms = list(range(n))
        heapify(available_rooms)
        using_rooms = []
        room_count = [0] * n
        meetings.sort()
        for start, end in meetings:
            while using_rooms and using_rooms[0][0] <= start:
                _, room = heappop(using_rooms)
                heappush(available_rooms, room)
            if available_rooms:
                room = heappop(available_rooms)
                heappush(using_rooms, [end, room])
                room_count[room] += 1
            else:
                available_time, i = heappop(using_rooms)
                heappush(using_rooms, [available_time + (end - start), i])
                room_count[i] += 1
        return room_count.index(max(room_count))

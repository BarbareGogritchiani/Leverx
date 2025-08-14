from typing import List, Dict, Any

class StudentRoomCombiner:

    def combine(self, students: List[Dict[str, Any]], rooms: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        room_map = {room["id"]: {**room, "students": []} for room in rooms}
        for student in students:
            room_id = student.get("room")
            if room_id in room_map:
                room_map[room_id]["students"].append(student)
        return list(room_map.values())

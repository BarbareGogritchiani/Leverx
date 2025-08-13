
import json
import argparse
import sys

students_file = "students.json"
rooms_file = "rooms.json"
output_file = "rooms_with_students.json"

def combine_students_and_rooms(students_file, rooms_file, output_file):
    try:
        with open(students_file, "r", encoding="utf-8") as f:
            students = json.load(f)
    except FileNotFoundError:
        print(f" Error: Students file '{students_file}' not found.")
        sys.exit(1)

    try:
        with open(rooms_file, "r", encoding="utf-8") as f:
            rooms = json.load(f)
    except FileNotFoundError:
        print(f" Error: Rooms file '{rooms_file}' not found.")
        sys.exit(1)

    room_map = {
        room["id"]: {**room, "students": []}
        for room in rooms
    }

    for student in students:
        room_id = student.get("room")
        if room_id in room_map:
            room_map[room_id]["students"].append(student)

    rooms_with_students = list(room_map.values())

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(rooms_with_students, f, indent=4)

    print(f" Data combined and saved to '{output_file}'")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Combine students and rooms data from JSON files into one output file."
    )
    parser.add_argument("students_file", help="Path to students.json file")
    parser.add_argument("rooms_file", help="Path to rooms.json file")
    parser.add_argument("output_file", help="Path for the output JSON file")

    args = parser.parse_args()

    combine_students_and_rooms(args.students_file, args.rooms_file, args.output_file)
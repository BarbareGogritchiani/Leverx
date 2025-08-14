import argparse
from readers import JSONFileReader
from writers import JSONFileWriter
from combiners import StudentRoomCombiner
from app import Application

DEFAULT_STUDENTS_FILE = "project/students.json"
DEFAULT_ROOMS_FILE = "project/rooms.json"
DEFAULT_OUTPUT_FILE = "project/rooms_with_students.json"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Combine students and rooms into one JSON file.")
    parser.add_argument("students_file", nargs="?", default=DEFAULT_STUDENTS_FILE, help="Path to students.json file")
    parser.add_argument("rooms_file", nargs="?", default=DEFAULT_ROOMS_FILE, help="Path to rooms.json file")
    parser.add_argument("output_file", nargs="?", default=DEFAULT_OUTPUT_FILE, help="Path for the output JSON file")

    args = parser.parse_args()

    app = Application(JSONFileReader(), JSONFileWriter(), StudentRoomCombiner())
    app.run(args.students_file, args.rooms_file, args.output_file)

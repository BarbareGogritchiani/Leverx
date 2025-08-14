class Application:

    def __init__(self, reader, writer, combiner):
        self.reader = reader
        self.writer = writer
        self.combiner = combiner

    def run(self, students_file: str, rooms_file: str, output_file: str) -> None:
        students = self.reader.read(students_file)
        rooms = self.reader.read(rooms_file)
        combined_data = self.combiner.combine(students, rooms)
        self.writer.write(output_file, combined_data)

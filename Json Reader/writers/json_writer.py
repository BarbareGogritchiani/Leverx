import json
from typing import Any

class JSONFileWriter:

    def write(self, file_path: str, data: Any) -> None:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        print(f" Data saved to '{file_path}'")

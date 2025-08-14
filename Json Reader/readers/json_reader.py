import json
import sys
from typing import Any, List, Dict

class JSONFileReader:

    def read(self, file_path: str) -> List[Dict[str, Any]]:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            print(f" Error: File '{file_path}' not found.")
            sys.exit(1)

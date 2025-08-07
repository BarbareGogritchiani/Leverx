import re
from functools import total_ordering

@total_ordering
class Version:
    def __init__(self, version):
        self.original = version
        self.major = 0
        self.minor = 0
        self.patch = 0
        self.pre_release = []

        self._parse(version)

    def _parse(self, version):
        # Split pre-release part if it exists
        if '-' in version:
            version, pre = version.split('-', 1)
            self.pre_release = self._parse_pre_release(pre)
        elif any(c.isalpha() for c in version):
            # handle cases like "1.0.0b" or "0.3.0b"
            match = re.match(r"([\d\.]+)([a-zA-Z].*)", version)
            if match:
                version, pre = match.groups()
                self.pre_release = self._parse_pre_release(pre)
        else:
            self.pre_release = []

        # Parse major.minor.patch
        parts = version.split('.')
        if len(parts) >= 1:
            self.major = int(parts[0])
        if len(parts) >= 2:
            self.minor = int(parts[1])
        if len(parts) >= 3:
            self.patch = int(parts[2])

    def _parse_pre_release(self, pre):
        parts = re.split(r'\.|-', pre)
        result = []
        for part in parts:
            if part.isdigit():
                result.append(int(part))
            else:
                result.append(part)
        return result

    def __eq__(self, other):
        return (
            (self.major, self.minor, self.patch, self.pre_release or [None])
            == (other.major, other.minor, other.patch, other.pre_release or [None])
        )

    def __lt__(self, other):
        # Compare major, minor, patch
        if (self.major, self.minor, self.patch) != (other.major, other.minor, other.patch):
            return (self.major, self.minor, self.patch) < (other.major, other.minor, other.patch)

        # Handle pre-release precedence
        if not self.pre_release and other.pre_release:
            return False  # self is a full release, other is pre-release
        if self.pre_release and not other.pre_release:
            return True  # self is pre-release, other is full release

        # Compare pre-release parts
        for s, o in zip(self.pre_release, other.pre_release):
            if s == o:
                continue
            if isinstance(s, int) and isinstance(o, int):
                return s < o
            elif isinstance(s, int):
                return True  # numbers < strings
            elif isinstance(o, int):
                return False  # strings > numbers
            else:
                return str(s) < str(o)

        # If all matched so far, shorter pre-release is smaller
        return len(self.pre_release) < len(other.pre_release)

    def __repr__(self):
        return f"Version('{self.original}')"

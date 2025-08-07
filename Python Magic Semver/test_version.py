from version import Version

def main():
    to_test = [
        ("1.0.0", "2.0.0"),
        ("1.0.0", "1.42.0"),
        ("1.2.0", "1.2.42"),
        ("1.1.0-alpha", "1.2.0-alpha.1"),
        ("1.0.1b", "1.0.10-alpha.beta"),
        ("1.0.0-rc.1", "1.0.0"),
    ]

    for left, right in to_test:
        v1 = Version(left)
        v2 = Version(right)
        print(f"Testing {v1} < {v2} => {v1 < v2}")
        assert v1 < v2, f"Failed: {v1} should be < {v2}"
        assert v2 > v1, f"Failed: {v2} should be > {v1}"
        assert v1 != v2, f"Failed: {v1} should != {v2}"

if __name__ == "__main__":
    main()

"""Example of function that processes every item in list."""

def main() -> None:
    names: list[str] = ["David", "Kris", "Floppo"]
    print(contains("David", names))


def contains(needle: str, haystack: list[str]) -> bool:
    """Goes through each item in list and checks whether needle is there. Returns True if so, False if otherwise."""
    i: int = 0
    while i < len(haystack):
        if haystack[i] == needle:
            return True
        i += 1
    return False

if __name__ == "__main__":
    main()
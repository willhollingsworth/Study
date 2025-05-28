"""Code wars.

for https://www.codewars.com/kata/545cedaa9943f7fe7b000048
"""
from string import ascii_lowercase


def is_pangram(st: str) -> bool:
    """Check if the string is a pangram."""
    results = [char in st.lower() for char in ascii_lowercase]
    return all(results)


if __name__ == "__main__":
    # Test cases
    print(is_pangram("The quick brown fox jumps over the lazy dog"), True)
    print(is_pangram("This is not a pangram"), False)
    print(is_pangram("Pack my box with five dozen liquor jugs"), True)
    print(is_pangram("Hello World!"), False)
    print(is_pangram("abcdefghijklmnopqrstuvwxyz"), True)

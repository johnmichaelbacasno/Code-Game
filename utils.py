import random
from collections.abc import Iterator

def unique_number(n: int) -> str:
    """A function that returns a string of number with 4 unique digits"""
    if n > 10: raise ValueError("n must be less than 10")
    
    return "".join(map(str, random.sample(range(0, 9 + 1), n)))

def generate_result(s: str, n: str) -> Iterator[str]:
    """
    A function that generates result based on the comparison of `s ` and `n`

    Yields
    ------
    "0"
        When a digit in `s` is in `n` and in similar position
    "X"
        When a digit in `s` is in `n` but in different position
    "-"
        When a digit in `s` is not in `n`
    
    """
    if len(s) != len(n): raise ValueError("Length of both strings must be equal")
    
    for index in range(0, len(n)):
        # Checks if digit is correct
        if s[index] in n:
            # Checks if digit is in the correct position
            if s[index] == n[index]:
                yield "0"
            else:
                yield "X"
        else:
            yield "-"

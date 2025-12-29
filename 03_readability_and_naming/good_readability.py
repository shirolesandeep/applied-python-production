from typing import List


def get_even_squares_greater_than_ten(numbers: List[int]) -> List[int]:
    """Return squares of even numbers greater than ten."""
    result: List[int] = []

    for number in numbers:
        if number <= 10:
            continue

        if number % 2 != 0:
            continue

        result.append(number * number)

    return result

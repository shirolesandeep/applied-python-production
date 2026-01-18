from typing import List


def get_average(numbers: List[float]) -> float:
    if not numbers:
        raise ValueError("numbers list cannot be empty")

    total = 0.0
    count = 0

    for number in numbers:
        if not isinstance(number, (int, float)):
            raise TypeError("all items must be numbers")

        total += number
        count += 1

    return total / count

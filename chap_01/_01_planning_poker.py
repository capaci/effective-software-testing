from dataclasses import dataclass
from typing import Optional


@dataclass
class Estimate:
    developer: str
    value: int


def identify_extremes(estimates: list[Estimate]) -> list[str]:
    if estimates is None:
        raise ValueError('Estimates cannot be None') 

    if len(estimates) <= 1:
        raise ValueError('There has to be more than 1 estimate in the list')

    highest: Optional[Estimate] = None
    lowest: Optional[Estimate] = None


    for estimate in estimates:
        if highest is None or estimate.value > highest.value:
            highest = estimate

        if lowest is None or estimate.value < lowest.value:
            lowest = estimate 

    return [
        lowest.developer,
        highest.developer
    ]


if __name__ == '__main__':
    res = identify_extremes([
        Estimate('A', 5),
        Estimate('B', 15),
        Estimate('C', 3),
        Estimate('D', 4),
        Estimate('E', 9),
        Estimate('F', 8),
    ])

    print(res)



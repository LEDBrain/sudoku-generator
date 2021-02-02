from typing import Callable
from Backtracker import Backtracker


def sudoku_validator(backtracker: Backtracker[int]) -> Callable[[int], bool]:
    def validator(proposed: int) -> bool:
        index = backtracker.element_index
        row = index // 9
        col = index % 9
        region = col // 3 + [0, 3, 6][row // 3]
        row_cells = backtracker.values[row * 9 : row * 9 + 9]
        col_cells = [backtracker.values[col + i * 9] for i in range(9)]
        region_cells = [
            element.value
            for element in filter(
                lambda element: (
                    (element.id % 9) // 3 + [0, 3, 6][(element.id // 9) // 3]
                )
                == region,
                backtracker.elements,
            )
        ]
        return proposed not in [*row_cells, *col_cells, *region_cells]

    return validator


def sudoku_printer(backtracker: Backtracker[int]) -> Callable[[], str]:
    def printer() -> str:
        result: str = ""
        for row in range(9):
            for col in range(9):
                if col != 0:
                    result += " "
                cell = backtracker.elements[row * 9 + col]
                result += str(cell) if cell.value is not None else str(0)
                if col in [2, 5]:
                    result += " |"
            if row != 8:
                result += "\n"
            if row in [2, 5]:
                result += "–" * (9 + 8 + 2 * 2) + "\n"
        return result

    return printer


class Sudoku(Backtracker[int]):
    def __init__(self):
        Backtracker.__init__(
            self, 81, [*range(1, 10)], sudoku_validator, sudoku_printer
        )

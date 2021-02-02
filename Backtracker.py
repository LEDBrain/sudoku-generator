import random
from typing import List, Generic, Callable
from BacktrackElement import BacktrackElement
from Types import CellValue


class Backtracker(Generic[CellValue]):
    def __init__(
        self,
        size: int,
        possible_values: List[CellValue],
        validation_function: Callable[
            ["Backtracker[CellValue]"], Callable[[CellValue], bool]
        ],
        str_function: Callable[["Backtracker[CellValue]"], Callable[[], str]] = None,
    ):
        BacktrackElement.possible_values = possible_values
        self.elements: List[BacktrackElement[CellValue]] = [
            BacktrackElement() for _ in range(size)
        ]
        self.element_index: int = 0
        self.validator = validation_function(self)
        if str_function:
            self.str_function = str_function(self)

    def __str__(self):
        if self.str_function:
            return self.str_function()
        return f"Backtracker with size {self.size}"

    @property
    def element(self):
        return self.elements[self.element_index]

    @property
    def values(self):
        return [element.value for element in self.elements]

    @property
    def size(self):
        return len(self.elements)

    def _backtrack(self):
        self.element.reset()
        self.element_index -= 1

    def _fill_element(self):
        proposed = random.choice(self.element.possible_values)
        if not self.validator(proposed):
            self.element.invalidate(proposed)
        else:
            self.element.set(proposed)
            self.element_index += 1

    def generate_solution(self):
        while self.element_index < self.size:
            if not self.element.fillable:
                self._backtrack()
            else:
                self._fill_element()

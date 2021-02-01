from typing import List, Optional, Tuple

Position = Tuple[int, int]

"""
regions:
0 | 1 | 2
---------
3 | 4 | 5
----------
6 | 7 | 8
"""


class Cell:
    def __init__(self, pos: Position):
        self.possibilities: List[int] = [*range(1, 10)]
        self.value: Optional[int] = None
        self.position: Position = pos

    def __str__(self) -> str:
        return str(self.value) if self.value is not None else str(0)

    def set(self, value: int) -> None:
        self.value = value

    def remove(self, value: int) -> None:
        self.possibilities.remove(value)

    @property
    def valid(self) -> bool:
        return bool(len(self.possibilities))

    @property
    def row(self) -> int:
        return self.position[0]

    @property
    def col(self) -> int:
        return self.position[1]

    @property
    def region(self) -> int:
        return self.col // 3 + [0, 3, 6][self.row // 3]

    def reset(self) -> None:
        self.__init__(self.position)

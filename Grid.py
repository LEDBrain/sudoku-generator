import random
from typing import List

from Cell import Cell


class Grid:
    def __init__(self):
        self.cells: List[Cell] = [Cell((i // 9, i % 9)) for i in range(81)]
        self.backtrack_cell: int = 0

    def __str__(self):
        result: str = ''
        for row in range(9):
            for col in range(9):
                if col != 0:
                    result += ' '
                result += str(self.cells[row * 9 + col])
                if col in [2, 5]:
                    result += ' |'
            if row != 8:
                result += '\n'
            if row in [2, 5]:
                result += '–' * (9 + 8 + 2 * 2) + '\n'
        return result

    @staticmethod
    def _values_from_cell_list(cell_list: List[Cell]) -> List[int]:
        return [cell.value for cell in cell_list]

    def _fill_cell(self) -> None:
        proposed: int = random.choice(self.cell.possibilities)
        if proposed in [
            *Grid._values_from_cell_list(self.row_cells),
            *Grid._values_from_cell_list(self.col_cells),
            *Grid._values_from_cell_list(self.region_cells)
        ]:
            self.cell.remove(proposed)
        else:
            self.cell.set(proposed)
            self.backtrack_cell += 1

    def _backtrack(self) -> None:
        self.cell.reset()
        self.backtrack_cell -= 1

    @property
    def cell(self) -> Cell:
        return self.cells[self.backtrack_cell]

    @property
    def row(self) -> int:
        return self.cell.row

    @property
    def col(self):
        return self.cell.col

    @property
    def region(self):
        return self.cell.region

    @property
    def row_cells(self) -> List[Cell]:
        return self.cells[(self.row * 9):(self.row * 9 + 9)]

    @property
    def col_cells(self) -> List[Cell]:
        return [self.cells[self.col + i * 9] for i in range(9)]

    @property
    def region_cells(self) -> List[Cell]:
        return [*filter(lambda cell: cell.region == self.region, self.cells)]

    def fill(self) -> None:
        while self.backtrack_cell < 81:
            if not self.cell.valid:
                self._backtrack()
            else:
                self._fill_cell()

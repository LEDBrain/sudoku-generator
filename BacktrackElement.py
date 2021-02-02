from typing import Generic, List, Optional

from Types import CellValue


class BacktrackElement(Generic[CellValue]):
    possible_values: List[CellValue] = []
    index: int = 0

    def __init__(self, reset: bool = False):
        self.value: Optional[CellValue] = None
        self.possible_values = BacktrackElement.possible_values.copy()

        if not reset:
            self.id = BacktrackElement.index
            BacktrackElement.index += 1

    def __str__(self):
        return str(self.value)

    @property
    def fillable(self):
        return bool(len(self.possible_values))

    def set(self, value: CellValue):
        if value not in self.possible_values:
            raise ValueError(
                f"Cannot set value `{value}` to element #{self.id} because it is not contained in possible values "
                f"{self.possible_values}"
            )
        self.value = value
        self.invalidate(value)

    def invalidate(self, value: CellValue):
        if value not in self.possible_values:
            raise ValueError(
                f"Cannot remove value `{value} from element #{self.id} because it is not "
                f"contained in possible values {self.possible_values}"
            )
        self.possible_values.remove(value)

    def reset(self):
        self.__init__(reset=True)

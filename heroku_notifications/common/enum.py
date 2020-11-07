from enum import Enum
from typing import Tuple


class ChoiceEnum(Enum):
    @classmethod
    def to_choices(cls) -> Tuple[Tuple[str, str], ...]:
        return tuple((entry.name, entry.value) for entry in cls)

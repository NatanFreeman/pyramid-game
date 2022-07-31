from enum import Enum
from colorama import Fore
import random


class Square(Enum):
    """A square on the board
    """
    BLANK = 0
    BLUE = 1
    YELLOW = 2
    PINK = 3

    def __repr__(self):
        return f"{self.name:7}"

    def __str__(self) -> str:
        """Returns the `Square` in the representation of a symbol
        """
        if self == Square.BLANK:
            return "_"
        if self == Square.BLUE:
            return "&"
        if self == Square.YELLOW:
            return "*"
        if self == Square.PINK:
            return "+"

    def pretty(self) -> str:
        """returns the `Square` ✨in color✨
        """
        if self == Square.BLANK:
            return Fore.WHITE+"#"
        if self == Square.BLUE:
            return Fore.BLUE+"#"
        if self == Square.YELLOW:
            return Fore.YELLOW+"#"
        if self == Square.PINK:
            return Fore.RED+"#"

    def rand():
        """Returns a random non-empty `Square`
        """
        return Square(random.randint(1, 3))

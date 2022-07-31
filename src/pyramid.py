import copy
from colorama import Fore
from square import Square


class Pyramid():
    arr: list
    next_arr: list

    def step(self):
        """Runs one turn of the simulation

        This is done by creating a new board based off the original, and changing it's `Square`'s by checking the rules on the original board. 
        """

        for (y, value) in enumerate(self.arr):
            # yellow rule
            if self.arr[y].count(Square.YELLOW) > 4:
                for x in range(len(self.next_arr[y])):
                    self.next_arr[y][x] = Square.rand()

            for x in range(y, len(value)-y):

                if value[x] == Square.BLANK:
                    value[x] = Square.rand()
                    continue

                # pink rule
                if value[x] == Square.PINK:
                    try:
                        if self.arr[y][x-1] == Square.BLUE and self.arr[y][x+1] == Square.BLUE and self.arr[y-1][x] == Square.BLUE and self.arr[y+1][x] == Square.BLUE:
                            next = Square.rand()
                            self.next_arr[y][x] = next
                    except IndexError:
                        pass

                # blue rule
                if value[x] == Square.BLUE:
                    if x == y or x == len(value)-y:
                        next = Square.rand()
                        self.next_arr[y][x] = next
                    elif y == 0:
                        next = Square.rand()
                        self.next_arr[y][x] = next
                self.arr = self.next_arr

    def _print(arr) -> str:
        res = ""
        for y in arr:
            for x in y:
                res += f"{x.pretty()} "
            res += "\n"
        rows = res.split("\n")
        rows.reverse()
        res = ""
        for i in rows:
            res += i+"\n"
        return res

    def __str__(self) -> str:
        return Pyramid._print(self.arr)

    def __init__(self, arr: list = []) -> None:
        self.arr = arr
        if len(arr) == 0:
            row = [Square.BLANK for _ in range(9)]
            for _ in range(5):
                arr.append(copy.deepcopy(row))
            self.next_arr = copy.deepcopy(arr)
            self.step()
        self.next_arr = copy.deepcopy(arr)

    def print_next(self) -> str:
        return Pyramid._print(self.next_arr)

    def print_symbols(arr) -> str:
        res = ""
        for y in arr:
            for x in y:
                res += f"{x} "
            res += "\n"
        return res

    def _str_to_list(string: str) -> list:
        string = string.replace(" ", "")
        arr = [Square.BLANK for _ in range(9)]

        for (x, value) in enumerate(string):
            if value == "*":
                arr[x] = Square.YELLOW
                continue

            if value == "&":
                arr[x] = Square.BLUE
                continue

            if value == "+":
                arr[x] = Square.PINK
                continue

        return arr

    def _read_pyramid(turn: int) -> list:
        file = open("pyramid.txt", 'r')
        lines = file.readlines()
        res = []
        for i in range(5):
            res.append(lines[i+turn*5].strip())
        return res

    def load_pyramid(turn: int):
        """loads a pyramid from the data in a file.

        Args:
            turn (int): the simulation index

        Returns:
            Pyramid:
        """
        arr = Pyramid._read_pyramid(turn)
        for i in range(len(arr)):
            arr[i] = Pyramid._str_to_list(arr[i])

        return Pyramid(arr)

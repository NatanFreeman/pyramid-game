import unittest

from colorama import Fore
from src.pyramid import Pyramid
from src.square import Square
import copy
import random


class TestStringMethods(unittest.TestCase):

    def test_pyramid(self):
        """Tests if a pyramid is read from a file successfully
        """
        strings = Pyramid._read_pyramid(0)

        squares = copy.deepcopy(strings)
        for i in squares:
            i = Pyramid._str_to_list(i)

        for i in range(len(strings)):
            self.assertEqual(strings[i], squares[i].__str__())

    def test_run_turns(self):
        """Tests 20 turns of the simulation for errors
        """
        random.seed(111)

        got: Pyramid = Pyramid.load_pyramid(0)

        for _ in range(20):
            print(Pyramid.print_symbols(got.arr))
            got.step()

    def test_check_turns(self):
        """Tests that 20 turns of the simulation run correctly
        """
        random.seed(111)

        got: Pyramid = Pyramid.load_pyramid(0)

        for i in range(20):
            expected = Pyramid.load_pyramid(i)
            print(got)
            # print(f"expected:\n{expected}")
            self.assertEqual(got.arr, expected.arr)
            got.step()


if __name__ == '__main__':
    unittest.main()

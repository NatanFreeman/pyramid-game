# Pyramid Game

This is an implementation of the "Pyramid Game".
The Pyramid Game is a cellular automata akin to that of Conway's Game Of Life.
The board is made up of a 9x5 grid containing a pyramid of randomly colored squares.
The rules of the game are then checked upon each square of the pyramid.

## Rules

There are 4 differently colored squires, one of which is blank and ignored. When a rule says that a square must die, it is replaced with another random square which may not be blank. The new square may be the same color as the previous square.

- The Blue square dies if it is on one of the sides of the pyramid
- The Pink square dies if it is sounded on all sides by Blue squares. This does not include diagonal.
- If a row has more than 4 Yellow Squares, the whole row dies.

## File structure

- `src` the Python source files. `main.py` being an infinite simulation.
- `tests` unittest.

## License

This project is licensed under [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0)

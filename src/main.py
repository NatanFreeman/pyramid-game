from pyramid import Pyramid
import random


def main():
    pyramid = Pyramid()
    while True:
        print(pyramid)
        pyramid.step()
        input()


if __name__ == '__main__':
    main()

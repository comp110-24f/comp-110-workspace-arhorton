"""printing the coordinates of the two input strings"""

__author__ = "730664552"


def get_coords(xs: str, ys: str) -> None:
    index1: int = 0
    index2: int = 0
    while index1 < len(xs):
        index2: int = 0
        while index2 < len(ys):
            print("(" + xs[index1], ",", ys[index2] + ")")
            index2 += 1
        index1 += 1

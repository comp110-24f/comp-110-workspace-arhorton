from CQs.cq07.find_max import find_and_remove_max

"""Testing the max functions"""

__author__ = "7306645652"


def test_usecase1() -> None:  # tests that the removed value is the max
    list1: list[int] = [10, 9, 8, 7, 10]
    assert find_and_remove_max(list1) == 10


def test_usecase2() -> None:  # tests that the input list is modified correctly
    list1: list[int] = [10, 9, 8, 7, 10]
    assert find_and_remove_max(list1) == [9, 8, 7]


def test_edgecase() -> None:  # tests that the empty list returns -1
    list1: list[int] = []
    assert find_and_remove_max(list1) == -1

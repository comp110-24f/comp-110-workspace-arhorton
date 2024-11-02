from exercises.ex05.utils import (
    only_evens,
    sub,
    add_at_index,
)  # import the functions from the other file
import pytest  # import the test built-in function

"""Implementing tests for the utility test functions"""

__author__ = "730664552"


def test_onlye() -> None:  # all should return None (all test cases)
    """Test list1 returns the values of the list that are even - modifying input"""
    list1: list[int] = [1, 2, 3, 4, 5]  # list1 of integers
    assert only_evens(list1) == [2, 4]  # returns the even values in the list


def test_onlyevens() -> None:
    """Test if all are even, will just return the list - list[int] as return type"""
    list1: list[int] = [2, 4, 6, 8]  # list of all even numbers
    assert only_evens(list1) == [
        2,
        4,
        6,
        8,
    ]  # returns the whole list of list[int] as dictated by the return type


def test_edgeonlyevens() -> None:
    """Edge case test: if an odd list is entered, return [] - edge case"""
    list1: list[int] = [1, 3, 5, 7]  # odd list
    assert only_evens(list1) == []  # returns nothing because the list is all odd


def test_sub() -> None:
    """Testing if it will pull out the values needed - mutating the input"""
    a_list: list[int] = [15, 25, 35, 45]  # giving the function a list of ints
    assert sub(a_list, 1, 2) == [
        25
    ]  # only pulling out 25 because the end index is noninclusive
    # mutates the input list


def test_subedge() -> None:
    """Testing what happens if the starting index is below zero - edge case"""
    a_list: list[int] = [15, 25, 35, 45]  # a list of ints as the input
    assert (
        sub(a_list, -1, 0) == []
    )  # the index is below zero, return only an empty string - edge case


def test_sub1() -> None:
    """Testing to see if it pulls out values at indexes - returns a list of ints"""
    a_list: list[int] = [15, 25, 35, 45]  # a list of ints for the input
    assert sub(a_list, 0, 4) == [15, 25, 35, 45]  # returns a list of ints


def test_add() -> None:
    """Testing to see if it will return the correct value of None - return type"""
    list_1: list[int] = [1, 3, 5, 9]  # input = a list of integers
    assert (
        add_at_index(list_1, 7, 3) == None
    )  # the return type is None - should return None


def test_add1() -> None:
    """Testing to see if it will mutate the list correctly - modifying input"""
    list_1: list[int] = [1, 3, 5, 6]  # list of ints as the input
    add_at_index(list_1, 4, 2)  # the mutation command
    assert list_1 == [1, 3, 4, 5, 6]  # return the correctly mutated list


def test_edgeadd() -> None:
    """Testing that add_at_index raises an index error when appropriate - edge case"""
    list_1: list[int] = [2, 4, 5, 4, 3, 7]  # the list of input ints
    with pytest.raises(IndexError):  # the raising error that was given in the writeup
        add_at_index(list_1, 4, 45)  # error is the end index > len(list_1)

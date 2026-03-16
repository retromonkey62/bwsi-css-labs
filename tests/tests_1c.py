"""
tests_1c.py

This module contains unit tests for lab_1c.py.
"""

import pytest
from labs.lab_1.lab_1c import max_subarray_sum

def test_mixed_numbers():
    assert max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]) == 6

def test_all_positive():
    assert max_subarray_sum([3, 1, 5, 8, 6]) == 23

def test_all_negative():
    assert max_subarray_sum([-7, -3, -6, -4, -9, -2]) == -2

def test_one_element():
    assert max_subarray_sum([3]) == 3

def test_zeroes():
    assert max_subarray_sum([2, 0, -3, 4, -2, 0, -1, 4]) == 5

def test_one_best_element():
    assert max_subarray_sum([-2, 1, 1, -3, 11, -4]) == 11


if __name__ == "__main__":
    pytest.main()
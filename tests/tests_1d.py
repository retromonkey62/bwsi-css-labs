"""
tests_1d.py

This module contains unit tests for lab_1d.py.
"""

import pytest
from labs.lab_1.lab_1d import two_sum

def test_all_postive():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]   # Test for zero addition

def test_all_negative():
    assert two_sum([-2, -3, -6, -4, -9], -7) == [1, 3]

def test_mixed_numbers():
    assert two_sum([4, -3, 3, 7, -5], -1) == [0, 4]

def test_zero_used():
    assert two_sum([4, 0, 3, 9, 7], 9) == [1, 3]

def test_zero_target():
    assert two_sum([2, -3, 4, 5, -5], 0) == [3, 4]

def test_duplicates():
    assert two_sum([6, 3, 5, 6], 12) == [0, 3]



if __name__ == "__main__":
    pytest.main()
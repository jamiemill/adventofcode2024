import pytest
from day01 import solve, solve_part2


def test_example():
    example_input = """3   4
4   3
2   5
1   3
3   9
3   3
"""
    assert solve(example_input) == 11
    assert solve_part2(example_input) == 31

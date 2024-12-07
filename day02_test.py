import pytest
from day02 import solve, solve_part2


def test_example():
    example_input = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""
    assert solve(example_input) == 2
    assert solve_part2(example_input) == 4


test_example()
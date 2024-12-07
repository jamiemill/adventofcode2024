import pytest
from day03 import solve, solve_part2


def test_example():
    example_input = """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""
    assert solve(example_input) == 161
    example_input2 = """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""
    assert solve_part2(example_input2) == 48


test_example()
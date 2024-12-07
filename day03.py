import re

def solve(input_data:str) -> int:
    matches = re.findall(r"mul\(\d+,\d+\)", input_data)
    total = 0
    for match in matches:
        l,r = re.findall(r"\d+", match)
        total += int(l) * int(r)
    return total

def solve_part2(input_data:str) -> int:
    matches = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", input_data)
    enabled = True
    total = 0
    for match in matches:
        if match == "do()": enabled = True
        if match == "don't()": enabled = False
        if re.match(r"mul\(\d+,\d+\)", match) and enabled:
            l,r = re.findall(r"\d+", match)
            total += int(l) * int(r)
    return total
    

if __name__ == "__main__":
    with open("input/day03.txt") as f:
        puzzle_input = f.read()
    result = solve(puzzle_input)
    print(f"Result: {result}")
    result = solve_part2(puzzle_input)
    print(f"Result: {result}")
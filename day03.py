import re

CMD_MUL = r"mul\(\d+,\d+\)"
CMD_DO = r"do\(\)"
CMD_DONT = r"don't\(\)"

def solve(input_data:str) -> int:
    matches = re.findall(CMD_MUL, input_data)
    total = 0
    for match in matches:
        l,r = re.findall(r"\d+", match)
        total += int(l) * int(r)
    return total

def solve_part2(input_data:str) -> int:
    matches = re.findall(CMD_MUL + "|" + CMD_DO + "|" + CMD_DONT, input_data)
    enabled = True
    total = 0
    for match in matches:
        if re.match(CMD_DO, match): enabled = True
        if re.match(CMD_DONT, match): enabled = False
        if re.match(CMD_MUL, match) and enabled:
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
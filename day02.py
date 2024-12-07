def parse(input_data:str) ->list[list[int]]:
    lines = input_data.splitlines()
    return [list(map(int, l.split())) for l in lines]

def range_ok(pair):
    [l,r] = pair
    return abs(l-r) < 4 and abs(l-r) > 0

def is_safe(report):
    is_increasing = sorted(report) == report
    is_decreasing = list(reversed(sorted(report))) == report
    pairs = list(zip(report, report[1:]))
    differences_are_ok = False not in map(range_ok, pairs)
    return (is_increasing or is_decreasing) and differences_are_ok


def solve(input_data:str) -> int:
    reports = parse(input_data)
    count_safe = 0
    for report in reports:
        if is_safe(report): count_safe += 1 
    return count_safe


# def solve_part2(input_data:str) -> int:
   



if __name__ == "__main__":
    with open("input/day02.txt") as f:
        puzzle_input = f.read()
    result = solve(puzzle_input)
    print(f"Result: {result}")
    # result = solve_part2(puzzle_input)
    # print(f"Result: {result}")
def parse(input_data:str) ->list[list[int]]:
    lines = input_data.splitlines()
    return [list(map(int, l.split())) for l in lines]


def solve(input_data:str) -> int:
    reports = parse(input_data)
    count_safe = 0
    for report in reports:
        is_increasing = sorted(report) == report
        is_decreasing = list(reversed(sorted(report))) == report
        differences_are_ok = True
        pairs = zip(report, report[1:])
        for pair in pairs:
            [l,r] = pair
            if abs(l-r) > 3:
                differences_are_ok = False
            if abs(l-r) < 1:
                differences_are_ok = False
        is_safe = (is_increasing or is_decreasing) and differences_are_ok
        if is_safe:
            count_safe += 1
    return count_safe


# def solve_part2(input_data:str) -> int:
   



if __name__ == "__main__":
    with open("input/day02.txt") as f:
        puzzle_input = f.read()
    result = solve(puzzle_input)
    print(f"Result: {result}")
    # result = solve_part2(puzzle_input)
    # print(f"Result: {result}")
def parse(input_data:str) ->list[list[int]]:
    lines = input_data.splitlines()
    return [list(map(int, l.split())) for l in lines]

def range_ok(pair):
    l,r = pair
    return 0 < abs(l-r) < 4

def is_safe(report):
    is_increasing = sorted(report) == report
    is_decreasing = sorted(report, reverse=True) == report
    pairs = zip(report, report[1:])
    differences_are_ok = all(range_ok(pair) for pair in pairs)
    return (is_increasing or is_decreasing) and differences_are_ok


def solve(input_data:str) -> int:
    reports = parse(input_data)
    count_safe = 0
    for report in reports:
        if is_safe(report): count_safe += 1 
    return count_safe

def remove_item_at_index(idx, lst):
    return lst[:idx] + lst[idx+1:]

def solve_part2(input_data:str) -> int:
    reports = parse(input_data)
    count_safe = 0
    for report in reports:
        report_variants = [report] + list(map(lambda i: remove_item_at_index(i, report), range(len(report))))
        if any(is_safe(variant) for variant in report_variants):
            count_safe += 1
    return count_safe


if __name__ == "__main__":
    with open("input/day02.txt") as f:
        puzzle_input = f.read()
    result = solve(puzzle_input)
    print(f"Result: {result}")
    result = solve_part2(puzzle_input)
    print(f"Result: {result}")
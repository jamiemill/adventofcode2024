def parse(input_data:str) ->list[list[int]]:
    lines = input_data.splitlines()
    return [list(map(int, l.split())) for l in lines]

def range_ok(pair):
    l,r = pair
    return 0 < abs(l-r) < 4

def is_safe(report):
    pairs = list(zip(report, report[1:])) # call list to avoid having a generator that gets exhausted and can't be reused
    is_increasing = all(r >= l for l,r in pairs)
    is_decreasing = all(r <= l for l,r in pairs)
    differences_are_ok = all(range_ok(pair) for pair in pairs)
    return (is_increasing or is_decreasing) and differences_are_ok


def solve(input_data:str) -> int:
    reports = parse(input_data)
    return sum(is_safe(report) for report in reports)

def remove_item_at_index(idx, lst):
    return lst[:idx] + lst[idx+1:]

def solve_part2(input_data:str) -> int:
    reports = parse(input_data)
    count_safe = 0
    for report in reports:
        report_variants = [report] + [remove_item_at_index(i, report) for i in range(len(report))]
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
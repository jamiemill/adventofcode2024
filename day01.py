def parse(input_data):
    lines = input_data.splitlines()
    first_list = []
    second_list = []
    for line in lines:
        [left, right] = line.split()
        first_list.append(int(left))
        second_list.append(int(right))
    return [first_list, second_list]


def solve(input_data:str) -> int:
    [first_list, second_list] = parse(input_data)
    first_list.sort()
    second_list.sort()
    return sum(abs(l-r) for l,r in zip(first_list, second_list))

def solve_part2(input_data:str) -> int:
    [first_list, second_list] = parse(input_data)
    return sum(item * second_list.count(item) for item in first_list)



if __name__ == "__main__":
    with open("input/day01.txt") as f:
        puzzle_input = f.read()
    result = solve(puzzle_input)
    print(f"Result: {result}")
    result = solve_part2(puzzle_input)
    print(f"Result: {result}")
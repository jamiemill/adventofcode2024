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
    zipped = zip(first_list, second_list)
    summed = sum(map(lambda pair: abs(pair[0] - pair[1]), zipped))
    return summed

def solve_part2(input_data:str) -> int:
    [first_list, second_list] = parse(input_data)
    score = 0
    for item in first_list:
        score += item * second_list.count(item)
    return score



if __name__ == "__main__":
    with open("input/day01.txt") as f:
        puzzle_input = f.read()
    result = solve(puzzle_input)
    print(f"Result: {result}")
    result = solve_part2(puzzle_input)
    print(f"Result: {result}")
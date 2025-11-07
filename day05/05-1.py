def to_int(digits: str) -> int | None:
    if len(digits) == 0:
        return None

    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    result = 0
    for num in digits:
        if num not in numbers:
            return None
        result = result * 10 + numbers.index(num)

    return result


def main() -> None:
    data = []
    with open("05-input.txt", "r") as file:
        data = file.readlines()
        # clean \n
        data_edit = [line.rstrip() for line in data]

    seeds_str = data_edit[0].split(": ")[1].split(" ")
    min_count = None
    for seed in seeds_str:
        ret = process(data, to_int(seed))
        if min_count is None or ret < min_count:
            min_count = ret

    print("-----")
    print(min_count)


def process(data, seed):
    block_process = False

    for index, line in enumerate(data):
        if index == 0:
            continue
        if line == "\n":
            continue

        line = line.rstrip()
        if ":" not in line:
            if not block_process:
                nums = line.split(" ")
                if to_int(nums[1]) <= seed < (to_int(nums[1]) + to_int(nums[2])):
                    block_process = True
                    seed = to_int(nums[0]) + seed - to_int(nums[1])
        else:
            block_process = False

    return seed

if __name__ == "__main__":
    main()

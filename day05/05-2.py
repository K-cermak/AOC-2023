def main() -> None:
    data = []
    with open("05-input.txt", "r") as file:
        data = file.readlines()
        # clean \n
        data_edit = [line.rstrip() for line in data]

    seeds_str = data_edit[0].split(": ")[1].split(" ")
    
    # remove new line and first index from data
    data.pop(0)
    for i in range(len(data) - 1, -1, -1):
        if data[i] == "\n":
            data.pop(i)
        else:
            data[i] = data[i].rstrip()

    intervals = []
    min_count = None

    for i in range(0, len(seeds_str), 2):
        seed_start = int(seeds_str[i])
        seed_end = seed_start + int(seeds_str[i + 1])
        intervals.append((seed_start, seed_end))

    for index, interval in enumerate(intervals):
        start, end = interval

        ret, limit = process(data, start)
        if min_count is None or ret < min_count:
            min_count = ret

        if start + limit >= end:
            ret, _ = process(data, end)
            if min_count is None or ret < min_count:
                min_count = ret
        else:
            ret, _ = process(data, start + limit)
            if min_count is None or ret < min_count:
                min_count = ret

            intervals[index] = (start, start + limit)
            intervals.append((start + limit + 1, end))

    print("-----")
    print(min_count)


def process(data, seed):
    block_process = False
    max_limit = 9999999999999999999 # scuffed
    maybe_limit = 9999999999999999999 # scuffed

    for line in data:
        if ":" not in line:
            if not block_process:
                nums = line.split(" ")
                first = int(nums[0])
                two = int(nums[1])
                three = int(nums[2])

                if two <= seed < (two + three):
                    new_limit = (two + three) - seed
                    if new_limit < max_limit:
                        max_limit = new_limit

                    block_process = True
                    seed = first + seed - two


                elif seed < two and (two - seed) < maybe_limit:
                    maybe_limit = two - seed - 1

        else:
            if not block_process and maybe_limit < max_limit:
                max_limit = maybe_limit

            block_process = False

    return seed, max_limit

if __name__ == "__main__":
    main()

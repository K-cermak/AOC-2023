# absolutely not optimized, but probably would work, but crushed on my server (48 threads, 128 GB of RAM), so :)

import multiprocessing

NUM_OF_PROCESS = 8

def line_gen(clue, size, sub_gen):
    if size == 0:
        return [[]]

    if len(clue) == 0:
        return [[0 for _ in range(size)]]

    variants = []
    max_zeros = size - sum(clue) - len(clue) + 1

    if max_zeros < 0:
        return []

    lines_builder(clue, [0], size - 1, variants, sub_gen)
    lines_builder(clue, [1], size - 1, variants, sub_gen)

    return len(variants)


def lines_builder(clue, state, size_left, variants, sub_gen):
    if size_left == 0:
        variants.append(state)
        return

    pos_data = sub_gen[len(state)]

    if (pos_data == 0 or pos_data == 2) and clue_correspond(clue, state + [0], size_left - 1):
        lines_builder(clue, state + [0], size_left - 1, variants, sub_gen)

    if (pos_data == 1 or pos_data == 2) and clue_correspond(clue, state + [1], size_left - 1):
        lines_builder(clue, state + [1], size_left - 1, variants, sub_gen)


def clue_correspond(clue, line, size_left):
    groups = []
    count = 0

    for pixel in line:
        if pixel == 1:
            count += 1
        elif count > 0:
            groups.append(count)
            count = 0

    # add rest
    if count > 0:
        groups.append(count)

    if len(groups) == 0 and len(clue) == 0:
        return size_left == 0

    if size_left == 0:
        return clue == groups

    size_lim = len(clue) - len(groups)
    if size_lim < 0:
        return False

    count = 0
    for i in range(1, size_lim + 1):
        count += clue[-i] + 1

    if line[-1] == 0:
        count -= 1

    if count > size_left:
        return False

    for i in range(len(groups)):
        if (i < len(groups) - 1 and
           groups[i] != clue[i]) or groups[i] > clue[i]:
            return False

    return True



def main() -> None:
    data = []
    with open("12-input.txt", "r") as file:
        data = file.readlines()
        # clean \n
        data = [line.rstrip() for line in data]


    clues = []
    sizes = []
    prefixes = []

    for line in data:
        splitted = line.split(" ")
        dupl_first = splitted[0]
        dupl_sec = splitted[1]

        for _ in range(4):
            splitted[0] += "?" + dupl_first
            splitted[1] += "," + dupl_sec

        clue = splitted[1].split(",")
        for i in range(len(clue)):
            clue[i] = int(clue[i])
        
        # 0 = ?
        # 1 = #
            
        prefix = []
        for char in splitted[0]:
            if char == "#":
                prefix.append(1)
            elif char == ".":
                prefix.append(0)
            else:
                prefix.append(2)

        clues.append(clue)
        sizes.append(len(splitted[0]))
        prefixes.append(prefix)


    with multiprocessing.Pool(processes=NUM_OF_PROCESS) as pool:
        results = pool.starmap(line_gen, zip(clues, sizes, prefixes))
    print(results)
    print(sum(results))


def mapper(char):
    if char == ".":
        return 0
    if char == "#":
        return 1


if __name__ == "__main__":
    main()
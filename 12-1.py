def line_gen(clue, size, starting_with):
    if size == 0:
        return [[]]

    if len(clue) == 0:
        return [[0 for _ in range(size)]]

    variants = []
    max_zeros = size - sum(clue) - len(clue) + 1

    if max_zeros < 0:
        return []

    if len(starting_with) == 0:
        lines_builder(clue, [0], size - 1, variants)
        lines_builder(clue, [1], size - 1, variants)
    else:
        lines_builder(clue, starting_with, size - len(starting_with), variants)

    return variants


def lines_builder(clue, state, size_left, variants):
    if size_left == 0:
        variants.append(state)
        return

    if clue_correspond(clue, state + [0], size_left - 1):
        lines_builder(clue, state + [0], size_left - 1, variants)

    if clue_correspond(clue, state + [1], size_left - 1):
        lines_builder(clue, state + [1], size_left - 1, variants)


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

    summary = 0
    for line in data:
        splitted = line.split(" ")
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
                break

        variants = line_gen(clue, len(splitted[0]), prefix)
        for variant in variants:
            is_valid = True
            for i in range(len(variant)):
                if splitted[0][i] == "?":
                    continue
                if mapper(splitted[0][i]) != variant[i]:
                    is_valid = False
                    break
            
            if is_valid:
                summary += 1

    print(summary)

def mapper(char):
    if char == ".":
        return 0
    if char == "#":
        return 1


if __name__ == "__main__":
    main()
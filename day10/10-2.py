import sys
sys.setrecursionlimit(100000)

# ━     -
# ┃     |
# ┗     L
# ┛     J
# ┓     7
# ┏     F

S_ACTUAL_CHAR = "┗"

def main() -> None:
    data = []
    with open("10-input.txt", "r", encoding="utf8") as file:
        data = file.readlines()
        # clean \n
        data = [line.rstrip() for line in data]

    data_copy = data
    data = []
    start_x = None
    start_y = None

    for y, line in enumerate(data_copy):
        chars = []
        for x, char in enumerate(line):
            chars.append(char)
            if char == "S":
                start_x = x
                start_y = y
        data.append(chars)

    mov_x, mov_y = is_connect_to(start_x, start_y, data)

    # tuples of (Y, X)
    loop_tiles = set()
    find_way(mov_x, mov_y, start_x, start_y, data, loop_tiles)
    loop_tiles.add((start_y, start_x))
    
    loop_tiles_sort = list(loop_tiles)
    loop_tiles_sort.sort()
    data[start_y][start_x] = S_ACTUAL_CHAR
    

    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if (y, x) not in loop_tiles_sort:
                data[y][x] = "."

    in_area_sum = 0

    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if data[y][x] == ".":
                in_correct_y = False
                seen = {}
                skip_index = set()

                for y_tile, x_tile in loop_tiles_sort:
                    if x_tile in skip_index:
                        continue

                    if y_tile == y and x_tile < x:
                        in_correct_y = True

                        if data[y_tile][x_tile] != "." and data[y_tile][x_tile] != "━":
                            is_not_returning = True

                            if data[y_tile][x_tile] == "┗":
                                for i in range(x_tile + 1, len(data[0])):
                                    if data[y_tile][i] == "━":
                                        continue
                                    if data[y_tile][i] == "┛":
                                        is_not_returning = False
                                        skip_index.add(i)
                                    break

                            if data[y_tile][x_tile] == "┏":
                                for i in range(x_tile + 1, len(data[0])):
                                    if data[y_tile][i] == "━":
                                        continue
                                    if data[y_tile][i] == "┓":
                                        is_not_returning = False
                                        skip_index.add(i)
                                    break

                            if is_not_returning:
                                seen[data[y_tile][x_tile]] = seen.get(data[y_tile][x_tile], 0) + 1

                    if in_correct_y and (y != y_tile or x_tile > x):
                        break

                if is_inside(seen):
                    in_area_sum += 1

    print(in_area_sum)

def is_inside(seen):
    count = 0

    for key, value in seen.items():
        if key == "┃":
            count += value * 1
        elif key == "┗":
            count += value * 0.5
        elif key == "┛":
            count += value * 0.5
        elif key == "┓":
            count += value * 0.5
        elif key == "┏":
            count += value * 0.5

    return count % 2 != 0
        


def find_way(x, y, last_x, last_y, data, loop_tiles):
    new_x, new_y = continue_to(x, y, last_x, last_y, data)
    if new_x is None or new_y is None:
        return
    
    loop_tiles.add((y, x))
    find_way(new_x, new_y, x, y, data, loop_tiles)


def is_connect_to(x, y, data):
    if x + 1 < len(data[0]):
        if data[y][x + 1] == "━" or data[y][x + 1] == "┛" or data[y][x + 1] == "┓":
            return (x + 1, y)
    if x - 1 >= 0:
        if data[y][x - 1] == "━" or data[y][x - 1] == "┗" or data[y][x - 1] == "┏":
            return (x - 1, y)
    if y + 1 < len(data):
        if data[y + 1][x] == "┃" or data[y + 1][x] == "┏" or data[y + 1][x] == "┓":
            return (x, y + 1)
    if y - 1 >= 0:
        if data[y - 1][x] == "┃" or data[y - 1][x] == "┗" or data[y - 1][x] == "┛":
            return (x, y - 1)


def continue_to(x, y, x_dis, y_dis, data):
    new_x = None
    new_y = None

    if data[y][x] == "━":
        if x + 1 < len(data[0]) and x + 1 != x_dis:
            new_x = x + 1
            new_y = y
        elif x - 1 >= 0 and x - 1 != x_dis:
            new_x = x - 1
            new_y = y
    
    if data[y][x] == "┃":
        if y + 1 < len(data) and y + 1 != y_dis:
            new_x = x
            new_y = y + 1
        elif y - 1 >= 0 and y - 1 != y_dis:
            new_x = x
            new_y = y - 1

    
    if data[y][x] == "┗":
        if x + 1 < len(data[0]) and x + 1 != x_dis:
            new_x = x + 1
            new_y = y
        elif y - 1 >= 0 and y - 1 != y_dis:
            new_x = x
            new_y = y - 1

    if data[y][x] == "┛":
        if x - 1 >= 0 and x - 1 != x_dis:
            new_x = x - 1
            new_y = y
        elif y - 1 >= 0 and y - 1 != y_dis:
            new_x = x
            new_y = y - 1

    if data[y][x] == "┓":
        if x - 1 >= 0 and x - 1 != x_dis:
            new_x = x - 1
            new_y = y
        elif y + 1 < len(data) and y + 1 != y_dis:
            new_x = x
            new_y = y + 1

    if data[y][x] == "┏":
        if x + 1 < len(data[0]) and x + 1 != x_dis:
            new_x = x + 1
            new_y = y
        elif y + 1 < len(data) and y + 1 != y_dis:
            new_x = x
            new_y = y + 1

    return new_x, new_y




if __name__ == "__main__":
    main()

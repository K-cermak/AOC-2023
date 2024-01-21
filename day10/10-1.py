import sys
sys.setrecursionlimit(100000)

# ━     -
# ┃     |
# ┗     L
# ┛     J
# ┓     7
# ┏     F


def main() -> None:
    data = []
    with open("10-input.txt", "r") as file:
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
    distance = find_way(mov_x, mov_y, start_x, start_y, data, 1)
    print(distance // 2)


def find_way(x, y, last_x, last_y, data, distance):
    new_x, new_y = continue_to(x, y, last_x, last_y, data)
    if new_x is None or new_y is None:
        return distance
    
    data[y][x] = distance
    return find_way(new_x, new_y, x, y, data, distance + 1)


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

# would work, but too slow

import sys
sys.setrecursionlimit(10000000)

def main() -> None:
    data = []
    with open("21-input.txt", "r") as file:
        data = file.readlines()
        # clean \n
        data = [line.rstrip() for line in data]

    s_location = None
    data_array = []
    for line in data:
        sub_array = []
        for char in line:
            if char == "S":
                s_location = (len(sub_array), len(data_array))
            sub_array.append(char)
        data_array.append(sub_array)

    x, y = s_location
    current_locations = set()
    go(x, y, data_array, current_locations, 64)
    print(len(current_locations))


def go(pos_x, pos_y, data, current_locations, distance):
    if pos_x >= len(data[0]) or pos_y >= len(data) or pos_x < 0 or pos_y < 0:
        return
    if data[pos_y][pos_x] == "#":
        return
    if distance == 0:
        return pos_x, pos_y
    

    left = go(pos_x - 1, pos_y, data, current_locations, distance - 1)
    right = go(pos_x + 1, pos_y, data, current_locations, distance - 1)
    up = go(pos_x, pos_y - 1, data, current_locations, distance - 1)
    down = go(pos_x, pos_y + 1, data, current_locations, distance - 1)

    if left is not None and distance == 1:
        current_locations.add(left)
    if right is not None and distance == 1:
        current_locations.add(right)
    if up is not None and distance == 1:
        current_locations.add(up)
    if down is not None and distance == 1:
        current_locations.add(down)


if __name__ == "__main__":
    main()
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
    with open("11-input.txt", "r") as file:
        data = file.readlines()
        # clean \n
        data = [line.rstrip() for line in data]

    data_copy = data
    data = []

    for line in data_copy:
        chars = []
        for char in line:
            chars.append(char)
        data.append(chars)

    distance_sum = 0
    all_stars = set()
    visited = set()
    voids_x = set()
    voids_y = set()

    for y, line in enumerate(data):
        is_free = True
        for char in line:
            if char == "#":
                is_free = False
                break

        if is_free:
            voids_y.add(y)

    for i in range(len(data[0]) - 1, -1, -1):
        is_free = True
        for j in range(len(data)):
            if data[j][i] == "#":
                is_free = False
                break

        if is_free:
            voids_x.add(i)

    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if char == "#":
                all_stars.add((x, y))
    
    for star in all_stars:
        x, y = star
        distance_sum += find_way(x, y, all_stars - {star}, visited, voids_x, voids_y)

    print(distance_sum)


def find_way(x, y, all_stars, visited, voids_x, voids_y):
    distance = 0
    for x_dest, y_dest in all_stars:
        if (x, y, x_dest, y_dest) in visited or (x_dest, y_dest, x, y) in visited:
            continue
        visited.add((x, y, x_dest, y_dest))
        distance += (abs(x - x_dest) + abs(y - y_dest)) + hitted_empty(x, y, x_dest, y_dest, voids_x, voids_y)

    return distance


def hitted_empty(x_first, y_first, x_sec, y_sec, voids_x, voids_y):
    how_many = 0
    multiplier = 999999

    for x in voids_x:
        if x_first < x < x_sec:
            how_many += 1
        if x_sec < x < x_first:
            how_many += 1
    
    for y in voids_y:
        if y_first < y < y_sec:
            how_many += 1
        if y_sec < y < y_first:
            how_many += 1
    
    return how_many * multiplier
        



if __name__ == "__main__":
    main()

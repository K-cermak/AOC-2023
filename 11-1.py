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
    expanded_data = []

    for line in data_copy:
        chars = []
        for char in line:
            chars.append(char)
        data.append(chars)

    # check line
    for line in data:
        is_free = True
        for char in line:
            if char == "#":
                is_free = False
                break

        expanded_data.append(line.copy())
        if is_free:
            expanded_data.append(line.copy())

    # check cols
    for i in range(len(data[0]) - 1, -1, -1):
        is_free = True
        for j in range(len(data)):
            if data[j][i] == "#":
                is_free = False
                break

        if is_free:
            for line in expanded_data:
                line.insert(i + 1, ".")

    distance_sum = 0
    all_stars = set()
    visited = set()

    for y, line in enumerate(expanded_data):
        for x, char in enumerate(line):
            if char == "#":
                all_stars.add((x, y))
    
    for star in all_stars:
        x, y = star
        distance_sum += find_way(x, y, all_stars - {star}, visited)

    print(distance_sum)


def find_way(x, y, all_stars, visited):
    distance = 0
    for x_dest, y_dest in all_stars:
        if (x, y, x_dest, y_dest) in visited or (x_dest, y_dest, x, y) in visited:
            continue
        visited.add((x, y, x_dest, y_dest))
        distance += (abs(x - x_dest) + abs(y - y_dest))

    return distance






if __name__ == "__main__":
    main()

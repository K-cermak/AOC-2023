import sys
sys.setrecursionlimit(10000000)

def main() -> None:
    data = []
    with open("16-input.txt", "r") as file:
        data = file.readlines()
        # clean \n
        data = [line.rstrip() for line in data]

    data_array = []
    for line in data:
        sub_array = []
        for char in line:
            sub_array.append(char)
        data_array.append(sub_array)

    best = 0
    # top and bottom
    for i in range(len(data_array[0])):
        visited = set()
        beam_search(data_array, i, -1, 2, visited, set())
        if len(visited) > best:
            best = len(visited)

        visited = set()
        beam_search(data_array, i, len(data_array), 4, visited, set())
        if len(visited) > best:
            best = len(visited)

    # left and right
    for i in range(len(data_array)):
        visited = set()
        beam_search(data_array, -1, i, 1, visited, set())
        if len(visited) > best:
            best = len(visited)

        visited = set()
        beam_search(data_array, len(data_array[0]), i, 3, visited, set())
        if len(visited) > best:
            best = len(visited)

    print(best)


def beam_search(data, pos_x, pos_y, direction, visited, visited_direction):
    if (pos_x, pos_y, direction) in visited_direction:
        return
    
    if pos_x != -1 and pos_y != -1 and pos_x != len(data[0]) and pos_y != len(data):
        visited.add((pos_x, pos_y))
        visited_direction.add((pos_x, pos_y, direction))

    # 1 for right, 2 for down, 3 for left, 4 for up
    if direction == 1:
        pos_x += 1
    elif direction == 2:
        pos_y += 1
    elif direction == 3:
        pos_x -= 1
    elif direction == 4:
        pos_y -= 1

    # base
    if pos_x < 0 or pos_x >= len(data[0]) or pos_y < 0 or pos_y >= len(data):
        return

    if data[pos_y][pos_x] == ".":
        beam_search(data, pos_x, pos_y, direction, visited, visited_direction)
    elif data[pos_y][pos_x] == "/":
        if direction == 1:
            direction = 4
        elif direction == 2:
            direction = 3
        elif direction == 3:
            direction = 2
        elif direction == 4:
            direction = 1
        beam_search(data, pos_x, pos_y, direction, visited, visited_direction)
    elif data[pos_y][pos_x] == "\\":
        if direction == 1:
            direction = 2
        elif direction == 2:
            direction = 1
        elif direction == 3:
            direction = 4
        elif direction == 4:
            direction = 3
        beam_search(data, pos_x, pos_y, direction, visited, visited_direction)
    elif data[pos_y][pos_x] == "-":
        if direction == 1 or direction == 3:
            beam_search(data, pos_x, pos_y, direction, visited, visited_direction)
        else:
            beam_search(data, pos_x, pos_y, 1, visited, visited_direction)
            beam_search(data, pos_x, pos_y, 3, visited, visited_direction)
    elif data[pos_y][pos_x] == "|":
        if direction == 2 or direction == 4:
            beam_search(data, pos_x, pos_y, direction, visited, visited_direction)
        else:
            beam_search(data, pos_x, pos_y, 2, visited, visited_direction)
            beam_search(data, pos_x, pos_y, 4, visited, visited_direction)


if __name__ == "__main__":
    main()
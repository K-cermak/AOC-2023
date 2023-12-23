import sys
sys.setrecursionlimit(10000000)

def main() -> None:
    data = []
    with open("18-input.txt", "r") as file:
        data = file.readlines()
        # clean \n
        data = [line.rstrip() for line in data]

    for index, line in enumerate(data):
        data[index] = line.split(" (")[0]
        data[index] = data[index].split(" ")

    print(data)
    
    pos_x = pos_y = 0
    all_conns = []
    for direction, dest in data:
        last_x = pos_x
        last_y = pos_y
        if direction == "R":
            pos_x += int(dest)
        elif direction == "L":
            pos_x -= int(dest)
        elif direction == "U":
            pos_y -= int(dest)
        elif direction == "D":
            pos_y += int(dest)

        all_conns.append(((last_x, last_y), (pos_x, pos_y)))


    most_x = most_y = 0
    lowest_x = lowest_y = 0
    for start, _ in all_conns:
        x, y = start
        if x > most_x:
            most_x = x
        if y > most_y:
            most_y = y
        if x < lowest_x:
            lowest_x = x
        if y < lowest_y:
            lowest_y = y

    for index, inst in enumerate(all_conns):
        first, sec = inst
        x1, y1 = first
        x2, y2 = sec
        all_conns[index] = ((x1 - lowest_x, y1 - lowest_y), (x2 - lowest_x, y2 - lowest_y))

    map = [["." for _ in range(-lowest_x + most_x + 1)] for _ in range(-lowest_y + most_y + 1)]
    for start, end in all_conns:
        x1, y1 = start
        x2, y2 = end
        if x1 == x2:
            if y1 > y2:
                y1, y2 = y2, y1
            for y in range(y1, y2 + 1):
                map[y][x1] = "#"
        elif y1 == y2:
            if x1 > x2:
                x1, x2 = x2, x1
            for x in range(x1, x2 + 1):
                map[y1][x] = "#"

    first, _ = all_conns[0]
    x, y = first
    paint(map, x + 1, y + 1)
    

    count = 0
    for row in map:
        for char in row:
            if char == "#":
                count += 1   

    print(count)
        


def paint(map, x, y):
    if map[y][x] == ".":
        map[y][x] = "#"
    else:
        return

    if y > 0:
        paint(map, x, y - 1)
    if y < len(map) - 1:
        paint(map, x, y + 1)
    if x > 0:
        paint(map, x - 1, y)
    if x < len(map[0]) - 1:
        paint(map, x + 1, y)
    





if __name__ == "__main__":
    main()
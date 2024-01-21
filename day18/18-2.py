import sys, math
sys.setrecursionlimit(999999999)

def main() -> None:
    data = []
    with open("18-input.txt", "r") as file:
        data = file.readlines()
        # clean \n
        data = [line.rstrip() for line in data]


    path_value = 0
    for index, line in enumerate(data):
        data[index] = line.split(" (")[1]
        # remove first char
        data[index] = data[index][1:]
        direction = data[index][len(data[index]) - 2]
        if direction == "0":
            direction = "R"
        elif direction == "1":
            direction = "D"
        elif direction == "2":
            direction = "L"
        elif direction == "3":
            direction = "U"

        data[index] = data[index][:-2]
        data[index] = int(data[index], 16)
        path_value += data[index]
        data[index] = (direction, data[index])

    pos_x = pos_y = 0
    all_conns = []
    for direction, dest in data:
        if direction == "R":
            pos_x += dest
        elif direction == "L":
            pos_x -= dest
        elif direction == "U":
            pos_y -= dest
        elif direction == "D":
            pos_y += dest

        all_conns.append([pos_x, pos_y])


    area = area_calc(all_conns)
    print(math.trunc(area + ((path_value) // 2) + 1))


# Shoelace Algorithm
def area_calc(vertices):
    sum1 = sum2 = 0
    
    for i in range(0, len(vertices) - 1):
        sum1 += vertices[i][0] * vertices[i + 1][1]
        sum2 += vertices[i][1] * vertices[i + 1][0]

    sum1 += vertices[-1][0] * vertices[0][1]   
    sum2 += vertices[0][0] * vertices[-1][1]   
    
    area = abs(sum1 - sum2) / 2
    return area

    

if __name__ == "__main__":
    main()
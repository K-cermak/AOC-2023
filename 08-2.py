def main() -> None:
    data = []
    with open("08-input.txt", "r") as file:
        data = file.readlines()
        # clean \n
        data = [line.rstrip() for line in data]

    data_dict = {}
    current = []

    for index, line in enumerate(data):
        if index < 2:
            continue

        instruction = line.split(" = ")
        possible_to = instruction[1].split(", ")
        possible_to[0] = possible_to[0][1:]
        possible_to[1] = possible_to[1][:-1]
    
        data_dict[instruction[0]] = [possible_to[0], possible_to[1]]

        if instruction[0][2] == "A":
            current.append(instruction[0])

    directions = data[0]
    iterations = []


    for index, c in enumerate(current):
        iteration = 0
        while c[2] != "Z":
            c = process_line(c, directions[iteration % len(directions)], data_dict)
            iteration += 1
        iterations.append(iteration)

    iterations.sort()
    print(iterations)


def process_line(current, direction, data_dict):
    if direction == "L":
        return data_dict[current][0]
    return data_dict[current][1]




if __name__ == "__main__":
    main()

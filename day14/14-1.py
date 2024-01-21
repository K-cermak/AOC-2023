def main() -> None:
    data = []
    with open("14-input.txt", "r") as file:
        data = file.readlines()
        # clean \n
        data = [line.rstrip() for line in data]

    data_array = []
    for line in data:
        sub_array = []
        for char in line:
            sub_array.append(char)
        data_array.append(sub_array)


    something_moved = True

    while something_moved:
        something_moved = False

        for i in range(len(data_array) - 1, 0, -1):
            for j in range(len(data_array[0])):
                if data_array[i][j] == "O" and data_array[i - 1][j] == ".":
                    something_moved = True
                    data_array[i][j] = "."
                    data_array[i - 1][j] = "O"
    
    count = 0

    for row, line in enumerate(data_array):
        for char in line:
            if char == "O":
                count += len(data_array) - row

    print(count)




if __name__ == "__main__":
    main()
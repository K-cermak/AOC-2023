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


    history = {}
    limit = -1

    for iter in range(1000000000 * 4):
        if limit != -1:
            limit -= 1
            if limit == -1:
                break

        something_moved = True

        while something_moved:
            something_moved = False

            if iter % 4 == 0: # bad
                for i in range(len(data_array) - 1, 0, -1):
                    for j in range(len(data_array[0])):
                        if data_array[i][j] == "O" and data_array[i - 1][j] == ".":
                            something_moved = True
                            data_array[i][j] = "."
                            data_array[i - 1][j] = "O"
            elif iter % 4 == 2: # bad
                for i in range(0, len(data_array) - 1):
                    for j in range(len(data_array[0])):
                        if data_array[i][j] == "O" and data_array[i + 1][j] == ".":
                            something_moved = True
                            data_array[i][j] = "."
                            data_array[i + 1][j] = "O"

            elif iter % 4 == 1: # bad
                for j in range(len(data_array[0]) - 1, 0, -1):
                    for i in range(len(data_array)):
                        if data_array[i][j] == "O" and data_array[i][j - 1] == ".":
                            something_moved = True
                            data_array[i][j] = "."
                            data_array[i][j - 1] = "O"
            elif iter % 4 == 3: # bad
                for j in range(len(data_array[0]) - 1):
                    for i in range(len(data_array)):
                        if data_array[i][j] == "O" and data_array[i][j + 1] == ".":
                            something_moved = True
                            data_array[i][j] = "."
                            data_array[i][j + 1] = "O"


        if iter % 4 == 0 and limit == -1:
            query_search = tuple(tuple(line) for line in data_array)
            if query_search in history:
                iter_last = history[query_search]
                iter_diff = (iter // 4) - iter_last

                limit_tmp = ((1000000000 - iter_last) // iter_diff)
                limit = (((1000000000 - iter_last) - (limit_tmp * iter_diff)) * 4) - 1

            else:
                history[query_search] = iter // 4


    count = 0
    for row, line in enumerate(data_array):
        for char in line:
            if char == "O":
                count += len(data_array) - row

    print(count)


if __name__ == "__main__":
    main()
def main() -> None:
    data = []
    with open("09-input.txt", "r") as file:
        data = file.readlines()
        # clean \n
        data = [line.rstrip() for line in data]

    summary = 0

    for line in data:
        all_lines = []
        
        nums = line.split(" ")
        first_line = []

        for num in nums:
            first_line.append(int(num))

        all_lines.append(first_line)
        process_list(all_lines)
        process_back(all_lines)

        summary += all_lines[0][0]

    print(summary)


def process_list(line_list):
    working_list = line_list[-1]
    new_sublist = []

    all_zeros = True

    for i in range(1, len(working_list)):
        new_sublist.append(working_list[i] - working_list[i - 1])
        if working_list[i] - working_list[i - 1] != 0:
            all_zeros = False
    
    line_list.append(new_sublist)
    if not all_zeros:
        process_list(line_list)
    else:
        new_sublist.insert(0, 0)


def process_back(line_list):
    for i in range(len(line_list) - 1, 0, -1):
        bottom_num = line_list[i][0]
        top_list = line_list[i - 1]
        top_list.insert(0, top_list[0] - bottom_num)


if __name__ == "__main__":
    main()

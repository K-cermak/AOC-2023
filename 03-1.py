def to_int(digits: str) -> int | None:
    if len(digits) == 0:
        return None

    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    result = 0
    for num in digits:
        if num not in numbers:
            return None
        result = result * 10 + numbers.index(num)

    return result


def main() -> None:
    data = []
    with open("03-input.txt", "r") as file:
        for line in file:
            line = line.strip()
            data.append([])
            
            for char in line:
                data[-1].append(char)

    count = 0

    for line_index, line in enumerate(data):
        in_num = False
        index_Start = 0

        for index, char in enumerate(line):
            if char.isdigit():
                if not in_num:
                    index_Start = index
                in_num = True
            else:
                if in_num:
                    in_num = False
                    num = check_validity(index_Start, index - 1, line_index, data)
                    if num is not None:
                        count += num

        # end of line
        if in_num:
            num = check_validity(index_Start, index, line_index, data)
            if num is not None:
                count += num


    print(count)
         


def check_validity(start_index, end_index, line, data):
    nums = ""
    something_detect = False

    if start_index - 1 >= 0:
        if data[line][start_index - 1] != ".":
            something_detect = True
        if line - 1 >= 0:
            if data[line - 1][start_index - 1] != ".":
                something_detect = True
        if line + 1 < len(data):
            if data[line + 1][start_index - 1] != ".":
                something_detect = True


    if end_index + 1 < len(data[line]):
        if data[line][end_index + 1] != ".":
            something_detect = True
        if line - 1 >= 0:
            if data[line - 1][end_index + 1] != ".":
                something_detect = True
        if line + 1 < len(data):
            if data[line + 1][end_index + 1] != ".":
                something_detect = True

    for i in range(start_index, end_index + 1):        
        nums += data[line][i]

        if line - 1 >= 0:
            if data[line - 1][i] != ".":
                something_detect = True
        if line + 1 < len(data):
            if data[line + 1][i] != ".":
                something_detect = True

    if something_detect:
        return to_int(nums)
    
    return None
    


if __name__ == "__main__":
    main()

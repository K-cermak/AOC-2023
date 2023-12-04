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
    with open("01-input.txt", "r") as file:
        data = file.readlines()
        # clean \n
        data = [line.rstrip() for line in data]

    count = 0
    for line in data:
        left_num = ""
        right_num = ""
        for index, char in enumerate(line):
            if char.isdecimal():
                if left_num == "":
                    left_num = char
                right_num = char
            else:
                pos_num = is_valid_number(line, index)
                if pos_num is not None:
                    if left_num == "":
                        left_num = pos_num
                    right_num = pos_num

        count += to_int(left_num + right_num)

    print(count)

def is_valid_number(line, start_pos):
    code_table = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

    string = line[start_pos]
    for i in range(1, 5):
        if start_pos + i >= len(line):
            return None

        string += line[start_pos + i]
        num = code_table.get(string)
        if num is not None:
            return num
    
    return None



if __name__ == "__main__":
    main()

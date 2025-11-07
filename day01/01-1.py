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
        for char in line:
            if char.isdecimal():
                if left_num == "":
                    left_num = char
                right_num = char

        print(left_num + right_num)
        count += to_int(left_num + right_num)

    print(count)
         



if __name__ == "__main__":
    main()

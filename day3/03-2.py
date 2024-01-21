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
        for index, char in enumerate(line):
            if char == "*":
                res = detect(line_index, index, data)
                if res is not None:
                    count += res

    print(count)


def detect(line, index, data):
    nums = set()
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue

            num = get_num(line + i, index + j, data)
            if num is not None:
                nums.add(num)
    
    if len(nums) == 2:
        sum_ = 1
        for num in nums:
            sum_ *= num
        return sum_

def get_num(line, index, data):
    if line < 0 or line >= len(data):
        return None

    if index < 0 or index >= len(data[line]):
        return None

    if not data[line][index].isdecimal():
        return None

    num = data[line][index]
    l_index = index
    r_index = index
    while True:
        l_index += 1
        if l_index >= len(data[line]):
            break

        if data[line][l_index].isdecimal():
            num = num + data[line][l_index]
        else:
            break
    while True:
        r_index -= 1
        if r_index < 0:
            break

        if data[line][r_index].isdecimal():
            num = data[line][r_index] + num
        else:
            break

    return to_int(num)


if __name__ == "__main__":
    main()

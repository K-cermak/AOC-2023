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
    with open("02-input.txt", "r") as file:
        data = file.readlines()
        # clean \n
        data = [line.rstrip() for line in data]

    count = 0
    for line in data:
        count += line_worker(line)

    print(count)

def line_worker(line):
    red_max = 1
    blue_max = 1
    green_max = 1

    results = line.split(":")[1].strip().split("; ")
    for result in results:
        picks = result.split(", ")
        for pick in picks:
            pick = pick.split(" ")
            num =  to_int(pick[0])
            if pick[1] == "red" and num > red_max:
                red_max = num
            if pick[1] == "blue" and num > blue_max:
                blue_max = num 
            if pick[1] == "green" and num > green_max:
                green_max = num
    
    return red_max * blue_max * green_max
         



if __name__ == "__main__":
    main()

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
    with open("04-input.txt", "r") as file:
        data = file.readlines()
        # clean \n
        data = [line.rstrip() for line in data]

    count = 0
    for line in data:
        my_nums_set = set()
        all_nums_set = set()

        my_nums = line.split(" | ")[0].split(": ")[1].split(" ")
        all_nums = line.split(" | ")[1].split(" ")

        for i in range(len(my_nums)):
            if my_nums[i] != "":
                my_nums_set.add(to_int(my_nums[i].strip()))
        
        for i in range(len(all_nums)):
            if all_nums[i] != "":
                all_nums[i] = all_nums[i].strip()
                if to_int(all_nums[i]) in my_nums_set:
                    all_nums_set.add(to_int(all_nums[i]))

        subcount = 0
        for _ in all_nums_set:
            if subcount == 0:
                subcount += 1
            else:
                subcount *= 2
        
        count += subcount    


    print(count)
         


if __name__ == "__main__":
    main()

def main() -> None:
    data = []
    with open("15-input.txt", "r") as file:
        data = file.readlines()
        # clean \n
        data = [line.rstrip() for line in data]

    data = data[0].split(",")
    total_sum = 0

    for current_turn in data:
        subcount = 0

        for char in current_turn:
            subcount += ord(char)
            subcount *= 17
            subcount %= 256
        
        total_sum += subcount
    
    print(total_sum)

    




if __name__ == "__main__":
    main()
def main() -> None:
    data = []
    with open("13-input.txt", "r") as file:
        data = file.readlines()
        # clean \n
        data = [line.rstrip() for line in data]

    processed = []
    current_process = []

    for line in data:
        if line == "":
            processed.append(current_process)
            current_process = []
            continue
    
        char_list = []
        for char in line:
            char_list.append(char)
        current_process.append(char_list)

    processed.append(current_process)
    
    count = 0
    for game in processed:
        # horizontal
        for i in range(len(game) - 1):
            if game[i] == game[i + 1] and check_reflection(True, game, i):
                count += (i + 1) * 100
        
        # vertical
        for i in range(len(game[0]) - 1):
            left_row = []
            right_row = []
            for row in game:
                left_row.append(row[i])
                right_row.append(row[i + 1])
            if left_row == right_row and check_reflection(False, game, i):
                count += i + 1

    print(count)


def check_reflection(is_horizontal, game, i):
    if is_horizontal:
        left_index = i - 1
        right_index = i + 2
        while left_index >= 0 and right_index < len(game):
            if game[left_index] != game[right_index]:
                return False
            left_index -= 1
            right_index += 1

        return True
    
    else:
        top_index = i - 1
        bottom_index = i + 2
        while top_index >= 0 and bottom_index < len(game[0]):
            left_row = []
            right_row = []
            for row in game:
                left_row.append(row[top_index])
                right_row.append(row[bottom_index])
            if left_row != right_row:
                return False
            top_index -= 1
            bottom_index += 1

        return True



def mapper(char):
    if char == ".":
        return 0
    if char == "#":
        return 1


if __name__ == "__main__":
    main()
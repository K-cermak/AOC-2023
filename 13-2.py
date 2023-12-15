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
        subcount = 0
        orig_symmetry = get_symmetry(game, None)

        for index in range(len(game) * len(game[0])):
            change_game(game, index, True)

            """
            for line in game:
                for char in line:
                    print(char, end="")
                print()
            print()
            """
            
            symmetry = get_symmetry(game, orig_symmetry)
            if symmetry is None:
                continue

            is_horizontal, sym_index = symmetry

            if is_valid_solution(game, is_horizontal, sym_index):
                if is_horizontal:
                    subcount = (sym_index + 1) * 100
                else:
                    subcount = (sym_index + 1)

        if subcount != 0:
            count += subcount
        else:
            print(orig_symmetry)
            is_horizontal, sym_index = orig_symmetry
            if is_horizontal:
                count += (sym_index + 1) * 100
            else:
                count += (sym_index + 1)

    print(count)


    # too high: 54500
    # too low: 25864
    # 42381 not right

    # 36755


def change_game(game, index, rec_allow):
    if index != 0 and rec_allow:
        change_game(game, index - 1, False)

    row = index // len(game[0])
    col = index % len(game[0])

    if game[row][col] == ".":
        game[row][col] = "#"
    else:
        game[row][col] = "."

def get_symmetry(game, not_this_symmetry):
    # horizontal
    for i in range(len(game) - 1):
        if game[i] == game[i + 1] and is_valid_solution(game, True, i) and not_this_symmetry != (True, i):
            return (True, i)

    # vertical
    for col in range(len(game[0]) - 1):
        left_col = []
        right_col = []
        for row in game:
            left_col.append(row[col])
            right_col.append(row[col + 1])
        if left_col == right_col and is_valid_solution(game, False, col) and not_this_symmetry != (False, col):
            return (False, col)
        
    return None


def is_valid_solution(game, is_horizontal, i):
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




if __name__ == "__main__":
    main()
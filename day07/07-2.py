def main() -> None:
    data = []
    with open("07-input.txt", "r") as file:
        data = file.readlines()
        # clean \n
        data = [line.rstrip() for line in data]

    for index, line in enumerate(data):
        data[index] = line.split(" ")

    sorted = []
    skip_indexes = set()

    while len(skip_indexes) < len(data):
        min, min_index = find_min(data, skip_indexes)
        sorted.append(min)
        skip_indexes.add(min_index)

    sorted.reverse()
    score = 0

    for index, card in enumerate(sorted):
        score += int(card[1]) * (index + 1)

    print(score)



def find_min(data, skip_indexes):
    min = None
    strong_lvl = None
    min_index = None

    for index, line in enumerate(data):
        if index in skip_indexes:
            continue

        if min is None:
            min = line
            strong_lvl = strong_level_calc(line[0])
            min_index = index
            continue

        strong_lvl2 = strong_level_calc(line[0])
        if strong_lvl2 > strong_lvl:
            min = line
            strong_lvl = strong_lvl2
            min_index = index

        elif strong_lvl2 == strong_lvl:
            if which_is_stronger(line[0], min[0]) == 1:
                min = line
                strong_lvl = strong_lvl2
                min_index = index

    return min, min_index


def which_is_stronger(card1, card2):
    values = {"A": 14, "K": 13, "Q": 12, "T": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2, "J": 1}
    for index, char in enumerate(card1):
        if values[char] > values[card2[index]]:
            return 1
        elif values[char] < values[card2[index]]:
            return 2
        
    return 0


def joker_gen(card):
    new_name = card.replace("J", "[AKQT98765432]")
    alls = resolve_template(new_name)
    max = 0

    for item in alls:
        new_max = strong_level_calc(item)
        if new_max > max:
            max = new_max

    return max
    

def strong_level_calc(card):
    # if has J in 
    if "J" in card:
        return joker_gen(card)

    types_dict = {}
    for char in card:
        types_dict[char] = types_dict.get(char, 0) + 1

    # five of a kind
    if len(types_dict) == 1:
        return 7
    
    # four of a kind
    if len(types_dict) == 2:
        for key in types_dict:
            if types_dict[key] == 4:
                return 6
            
    # full house
    if len(types_dict) == 2:
        can_be_full_house = True
        for key in types_dict:
            if types_dict[key] != 3 and types_dict[key] != 2:
                can_be_full_house = False

        if can_be_full_house:
            return 5
        
    # three of a kind
    if len(types_dict) == 3:
        for key in types_dict:
            if types_dict[key] == 3:
                return 4
    
    # two pairs
    if len(types_dict) == 3:
        detected_pairs = 0
        for key in types_dict:
            if types_dict[key] == 2:
                detected_pairs += 1

        if detected_pairs == 2:
            return 3
        
    # one pair
    if len(types_dict) == 4:
        return 2
    
    # high card
    return 1


def resolve_template(template: str) -> set[str]:
    words: set[str] = set()
    in_bracket = False

    if len(template) == 0:
        words.add("")
        return words

    data_in_bracket = ""
    bef_bracket = ""

    for letter in template:
        if in_bracket and letter != "]":
            data_in_bracket += letter
        elif not in_bracket and letter != "[":
            bef_bracket += letter

        if letter == "[":
            in_bracket = True
        elif letter == "]":
            in_bracket = False
            old_words = words.copy()
            words = set()

            if len(data_in_bracket) == 0:
                continue

            for bracket_let in data_in_bracket:
                if len(old_words) == 0:
                    words.add(bef_bracket + bracket_let)

                for item in old_words:
                    words.add(item + bef_bracket + bracket_let)

            bef_bracket = ""
            data_in_bracket = ""

    if len(bef_bracket) > 0:
        if len(words) == 0:
            words.add(bef_bracket)
        else:
            old_words = words.copy()
            words = set()

            for item in old_words:
                words.add(item + bef_bracket)

    return words
    




if __name__ == "__main__":  
    main()
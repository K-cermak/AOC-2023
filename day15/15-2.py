def main() -> None:
    data = []
    with open("15-input.txt", "r") as file:
        data = file.readlines()
        # clean \n
        data = [line.rstrip() for line in data]

    data = data[0].split(",")
    boxes = [[] for _ in range(256)]
    
    for current_turn in data:
        hash = hash_calc(current_turn)
        if "=" in current_turn:
            add_to_box(boxes[hash], current_turn)
        else:
            remove_from_box(boxes[hash], current_turn)

    count = 0
    for box_index, box in enumerate(boxes):
        for inbox_index, data in enumerate(box):
            _, num = data
            count += ((box_index + 1) * (inbox_index + 1) * int(num))

    print(count)


def add_to_box(box, str):
    new_str, new_num = to_tuple(str)
    for index, box_data in enumerate(box):
        data_str, _ = box_data
        if data_str == new_str:
            box[index] = (data_str, new_num)
            return
        
    box.append((new_str, new_num))


def remove_from_box(box, str):
    new_str, _ = to_tuple(str)
    for index, box_data in enumerate(box):
        data_str, _ = box_data
        if data_str == new_str:
            box.pop(index)
            return

def to_tuple(str):
    new_str = ""
    num = str[-1]

    for char in str:
        if char == "=" or char == "-":
            break
        new_str += char

    return (new_str, num)


def hash_calc(str):
    count = 0
    for char in str:
        if char == "=" or char == "-":
            break

        count += ord(char)
        count *= 17
        count %= 256
    
    return count    
    




if __name__ == "__main__":
    main()
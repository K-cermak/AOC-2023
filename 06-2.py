def main() -> None:
    data = []
    with open("06-2-input.txt", "r") as file:
        data = file.readlines()
        # clean \n
        data = [line.rstrip() for line in data]

    time = data[0].split(": ")[1].split(" ")
    distance = data[1].split(": ")[1].split(" ")
    #remove empty string
    for i in range(len(time) - 1, -1, -1):
        if time[i] == "":
            time.pop(i)

    for i in range(len(distance) - 1, -1, -1):
        if distance[i] == "":
            distance.pop(i)
    
    total_beat = 1
    for i in range(len(time)):
        how_many_beat = 0
        for wait in range(int(time[i])):
            distance_reached = (int(time[i]) - wait) * wait
            if distance_reached > int(distance[i]):
                how_many_beat += 1

        total_beat *= how_many_beat

    print(total_beat)



if __name__ == "__main__":
    main()

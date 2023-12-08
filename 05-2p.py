import threading

def main() -> None:
    data = []
    with open("05-input.txt", "r") as file:
        data = file.readlines()
        # clean \n
        data_edit = [line.rstrip() for line in data]

    seeds_str = data_edit[0].split(": ")[1].split(" ")
    min_count = [None]  # Initialize min_count with positive infinity
    min_count_lock = threading.Lock()  # Add a lock for min_count
    
    # remove new line and first index from data
    data.pop(0)
    for i in range(len(data) - 1, -1, -1):
        if data[i] == "\n":
            data.pop(i)
        else:
            data[i] = data[i].rstrip()

    threads = []
    for i in range(0, len(seeds_str), 2):
        seed_start = int(seeds_str[i])
        seed_end = seed_start + int(seeds_str[i + 1])

        print(f"Starting thread for seeds {seed_start} to {seed_end}")

        for seed in range(seed_start, seed_end):
            thread = threading.Thread(target=process_and_update_min, args=(data, seed, min_count, min_count_lock))
            threads.append(thread)
            thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    print("-----")
    print(min_count)

def process_and_update_min(data, seed, min_count, min_count_lock):
    ret = process(data, seed)
    with min_count_lock:  # Lock to avoid race conditions on min_count
        if min_count[0] is None or ret < min_count[0]:
            min_count[0] = ret

def process(data, seed):
    block_process = False

    for line in data:
        if ":" not in line:
            if not block_process:
                nums = line.split(" ")
                first = int(nums[0])
                two = int(nums[1])
                three = int(nums[2])

                if two <= seed < (two + three):
                    block_process = True
                    seed = first + seed - two
        else:
            block_process = False

    return seed

if __name__ == "__main__":
    main()

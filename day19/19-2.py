# does not work, maybe something is off by 1?

def main() -> None:
    class Part:
        def __init__(self, x, m, a, s):
            self.x = x
            self.m = m
            self.a = a
            self.s = s


    class ProcessCenter:
        def __init__(self, rules, fallback):
            self.rules = rules
            self.fallback = fallback

        def process(self, part):
            limits = {}

            for rule in self.rules:
                if rule.operation:
                    if limits.get(rule.type) is not None:
                        assert False, "Weird rule"

                    limits[rule.type] = rule.value

                if rule.type == "x" and ((part.x < rule.value and rule.operation) or (part.x > rule.value and not rule.operation)):
                    return (rule.action, limits)
        
                elif rule.type == "a" and ((part.a < rule.value and rule.operation) or (part.a > rule.value and not rule.operation)):
                    return (rule.action, limits)
                
                elif rule.type == "m" and ((part.m < rule.value and rule.operation) or (part.m > rule.value and not rule.operation)):
                    return (rule.action, limits)
                
                elif rule.type == "s" and ((part.s < rule.value and rule.operation) or (part.s > rule.value and not rule.operation)):
                    return (rule.action, limits)

            return (self.fallback, limits)

    class Rule:
        def __init__(self, type, operation, value, action):
            self.type = type # a
            self.operation = operation # bool (True for <, False for >)
            self.value = value # 2006
            self.action = action # qkq
    

    data = []
    with open("19-input.txt", "r") as file:
        data = file.readlines()
        # clean \n
        data = [line.rstrip() for line in data]

    processingInfo = {} # name: obj

    for line in data:
        if line == "":
            continue

        if "=" not in line: # processing info
            line = line.split("{")
            name = line[0]
            line = line[1].split("}")
            line = line[0]
            line = line.split(",")
            fallback = line[-1]
            line = line[:-1]

            rules = []
            for rule in line:
                rule = rule.split(":")
                action = rule[1]
                if "<" in rule[0]:
                    new = rule[0].split("<")
                    operation = True
                    type = new[0]
                    value = new[1]
                else:
                    new = rule[0].split(">")
                    operation = False
                    type = new[0]
                    value = new[1]

                rules.append(Rule(type, operation, int(value), action))

            processingInfo[name] = ProcessCenter(rules, fallback)

    
    # s 1351
    # a 2006
    # x 1416

    #part = Part(4001, 4001, 4001, 1351)
    #print(processingInfo["qqz"].process(part))


    count = 0
    x, m, a, s = 1, 1, 1, 1

    while x <= 4000 or m <= 4000 or a <= 4000 or s <= 4000:
        response = "in"
        limit_x, limit_m, limit_a, limit_s = 4001, 4001, 4001, 4001
        part = Part(x, m, a, s)

        while True:
            action, limits = processingInfo[response].process(part)
            print(action, limits)

            response = action
            for key, value in limits.items():
                if key == "x" and value < limit_x and value >= x:
                    limit_x = value
                elif key == "m" and value < limit_m and value >= m:
                    limit_m = value
                elif key == "a" and value < limit_a and value >= a:
                    limit_a = value
                elif key == "s" and value < limit_s and value >= s:
                    limit_s = value

            if response == "A" or response == "R":
                if response == "A":
                    count += (limit_x - x + 1) * (limit_m - m + 1) * (limit_a - a + 1) * (limit_s - s + 1)

                print("curr", x, m, a, s)
                print("limit", limit_x, limit_m, limit_a, limit_s)
                x = limit_x
                m = limit_m
                a = limit_a
                s = limit_s
                
                break

            
    print(count)
    




if __name__ == "__main__":
    main()
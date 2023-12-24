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
            for rule in self.rules:
                # maybe could be written better?
                if rule.type == "x" and ((part.x < rule.value and rule.operation) or (part.x > rule.value and not rule.operation)):
                    return rule.action
        
                elif rule.type == "a" and ((part.a < rule.value and rule.operation) or (part.a > rule.value and not rule.operation)):
                    return rule.action
                
                elif rule.type == "m" and ((part.m < rule.value and rule.operation) or (part.m > rule.value and not rule.operation)):
                    return rule.action
                
                elif rule.type == "s" and ((part.s < rule.value and rule.operation) or (part.s > rule.value and not rule.operation)):
                    return rule.action

            return self.fallback 

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
    parts = []

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
        else: # parts
            # remove first and last char
            line = line[1:-1]
            line = line.split(",")
            line = [part.split("=") for part in line]
            x = int(line[0][1])
            m = int(line[1][1])
            a = int(line[2][1])
            s = int(line[3][1])
            parts.append(Part(x, m, a, s))

    count = 0
    for part in parts:
        response = "in"
        while response != "A" and response != "R":
            response = processingInfo[response].process(part)
            if response == "A":
                count += part.x + part.m + part.a + part.s

    print(count)



if __name__ == "__main__":
    main()
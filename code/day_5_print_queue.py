###
# Problem : https://adventofcode.com/2024/day/5
#
def main():
    with open("input_text.txt", "r") as f:
        lines = f.readlines()

    rules = {}

    for line in lines:
        line = line.rstrip('\n')
        if  "|" in line:
            values = line.split("|")  # Split by |
            rules.setdefault(values[0], []).append(('<', values[1]))
            rules.setdefault(values[1], []).append(('>', values[0]))

    result = 0
    for line in lines:
        line = line.rstrip('\n')
        if "," in line:
            values = line.split(",")
            currMap = {y: x for x, y in enumerate(values)}
            if not verify_rules(values, rules, currMap):
                 continue
            else:
                #print(','.join(values))
                print(find_middle(values))
                result += int(find_middle(values))
    print(result)

def find_middle(lst)->int:
    middle_index = len(lst) // 2
    if len(lst) % 2 == 0:
        return (lst[middle_index - 1], lst[middle_index])
    else:
        return lst[middle_index]
    
def verify_rules(values, rules, currMap):
    for i, v in enumerate(values):
        if v in rules:
            for op, val in rules[v]:
                if val not in currMap:
                    continue
                #print(f"{v}:{currMap[v]} {op} {val}:{currMap[val]}")
                if op == '<' and currMap[v] > currMap[val]:
                    return False
                elif op == '>' and currMap[v] < currMap[val]:
                    return False
    return True
                        

if __name__ == "__main__":
    main()

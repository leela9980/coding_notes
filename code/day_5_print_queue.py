###
# Problem : https://adventofcode.com/2024/day/5
#
from functools import cmp_to_key

rules = {}

def main():
    with open("input_text.txt", "r") as f:
        lines = f.readlines()

    for line in lines:
        line = line.rstrip('\n')
        if  "|" in line:
            values = line.split("|")  # Split by |
            rules.setdefault(values[0], []).append(('<', values[1]))
            rules.setdefault(values[1], []).append(('>', values[0]))

    result = 0
    corrected_sum = 0
    for line in lines:
        line = line.rstrip('\n')
        if "," in line:
            values = line.split(",")
            currMap = {y: x for x, y in enumerate(values)}
            if not verify_rules(values, rules, currMap):
                corrected_sum += int(find_middle(sort_seq(values)))
                continue
            else:
                result += int(find_middle(values))
    print(result)
    print(corrected_sum)

def compare_pages(x, y):
    for (op, val) in rules[x]:
        if y != val:
            continue
        if op == '<':
            return -1
        elif op == '>':
            return 1
    return 0
    
def sort_seq(lst)->list:
    lst.sort(key=cmp_to_key(compare_pages))
    return lst

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

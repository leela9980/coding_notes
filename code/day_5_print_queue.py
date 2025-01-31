###
# Problem : https://adventofcode.com/2024/day/5
# Both Part1 and Part2
#
from functools import cmp_to_key

rules = {}

# Process input
def main():
    with open("input_text.txt", "r") as f:
        lines = f.readlines()

    for line in lines:
        line = line.rstrip('\n')
        if  "|" in line:
            values = line.split("|")  # Split by |
            rules.setdefault(values[0], []).append(('<', values[1]))
            rules.setdefault(values[1], []).append(('>', values[0]))

    correct_order_seq_sum = 0
    incorrect_order_seq_sum =  0
    for line in lines:
        line = line.rstrip('\n')
        if "," in line:
            values = line.split(",")
            currMap = {y: x for x, y in enumerate(values)}
            if not verify_rules(values, rules, currMap):
                incorrect_order_seq_sum += int(find_middle(sort_seq(values)))
                continue
            else:
                correct_order_seq_sum += int(find_middle(values))
    print(correct_order_seq_sum)
    print(incorrect_order_seq_sum)

# Custom comparison for incorrect sequence
def compare_pages(x, y):
    for (op, val) in rules[x]:
        if y != val:
            continue
        if op == '<':
            return -1
        elif op == '>':
            return 1
    return 0
    
# Sort function
def sort_seq(lst)->list:
    lst.sort(key=cmp_to_key(compare_pages))
    return lst

# Find middle value
def find_middle(lst)->int:
    middle_index = len(lst) // 2
    if len(lst) % 2 == 0:
        return (lst[middle_index - 1], lst[middle_index])
    else:
        return lst[middle_index]

# Verify if the value is in correct position in the sequence or not
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

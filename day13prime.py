from functools import cmp_to_key

with open('inputs/inputx13.txt', 'r') as f:
    a = f.read().strip().split('\n\n')

def process_couple(first, second):
    if type(first) == int and type(second) == int:
        if first < second:
            return 1
        elif first == second:
            return 0
        else:
            return -1
    elif type(first) == list and type(second) == int:
        return process_couple(first, [second])
    elif type(first) == int and type(second) == list:
        return process_couple([first], second)
    elif type(first) == list and type(second) == list:
        for f, s in zip(first, second):
            current = process_couple(f, s)
            if current != 0:
                return current
    return len(second) - len(first)

ans = 0
elements = []
for i, couple in enumerate(a):
    first, second = map(lambda exp: eval(exp), couple.split('\n'))
    elements.append(first)
    elements.append(second)

tokens = [[[2]], [[6]]]
elements += tokens

elements = sorted(elements, key=cmp_to_key(process_couple), reverse=True)

ans = 1
for i, el in enumerate(elements):
    if el in tokens:
        ans *= i+1

print(ans)

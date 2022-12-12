from functools import reduce

with open('inputs/inputx11.txt', 'r') as f:
    a = f.read().strip().split('\n\n')

ROUNDS = 10000
FACTOR = 1

# print(a)xs
monkeys_id = []
monkeys_items = {}
monkeys_op = {}
monkeys_cond = {}
monkeys_target = {}
monkeys_modu = {}
for monkey in a:
    monkey = monkey.split('\n')
    monkey_nb = int(monkey[0].split()[-1][0])
    monkey_items = list(map(lambda x: int(x), monkey[1].split(': ')[1].split(', ')))
    monkey_op = monkey[2].split(': ')[-1].split('=')[-1].split()
    nb = monkey_op[2]
    if monkey_op[1] == '*':
        if nb == 'old':
            nb = 0
            monkey_operation = lambda x, y: x * x
        else:
            monkey_operation = lambda x, y: x * y
    else:
        monkey_operation = lambda x, y: x + y
    monkey_cond = int(monkey[3].split()[-1])
    monkey_target = (int(monkey[4].split()[-1]), int(monkey[5].split()[-1]))

    monkeys_id.append(monkey_nb)
    monkeys_items[monkey_nb] = monkey_items
    monkeys_op[monkey_nb] = monkey_operation
    monkeys_cond[monkey_nb] = monkey_cond
    monkeys_target[monkey_nb] = monkey_target
    monkeys_modu[monkey_nb] = int(nb)

common_modulus = reduce(lambda x, y: x*y, monkeys_cond.values())

monkeys_counter = dict(zip(monkeys_items.keys(), [0]*len(monkeys_items)))
for round in range(ROUNDS):
    for monkey_nb in monkeys_id:
        # print(f"NOW Monkey {monkey_nb}")
        # print(monkeys_items[monkey_nb])
        # print(monkeys_op[monkey_nb], 'the function')
        for item in monkeys_items[monkey_nb]:
            monkeys_counter[monkey_nb] += 1
            item_worry_level = monkeys_op[monkey_nb](item, monkeys_modu[monkey_nb]) % common_modulus
            if item_worry_level % monkeys_cond[monkey_nb] == 0:
                # print(item, 'adding', item_worry_level, 'to', monkeys_target[monkey_nb][0], 'because true')
                monkeys_items[monkeys_target[monkey_nb][0]].append(item_worry_level)
            else:
                # print(item, 'adding', item_worry_level, 'to', monkeys_target[monkey_nb][1], 'because false')
                monkeys_items[monkeys_target[monkey_nb][1]].append(item_worry_level)

            monkeys_items[monkey_nb] = []

    # print(f'round {round} done!')
    # print(monkeys_counter)
    # print(monkeys_items)

passes = set(monkeys_counter.values())
# print(passes)
max1 = max(passes)
passes.remove(max1)
max2 = max(passes)
ans = max1 * max2  # monkey_business

print(ans)  
 # 313044376201059520 HIGH
 # 9024 too low
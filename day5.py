from collections import deque

with open('inputs/input5.txt', 'r') as f:
    a = f.read().split('\n')

q_list = [deque() for _ in range(9)]
initial = ['MJCBFRLH', 'ZCD', 'HJFCNGW', 'PJDMTSB', 'NCDRJ',
            'WLDQPJGZ', 'PZTFRH', 'LVMG', 'CBGPFQRJ']
for i, word in enumerate(initial):
    for letter in word:
        q_list[i].append(letter)

for line in a[:-1]:
    words = line.split()
    count = int(words[1])
    from_q = int(words[3]) - 1
    to_q = int(words[5]) - 1

    for _ in range(count):
        q_list[to_q].append(q_list[from_q].pop())

ans = [q.pop() for q in q_list]
print("".join(ans))

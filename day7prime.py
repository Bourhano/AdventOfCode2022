import os

# f = open('inputs/input7small.txt', 'r')
# PATH = ['day7small']
# PWD = os.path.join(*PATH)

# current_line = f.readline().split()
# while(current_line != []):
#     line = current_line
#     if line[0] == '$':
#         if line[1] == 'ls':
#             current_line = f.readline().split()
#             while current_line[0] != '$':
#                 if current_line[0] == 'dir':
#                     os.system(f'mkdir {PWD}/{current_line[1]}')
#                 elif current_line[0] != '$' :
#                     os.system(f'touch {PWD}/{current_line[1]}_{current_line[0]}')
#                 current_line = f.readline().split()
#                 if not current_line:
#                     break;
#             continue;

#         elif line[1] == 'cd':
#             if line[2] == '..':
#                 PATH.pop()
#             else:
#                 PATH.append(line[2])
#             PWD = os.path.join(*PATH)

#     current_line = f.readline().split()

# print('done')


total = 0
parent = 'day7'
ans = []
def get_dir_size(path):
    global total

    if os.path.isfile(path):
        path = path.__str__()
        fsize = int(path.split('/')[-1].split('_')[-1])
        return fsize
    else:
        partial = 0
        this_dir_content = os.listdir(path)
        for el in this_dir_content:
            current = get_dir_size(f'{path}/{el}')
            partial += current
            if os.path.isdir(f'{path}/{el}'):  # and current <= 100_000:
                if current >= 4804833:
                    print(f'{path}/{el}', current)
                total += current
                ans.append(current)
        return partial

root_size = get_dir_size(parent)
print('total :', root_size)
free_space = 70_000_000 - root_size
print('free  :', free_space)
needed_space = 30_000_000 - free_space
print('needed:', needed_space)

print(total, sum(ans))
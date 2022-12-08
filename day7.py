import os

# f = open('inputs/input7.txt', 'r')
# PATH = ['day7']
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
        this_dir_content = os.listdir(path)  # list(Path(path).rglob("*"))
        for el in this_dir_content:
            current = get_dir_size(f'{path}/{el}')
            partial += current
            if os.path.isdir(f'{path}/{el}') and current <= 100_000:
                # print(f'{path}/{el}', current)
                total += current
                ans.append(current)
        return partial
    
get_dir_size(parent)

print(total)
# print(sum(ans))
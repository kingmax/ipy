# coding:utf-8
# 先用这个脚本移除空行与单行注释
# 然后再用cpp那个移除多行注释

import os, sys

_thisDir = os.path.dirname(__file__)
src_dir = os.path.join(_thisDir, 'src')
new_dir = os.path.join(_thisDir, 'new')
if not os.path.exists(new_dir):
    os.makedirs(new_dir)
print(src_dir, new_dir)

ms_files = [f for f in os.listdir(src_dir) if f.endswith('.ms')]
print(ms_files)

ms_lib = os.path.join(src_dir, 'CR43D66Lib.ms')
#ms_lib = os.path.join(src_dir, 'comment_test.txt')
new_msLib = os.path.join(new_dir, 'CR43D66Lib.ms')
#new_msLib = os.path.join(new_dir, 'comment_test.txt')
print(ms_lib, new_msLib)

allLines = []
words = {}

# remove space line
with open(ms_lib, 'r') as fp:
    allLines = [line.strip() for line in fp.readlines() if line.strip()]
    print(len(allLines))

# remove single comment line
#print(range(len(allLines)))
new_lines = []

for line in allLines:
    if line.startswith('--'):
        continue
    elif line.startswith('/*') and line.endswith('*/'):
        continue
    else:
        new_lines.append(line)
        # print(line)

new_code = '\n'.join(new_lines)

# print(new_code)


print(len(new_lines))
if new_lines:
    with open(new_msLib, 'w') as fp:
        fp.writelines(new_code)
        print('write new file done')

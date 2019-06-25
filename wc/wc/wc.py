#coding:utf-8
import os, sys

_thisDir = os.path.dirname(__file__)
src_dir = os.path.join(_thisDir, 'src')
new_dir = os.path.join(_thisDir, 'new')
#os.makedirs(new_dir)
print(src_dir, new_dir)

ms_files = [f for f in os.listdir(src_dir) if f.endswith('.ms')]
print(ms_files)

ms_lib = os.path.join(src_dir, 'CR43D66Lib.ms')
new_msLib = os.path.join(new_dir, 'CR43D66Lib.ms')
print(ms_lib, new_msLib)

allLines = []
words = {}

# remove space lines
with open(ms_lib, 'r') as fp:
    allLines = [line.strip() for line in fp.readlines() if line.strip()]
    print(len(allLines))

# remove comment lines
#print(range(len(allLines)))
for line in allLines:
    if line.startswith('--'):
        continue

    found = False
    if line.startwith('/*') and not found:
        continue
    if line.endswith('*/'):
        found = True

n = len(allLines)
for i in range(n):
    line = allLines[i]
    if line.startswith('--'):
        continue

    found = False
    if line.startswith('/*') and not found:
        continue
    if line.endswith('*/'):
        found = True




'''
if allLines:
    with open(new_msLib, 'w') as fp:
        fp.writelines('\n'.join(allLines))
        print('write new file done')
'''    
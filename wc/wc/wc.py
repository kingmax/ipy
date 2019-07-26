# coding:utf-8
# 先用这个脚本移除空行与单行注释
# 然后再用cpp那个移除多行注释

import os, sys
import shutil

#----------------------------------------------------------------------
def remove_space_line_and_commnet(in_msfile, out_msfile):
    """"""
    allLines = []
    # remove space line
    with open(in_msfile, 'r') as fp:
        allLines = [line.strip() for line in fp.readlines() if line.strip()]
        #print(len(allLines))
        
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
    
    #print(len(new_lines))
    if new_lines:
        with open(out_msfile, 'w') as fp:
            fp.writelines(new_code)
            print('write new ms-file done::%s'%out_msfile)

            
#---------------------------------------------------------------------- start
devDir = r'D:\git\CR43D66\src\CR43D66'
devFileList = [f for f in os.listdir(devDir) if f.endswith('_dev.ms')] #('CR43D66CB_dev.ms', 'CR43D66Lib_dev.ms', 'CR43D66Submit_dev.ms', 'CR43D66UI_dev.ms')
print(len(devFileList), devFileList)

# backup dev src
_thisDir = os.path.dirname(__file__)
src_dir = os.path.join(_thisDir, 'src')
new_dir = os.path.join(_thisDir, 'new')
print(src_dir, new_dir)
try:
    shutil.rmtree(new_dir)
except:
    pass

if not os.path.exists(src_dir):
    os.makedirs(src_dir)
if not os.path.exists(new_dir):
    os.makedirs(new_dir)

bakFileList = []
if devFileList:
    for f in devFileList:
        dev = os.path.join(devDir, f)
        bak = os.path.join(src_dir, f)
        shutil.copy(dev, bak)
        bakFileList.append(bak)
        print('[bakup]%s -> %s'%(dev, bak))


newFileList = []
# remove space line and comment line
for f in bakFileList:
    new_name = os.path.basename(f).rsplit('_dev.ms', 1)[0]
    new_name += '.ms'
    dest = os.path.join(new_dir, new_name)
    print(dest)
    remove_space_line_and_commnet(f, dest)
    newFileList.append(dest)
    
# copy to dev dir
for f in newFileList:
    dev = os.path.join(devDir, os.path.basename(f))
    shutil.copy(f, dev)
    print('[new2dev]%s -> %s'%(f, dev))
    

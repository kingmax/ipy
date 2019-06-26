# coding:utf-8
# https://codereview.stackexchange.com/questions/148305/remove-comments-from-c-like-source-code

import re
import os
import sys

_thisDir = os.path.dirname(__file__)
src_dir = os.path.join(_thisDir, 'src')
new_dir = os.path.join(_thisDir, 'new')
if not os.path.exists(new_dir):
    os.makedirs(new_dir)

#ms_lib = os.path.join(src_dir, 'CR43D66Lib.ms')
ms_lib = os.path.join(src_dir, 'comment_test.txt')
#new_msLib = os.path.join(new_dir, 'CR43D66Lib.ms')
new_msLib = os.path.join(new_dir, 'comment_test.txt')

COMMENTS = re.compile(r'''
    (//[^\n]*(?:\n|$))    # Everything between // and the end of the line/file
    |                     # or
    (/\*.*?\*/)           # Everything between /* and */
''', re.VERBOSE)


def remove_comments(content):
    return COMMENTS.sub('\n', content)

content = ''
with open(ms_lib, 'r') as fp:
    content = fp.read()
    
print(remove_comments(content))

#txt = 'if (matchPattern theLine pattern:"*:*") or (matchPattern theLine pattern:"*\\*") or (matchPattern theLine pattern:"*/*") then'
# print(remove_comments(txt))


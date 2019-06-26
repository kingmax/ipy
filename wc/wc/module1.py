#coding:utf-8
# https://codereview.stackexchange.com/questions/148305/remove-comments-from-c-like-source-code

import re


COMMENTS = re.compile(r'''
    (//[^\n]*(?:\n|$))    # Everything between // and the end of the line/file
    |                     # or
    (/\*.*?\*/)           # Everything between /* and */
''', re.VERBOSE)


def remove_comments(content):
    return COMMENTS.sub('\n', content)

txt = 'if (matchPattern theLine pattern:"*:*") or (matchPattern theLine pattern:"*\\*") or (matchPattern theLine pattern:"*/*") then'

print(remove_comments(txt))
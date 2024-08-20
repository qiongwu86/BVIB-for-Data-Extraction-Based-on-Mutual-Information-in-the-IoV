# -*- coding = utf-8 -*-
# @Time : 2024/1/5 14:59
# @Author : Maxwell
# @File : titleCorrect.py
# @Software : PyCharm

import re

def wrap_title_in_braces(line):
    if line.startswith('title ='):
        # 使用正则表达式匹配标题文本，并在前后添加双括号
        line = re.sub(r'title\s*=\s*{(.+)}', r'title = {{\1}}', line)
    return line

# 读取BibTeX文件
with open('ref.txt', 'r') as file:
    lines = file.readlines()

# 修改标题文本格式
modified_lines = [wrap_title_in_braces(line) for line in lines]

# 将修改后的内容写回文件
with open('ref2.txt', 'w') as file:
    file.writelines(modified_lines)

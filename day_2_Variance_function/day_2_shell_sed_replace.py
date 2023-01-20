#!/user/bin/env python
# -*- coding:utf-8 -*-
__author__ = "Ming"

import sys

find_str = sys.argv[1]
replace_str = sys.argv[2]

with open(r'E:\MingData\Python\PythonDays\PythonDays\day_2_Variance_function\lyric.txt', 'r', encoding='utf-8') as file:
    with open(r'lyric_3.bak', 'w', encoding='utf-8') as file_new:
        for line in file:
            if find_str in line.strip():
                line = line.replace(find_str, replace_str)
            file_new.write(line)
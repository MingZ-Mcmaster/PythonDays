__author__ = "Ming"
import sys

find_str = sys.argv[1]
replace_str = sys.argv[2]

# 增改文件的内容
with open(r"day_2_Variance_function\lyric.txt", "r", encoding='utf-8') as f:    # read 文件
    with open("lyric_3.bak", "w", encoding='utf-8') as f_new:                   # 准备一个新文件
        for line in f:
            if "心里爱" in line:
                line = line.replace("心里爱", "心里爱Yang")         # 查找old,替换new
            f_new.write(line)                                      # 写到新的文件里

# 通过脚本传参数来改内容
with open(r"day_2_Variance_function\lyric.txt", "r", encoding='utf-8') as f:    # read 文件
    with open("lyric_3.bak", "w", encoding='utf-8') as f_new:                   # 准备一个新文件
        for line in f:
            if find_str in line:
                line = line.replace(find_str, replace_str)         # 查找old,替换new
            f_new.write(line)                                      # 写到新的文件里
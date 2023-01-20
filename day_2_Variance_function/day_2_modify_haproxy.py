#!/user/bin/env/python
# -*- coding:utf-8 -*-
__author__ = "Ming"

menu = ['search', 'create', 'delete']

while True:
    for i, content in enumerate(menu):
        print(i+1, content)

    choice = input("Select: ")
    if choice == 'q':   # 如果是q，就推出程序
        break
    elif not choice.isdigit():  # 判断是不是数字，如果不是数字，就报错并重新输入
        print("Invalid input, please try it again")
    elif 0 < int(choice) <= len(menu):  # 判断输入的数字是否在列表范围内
        if int(choice) == 1:
            search_str = input("Type the address: ")
            search_str_modified = str("backend %s\n"%search_str)
            with open(r'E:\MingData\Python\PythonDays\PythonDays\day_2_Variance_function\harproxy', 'r', encoding='utf-8') as original_file:
                # 方法一： 把文件全都到内存中，通过寻找内容的index，显示下一行index的内容。
                # data = original_file.readlines()
                # if search_str in data:
                #     index_add = data.index(search_str_modified)
                #     print(index_add, data[index_add], data[index_add+1])
                
                # 方法二： 每次只读一行内容进内存，找到寻找的内容后，显示下一行的内容
                for line in original_file:
                    if search_str_modified in line:
                        print("Output: ", original_file.readline())
                    else:
                        print("Not exist.")
        elif int(choice) == 2:      # {"backend":"www.test.org", 'record':{ 'server': '100.1.7.9', 'weight': 20, 'maxconn': 30 } }
            data = input("Type the content you want to add: ")
            data_dict = eval(data)                                      # convert to dict
            data_list = list(data_dict.items())                         # convert dict to list
            search_str = str( data_list[0][0]+" "+data_list[0][1] )     # organize the seach string，重组网址的string: "backend www.oldboy.org"
            exist_flag = False
            # 如果输入的地址已经存在，那就不做添加，否则就添加
            with open(r'E:\MingData\Python\PythonDays\PythonDays\day_2_Variance_function\harproxy', 'r', encoding='utf-8') as original_file:
                for line in original_file:  # 查找网址的string
                    if search_str in line:
                        exist_flag = True   # 如果存在，flag为True
                        break
            if exist_flag == True:          # 浏览完文档，如果flag=Ture，就说明已存在，不做改变
                print("Existed")
            else:                           # flag=False，不存在，需要增加
                with open(r'E:\MingData\Python\PythonDays\PythonDays\day_2_Variance_function\harproxy', 'a', encoding='utf-8') as original_file:
                    add_data = list(data_list[1][1].items())        # [('server', '100.1.7.9'), ('weight', 20), ('maxconn', 30)]
                    add_str = f"\n{search_str}\n\t\t{add_data[0][0]} {add_data[0][1]} {add_data[1][0]} {add_data[1][1]} {add_data[2][0]} {add_data[2][1]}"
                    print("需要添加的段落：", add_str)
                    original_file.write(add_str)

        elif int(choice) == 3:          # {"backend":"www.test.org", 'record':{ 'server': '100.1.7.9', 'weight': 20, 'maxconn': 30 } }
            data = input("Type the content you want to delete: ")
            data_dict = eval(data)                                      # convert to dict
            data_list = list(data_dict.items())                         # convert dict to list
            del_str_1 = str( data_list[0][0]+" "+data_list[0][1] )     # organize the seach string，重组网址的string: "backend www.test.org"

            del_data = list(data_list[1][1].items())        # [('server', '100.1.7.9'), ('weight', 20), ('maxconn', 30)]
            del_str_2 = f"{del_data[0][0]} {del_data[0][1]} {del_data[1][0]} {del_data[1][1]} {del_data[2][0]} {del_data[2][1]}"

            exist_flag = False

            # 如果输入的地址已经存在，那就不做添加，否则就添加
            with open(r'E:\MingData\Python\PythonDays\PythonDays\day_2_Variance_function\harproxy', 'r', encoding='utf-8') as original_file:
                with open(r'E:\MingData\Python\PythonDays\PythonDays\day_2_Variance_function\lyric_3.bak', 'w', encoding='utf-8') as new_file:
                    for line in original_file:  # 查找网址的string
                        if del_str_1 in line or del_str_2 in line:
                            exist_flag = True
                            continue
                        new_file.write(line)
            if exist_flag == True:
                print("Delete is done.")
            else:                           # flag=False，不存在，不需要更改
                print("No existing content.")
                
    else:
        print("Invalid input, please try it again.")


print("Exit the system.")

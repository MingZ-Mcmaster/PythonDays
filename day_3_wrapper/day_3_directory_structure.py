"""
Foo/
|-- bin/    # 存放项目的一些可执行文件，当然你可以起名script/之类的也行。
|   |-- foo 
|
|-- foo/    #  存放项目的所有源代码。
    |        #   (1) 源代码中的所有模块、包都应该放在此目录。不要置于顶层目录。
    |        #   (2) 其子目录tests/存放单元测试代码； 
    |        #   (3) 程序的入口最好命名为main.py。
|   |-- tests/
|   |   |-- __init__.py
|   |   |-- test_main.py
|   |
|   |-- __init__.py
|   |-- main.py
|
|-- docs/   # 存放一些文档。
|   |-- conf.py
|   |-- abc.rst
|
|-- setup.py    # 安装、部署、打包的脚本。
|-- requirements.txt    # 存放软件依赖的外部Python包列表。
|-- README  # 项目说明文件。

"""

# 除此之外，有一些方案给出了更加多的内容。比如LICENSE.txt,ChangeLog.txt文件等

import sys
import os
# 相对路径
relative_path = __file__
print("file: ", relative_path)   
# 绝对路径
absolute_path = os.path.abspath(__file__)
print(absolute_path) 
# 父文件
parent_dir = os.path.dirname(os.path.abspath(__file__))
print(parent_dir)   # 找到文件所属的父文件地址
# 爷文件
grandparent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(grandparent_dir)  # 找到文件所属的爷文件地址
# 查看环境变量
print(sys.path) # 可用的文件变量
# 添加环境变量
sys.path.append(parent_dir)
print(sys.path)
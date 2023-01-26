# json序列化:各个平台都可以互通数据的
#   pickle: 和json的methods都一样，只是只能在python里互通

# 3. 如果有些内容不能在保存和读取中完全恢复，就需要用到json
import json

# 1. 文件保存
info = {'name': 'ming', 'age':'38'}

f = open("test.txt", 'w')
# f.write(str(info))  # 因为不能存dict，所以转存成str

# 4. 用json来保存文件
print( json.dumps(info), type(json.dumps(info)))
f.write( json.dumps( info ))

f.close()

# 2. 读取文件内容
f = open("test.txt", 'r')

# data = eval(f.read())   # 将str转成dict

# 5. 用json读取文件
data = json.loads(f.read())
f.close()
print(data)
print(data['age'])

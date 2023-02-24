import json, pickle
import shelve   # 只支持pickle, 是其更上一层的封装
import datetime

data = {'k1': 123, 'k2':'Hello'}

# pickle.dumps 将数据通过特殊的形式转换为只有Python语言认识的字符串
p_bytes = pickle.dumps(data)
print(p_bytes, type(p_bytes))

# pickle.dump 将数据通过特殊的形式转换为只有Python语言认识的字符串,并写入文件
with open(r'./day_4_models/result.pk', 'wb') as fp:
    pickle.dump(data, fp)

# json.dumps 将数据通过特殊的形式转换为所有语言认识的字符串
j_str = json.dumps(data)
print(j_str, type(j_str))

# json.dump 将数据通过特殊的形式转换为所有语言认识的字符串,并写入文件
with open(r'./day_4_models/result.json', 'w') as fp:
    json.dump(data, fp)


# 用shelve写数据
d = shelve.open('shelve_test')  # 打开一个文件

info = {'age':22, 'job':'IT'}
name = ['ming','yang','test']
d['name'] = name    # 持久化列表
d['info'] = info    # 持久化dict
d['date'] = datetime.datetime.now()
d.close()   # 会生成3个文件

# 用shelve读数据
d = shelve.open('shelve_test')  # 打开文件
print(d.get("name"))        # 读数据
print(d.get("info"))
print(d.get('date'))
d.close()
import xml.etree.ElementTree as ET

tree = ET.parse(r'day_4_models\xml_sample.xml')
root = tree.getroot()
print(root.tag) # 打印内存对象的根节点

for child in root:
    print(child.tag, child.attrib)  # 只打印了标签内的头名称和属性，也就是国家的信息

    for i in child:
        print(i.tag, i.text)    # 只打印了标签的头名称，和标签内的文字
        print(i.attrib)     # 打印了标签的头名称后面的属性

# 单独遍历 year 节点
for node in root.iter('year'):
    print(node.tag, node.text)


# 修改
for node in root.iter('year'):
    new_year = int(node.text) + 1
    node.text = str(new_year)
    node.set('updated_by', 'Ming')

tree.write(r'day_4_models\xmltest.xml')

# 删除node
for country in root.findall('country'):
    rank = int(country.find('rank').text)
    if rank > 50:
        root.remove(country)

tree.write(r'day_4_models\xmltest.xml')

# 创建xml文档
new_xml = ET.Element("namelist")    # 创建了一个根节点
person_info = ET.SubElement(new_xml,"person_info",attrib={"enrolled":"yes"})    # 创建了一个子节点
name = ET.SubElement(person_info,"name")    # 在子节点下，增加标签名
name.text = "Ming"      # 标签名下的文字
age = ET.SubElement(person_info,"age",attrib={"checked":"no"})
sex = ET.SubElement(person_info,"sex")
age.text = '33'

person_info_2 = ET.SubElement(new_xml,"person_info_2",attrib={"enrolled":"no"})
age = ET.SubElement(person_info_2,"age")
age.text = '19'
 
et = ET.ElementTree(new_xml) #生成文档对象
et.write(r"day_4_models\test.xml", encoding="utf-8",xml_declaration=True)
 
ET.dump(new_xml) #打印生成的格式
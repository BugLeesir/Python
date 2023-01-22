name_list=['nihao','wohao','dajiahao',666]
#列表的遍历
for y in name_list:
    print(y)

i=0
while i<len(name_list):
    elem=name_list[i]
    print(elem)
    i+=1

#列表的访问
print(name_list[0])

print(name_list[-4])

#查找元素的下标索引
print(name_list.index("nihao"))

#修改下标索引值
name_list[0]="dajiahao"
print(name_list[0])

#元素插入
name_list.insert(1,"wocao")
for x in name_list:
    print(x)

#追加元素
name_list.append("wWWWWw")
for x in name_list:
    print(x)

#追加数据容器
new_list=[2222,2323232,2323234]
name_list.extend(new_list)
for x in name_list:
    print(x)    

#删除元素
del name_list[0]
print(name_list[0])
element=name_list.pop(0)
print(element)
for x in name_list:
    print(x)

#指定元素内容进行删除(删除第一个匹配项)
name_list.remove(666)
print(name_list)

#清空列表内容
# name_list.clear()
# print(name_list)

#统计列表内某一元素的数量
name_list.append(2222)
print(name_list.count(2222))

#列表长度
print(len(name_list))

#排序
list1=[1,24,5,6,7,8,2,4,6,8,5]
list2=sorted(list1)
list3=sorted(list1,reverse=True)
print(list2,list3)



my_set={"hello","nihao","wohao","hello"}
print(my_set)#无序不重复，不支持下标索引

#空集合
s1=set()

#添加新元素
my_set.add("huolu")
print(my_set)

#移除元素
my_set.remove("hello")
print(my_set)

#随机取出一个元素
print(my_set.pop())
print(my_set)

#清空集合
my_set.clear()
print(my_set)

#取两个集合的差集
set1={1,2,3}
set2={2,3,5,6,7}
set3=set1.difference(set2)
set4=set2.difference(set1)
print(set3)
print(set4)

#清除两个集合的差集
set2.difference_update(set1)
print(set2)

#集合合并
set5=set1.union(set2)
print(set5)

#集合遍历
for x in set5 :
    print(x)

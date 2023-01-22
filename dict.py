my_dict={"hahaha":114,"huhu":514,"xianbei":1919,"daisiki":810}#字典的key不允许重复
#key的类型不可为字典

#空字典
d1=dict()
d2={}

#基于key获取value
print(my_dict["huhu"])

#新增元素
my_dict["wocao"]="op"
print(my_dict)

#更新元素
my_dict["wocao"]="oupao"
print(my_dict)

#删除元素
val=my_dict.pop("wocao")
print(val,my_dict)

#获取所有的key
keys=my_dict.keys()
print(keys)

#遍历字典
for key in keys:
    print(my_dict[key])

for key in my_dict:
    print(key)
    print(my_dict[key])    

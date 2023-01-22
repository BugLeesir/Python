import json
data=[{"name":"kikk","age":12,"gender":"man"},{"name":"jsif","age":23,"gender":"man"}]
#python列表，字典转json
json_str=json.dumps(data)
print(json_str)
#json转python列表，字典
s='[{"name":"kikk","age":12,"gender":"man"},{"name":"jsif","age":23,"gender":"man"}]'
l=json.loads(s)
print(l)


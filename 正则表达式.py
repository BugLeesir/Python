import re

str = "python,huhupython,python"

# 从头匹配
result = re.match("python", str)
print(result)

# 搜索匹配
result = re.search("python", str)
print(result)

# 全部匹配
result = re.findall("python", str)
print(result)

# 匹配qq号    ：只有数字组成，第一位不为0，且长度为6-11位
r = r"^[1-9]\d{5,10}$"
mod_str_01="1007878894"
mod_str_02="0898973789"
mod_str_03="89s8973789"
print(re.findall(r,mod_str_01))
print(re.findall(r,mod_str_02))
print(re.findall(r,mod_str_03))

#匹配邮箱      ：只允许qq,gmail,163,foxmail
#例：{内容}.{内容}.{内容}@{内容}.{内容}
#内容中允许数字，字母，下划线，连接字符
r=r"(^[\w-]+(\.[\w-]+)*@(qq|163|gmail|foxmail)(\.[\w-]+)$)"
mod_str_04="1007878987@qq.com"
mod_str_05="6724637373.dfij.888@foxmail.com"
mod_str_06="1007878987@qq.com.cn"
print(re.findall(r,mod_str_04))
print(re.findall(r,mod_str_05))
print(re.findall(r,mod_str_06))
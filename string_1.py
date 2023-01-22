str1="nihao"

#字符串下标索引
print(str1[0])

#字符串的替换
str2=str1.replace("nihao","wocao")
print(str2)

#字符串的分割
str3="Good moring everyone"
test_str=str3.split(" ")
print(test_str)

#字符串的规整操作
str4="                 hello         "
print(str4)
test_str2=str4.strip()
print(test_str2)
str5="wocao op @@@"
test_str3=str5.strip("wocao@")
print(test_str3)

#统计字符串中某个字符串出现的次数
count=str5.count("@")
print(count)

#统计字符串的长度
print(len(str5))

#字符串比较
string1="abc"
string2="abcd"
string3="abce"
if string2>string1:
    print("2比1大")
if string3>string2:
    print("3比2大")
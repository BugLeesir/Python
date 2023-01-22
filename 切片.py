my_list=[0,1,2,3,4,5]

#序列[起始下标：结束下标：步长]
result1=my_list[1:4]#不设定步长默认为1
print(result1)

result2=my_list[:]#起始结束不写默认从头到尾
print(result2)

#将序列反转
result3=my_list[::-1]
print(result3) 

#反向切片
result4=my_list[4:1:-1]
print(result4)
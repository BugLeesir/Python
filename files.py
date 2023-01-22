#打开文件
f1=open("haha.txt",'r',encoding="UTF-8")
print(type(f1))

#读取文件
print(f1.read(10))

print(f1.readline())

print(f1.readlines(),type(f1.readlines()))

#for循环读取文件行
f2=open("haha.txt",'r',encoding="UTF-8")
for line in f2:
    print(line)

#关闭文件
f1.close
f2.close

#with open 语法操作文件(自动close)
with open("haha.txt","r",encoding="UTF-8") as f3:
    for line in f3:
        print(line)

#文件的写操作
f3=open("haha.txt","w",encoding="UTF-8")
f3.write("hurahura")
f3.flush()
f3.close()#close有flush的功能





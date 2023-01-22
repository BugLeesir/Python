str1="nihaoya"
str2="zhaoshanghao"
str3="wanshanghao"

def my_len(data):
    count=0;
    for i in data:
        count+=1
    print(f"字符串{data}的长度是{count}")

my_len(str1)
my_len(str2)
my_len(str3)

#函数返回多个返回值
def test1():
    return 1,1,3

print(test1())

#关键字传参
def test2(name,age,gender):
    print(name,age,gender)

test2("李云瑞",gender="男",age=21)

#缺省参数
def test3(name,age,gender="男"): #默认值只能在最后
    print(name,age,gender)

test3("liyunrui",13)

#不定长参数
def test4(*args):
    print(args);
    print(type(args))

test4(1,2,3,4,5,6,7,8)

def test5(**kwargs):
    print(kwargs)
    print(type(kwargs))

test5(姓名="李玉仁",年龄=18) 

#函数作为参数传递
def fun1(x,y):
    return x*y

def calculate(compute):
    print(compute(12,32),type(compute))

calculate(fun1)

#lambda
calculate(lambda x,y:x-y)

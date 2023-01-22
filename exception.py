 #捕获常规异常
try:
    f=open("dffd.txt","r",encoding="UTF-8")
except:
    print("异常发生")

#捕获指定异常
try:
    a=1/0
except ZeroDivisionError as e:
    print("除零异常")

#捕获多个异常
try: 
    a=1/0
except (NameError,ZeroDivisionError) as e :
    print("发生未定义异常或除零异常")

#捕获全部异常
try:
    a=1/0
except Exception as e :
    print("捕获全部异常")

#else,finally语句
try :
    a=1
except Exception as e:
    print("出现异常")
else:
    print("没有异常")
finally:
    print("无论如何我都会执行")

#异常具有传递性，函数调用异常传递
def fun1():
    a=1/0

def fun2():
    fun1()    

try:
    fun2()
except ZeroDivisionError as e :
    print("异常传递")


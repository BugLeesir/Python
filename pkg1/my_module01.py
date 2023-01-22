__all__=['add']#在别的模块中使用通配符*导入该模块中的内容时只导入列表中的内容
def add(a,b):
    return a+b

def div(a,b):
    return a/b

if __name__=='__main__':#只有在本模块运行该变量值才为main
    add(1,2)
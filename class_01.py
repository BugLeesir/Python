#设计一个类
class Student:
    name=None
    age=None
    gender=None
    def toString(self):
        return f"{self.name},{self.age},{self.gender}"

#创建一个对象
stu_01=Student()

#对对象进行赋值
stu_01.name="woc"
stu_01.age=19
stu_01.gender="男"

#输出对象中的数据
print(stu_01.toString())
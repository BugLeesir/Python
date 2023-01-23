# 设计一个类
class Student:
    name = None
    age = None
    gender = None

    # 私有成员变量，方法 以__开头
    __secret = None

    def __catch(self):
        print("我是私有方法,被调用了")

    def set_secret(self, secret):
        self.__catch()
        self.__secret = secret

    def get_secret(self):
        return self.__secret

    # 构造方法
    def __init__(self, name: str, age: int, gender: str):
        self.name = name
        self.age = age
        self.gender = gender

    # 析构方法
    def __del__(self):
        print("析构函数调用")

    # 魔术方法

    # str    tostring方法
    def __str__(self) -> str:
        return f"{self.name},{self.age},{self.gender}"

    # lt     '<' 重载(也可比较'>') gt 为重载'>'
    def __lt__(self, other: object) -> bool:
        return self.age < other.age

    # eq     '==' 重载
    def __eq__(self, __o: object) -> bool:
        return self.age == __o.age

    # le      '<=' 重载
    def __le__(self, other: object) -> bool:
        return self.age <= other.age


# 创建一个对象
stu_01 = Student(None, None, None)

# 对对象进行赋值
stu_01.name = "woc"
stu_01.age = 19
stu_01.gender = "男"

# 输出对象中的数据
print(stu_01)

# 使用构造方法赋值
stu_02 = Student("李云瑞", 19, "男")


print(stu_02)
print(stu_01 < stu_02)
print(stu_01 == stu_02)
print(stu_01 <= stu_02)
stu_02.set_secret("em.....")
print(stu_02.get_secret())

# 类的继承(继承优先级根据参数位置排位 高->低)
class NewStudent(Student):
    __id = None

    def setId(self, id):
        self.__id = id

    def getId(self):
        return self.__id

    # 方法重写
    def __str__(self) -> str:
        # super关键字调用父类成员
        return super().__str__() + f"{self.__id}"


new_student = NewStudent("haha", 99, "男")

new_student.setId(8888)
print(new_student.getId())

print(new_student)

# pass关键字(防止没写东西导致的语法错误检查)
class Nothing(NewStudent, Student):
    pass


# 类型注解

# 基本变量类型注解
var1: int = 10
var2: float = 8.9
var3: str = "shfishfdi"

# 基础容器类型注解
mylist: list = [1, 2, 3]
mytuple: tuple = (1, 2, 3)
mydict: dict = {"hahafh", 18}

# 容器类型详细注解
new_list: list[int] = [1, 2, 3]
new_tuple: tuple[int, str, float] = (18, "huhuhu", 88.7)

# 在注释中进行类型注解
var4 = None  # type:str
var5 = None  # type:tuple[int,str]

# 函数类型注解
def test(x: int, y: str) -> str:
    return f"{x}" + y


print(test(88, "haha"))

# 使用Union进行类型注解
from typing import Union


def haha(x: int, y: str, z: bool) -> Union[str, int]:
    if z:
        return x
    else:
        return y

print(haha(88,"838",True))
print(haha(88,"999",False))

#抽象类（接口）
class Animal:
    def spake(self):pass

class Cat(Animal):
    def spake(self):
        print("喵喵")

class Dog(Animal):
    def spake(self):
        print("汪汪")

cat=Cat()
dog=Dog()
cat.spake()
dog.spake()

#多态
def hurahuar(animal:Animal):
    animal.spake()

hurahuar(cat)
hurahuar(dog)
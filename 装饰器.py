#装饰器的闭包写法
def sleep():
    import random
    import time
    print("呼噜呼噜")
    time.sleep(random.randint(1,5))

def outer(func):
    def inner():
        print("我要睡了")
        func()
        print("我起床了")
    return inner

fn=outer(sleep)
fn()

#装饰器的快捷写法(语法糖)
def outer(func):
    def inner():
        print("我要睡了")
        func()
        print("我起床了")
    return inner

@outer
def sleep():
    import random
    import time
    print("呼噜呼噜")
    time.sleep(random.randint(1,5))

sleep()
import threading
import time

def thring_01(msg):
    while True:
        print(msg)
        time.sleep(1)


def thring_02(msg):
    while True:
        print(msg)
        time.sleep(1)

if __name__=='__main__':

    sing_thread=threading.Thread(target=thring_01,args=("我在唱歌",))
    dance_thread=threading.Thread(target=thring_02,kwargs={'msg':"我在跳舞"})

#开启线程
    sing_thread.start()
    dance_thread.start()
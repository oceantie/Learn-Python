import time
import threading
def coding():
    for x in range(3):
        print("i am writing %s" %threading.current_thread() )
        time.sleep(1)

def drawing():
    for x in range(3):
        print("i am drawing %s" %threading.current_thread())
        time.sleep(1)
#传统模式
# def main():
#     coding()
#     drawing()
def main():
    t1=threading.Thread(target=coding)
    t2 = threading.Thread(target=drawing)
    t1.start()
    t2.start()
    #查看线程数
    print(threading.enumerate())
if __name__=='__main__':
    main()
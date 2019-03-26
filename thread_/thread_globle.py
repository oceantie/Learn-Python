import threading
VALUE=0

gLock=threading.Lock()
def add_value():
    global VALUE
    #锁只用在修改全局变量的地方，访问不需要加锁
    gLock.acquire()
    for x in range(10):
        VALUE +=1
        print("="*10)
        print(VALUE)
    gLock.release()
    print('value:%d' %VALUE)
def main():
    for x in range(2):
        t=threading.Thread(target=add_value)
        t.start()

if __name__=='__main__':
    main()
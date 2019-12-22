from threading import Thread


class MyTrd1(Thread):
    def run(self):
        for i in range(1, 500):
            print("Hello! I am Thread 1")


class MyTrd2(Thread):
    def run(self):
        for i in range(1, 500):
            print("Hi! Thread 2")


t1 = MyTrd1()
t2 = MyTrd2()

t1.start()
t2.start()
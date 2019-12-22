from threading import Thread
from time import sleep


class MyTrd1(Thread):
    def run(self):
        while True:
            msg = input("Your message please: ")
            print(msg)


class MyTrd2(Thread):
    def run(self):
        while True:
            sleep(1)
            print("\nNew message from another thread.")


t1 = MyTrd1()
t2 = MyTrd2()

t1.start()
t2.start()
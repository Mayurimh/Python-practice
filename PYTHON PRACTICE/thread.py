from threading import*
import time
# def show():
#     print("this is child thread")
# t=Thread(target=show())
# t.start()
# print("this is parant therad")

# class Mythread:
#     def run(self):
#         for i in range(5):
#             print("\n this is child thread")
# obj=Mythread()
# t=Thread(target=obj.run())
# t.start()
# for i in range(5):
#     print("\n this is main thread")

class Demo:
    def number(self):
        for i in range(1,6):
            print("the number is ",i)
            time.sleep(1)
    def double(self):
        for i in range(1,6):
            print("the double of number is ",2*i)
            time.sleep(1)

    def triple(self):
        for i in range(1,6):
            print("the triple number is ",3*i)
            time.sleep(1)

obj=Demo()
t1=Thread(target=obj.number())
t2=Thread(target=obj.double())
t3=Thread(target=obj.triple())

t1.start()
time.sleep(0.2)
t2.start()
time.sleep(0.2)
t3.start()
time.sleep(0.2)

t1.join()
t2.join()
t3.join()

print("this is main thread")
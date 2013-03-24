import multitask
import time 

def fun_1():
    for i in range(5):
        print 'fun_1', i
        yield i
        
def fun_2():
    for i in range(8):
        print 'fun_2', i
        yield i
 
def fun_3():
    for i in range(5):
        print 'fun_3', i
        yield i

multitask.add(fun_1())
multitask.add(fun_2())
multitask.add(fun_3())

multitask.run()

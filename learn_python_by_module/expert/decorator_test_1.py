#coding=utf8

def oneLevelDecorator(function):
    def _decorator(*arg, **kw):
        print "开始装饰了"
        res = function(*arg, **kw)
        return res
    return _decorator
    
def fun(a, b):
    return a+b
    
print fun(3, 2)

fun2 = oneLevelDecorator(fun)

print fun2(5, 2)

def twoLevelDecorator(arg1, arg2):
    def oneLevelDecorator(function):
        def _decorator(*arg, **kw):
            print "开始装饰2了"
            print arg1, arg2
            res = function(*arg, **kw)
            return res
        return _decorator
    return oneLevelDecorator
    
@twoLevelDecorator(123, 423)
def fun3(a, b):
    return a * b
 
print fun3(3, 4)

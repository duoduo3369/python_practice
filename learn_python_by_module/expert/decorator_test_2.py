from itertools import izip

rpc_info = {}

def xmlrpc(in_=(), out=(type(None),)):
    def _xmlrpc(function):
        func_name = function.func_name
        rpc_info[func_name] = (in_, out)

        def _check_types(elements, types):
            # elements --> (1, 2)
            # types --> (<type 'int'>, <type 'int'>)
            if len(elements) != len(types):
                raise TypeError('argument count is wrong')
            typed = enumerate(izip(elements,types))
            #typed --> [(0, (1, <type 'int'>)), (1, (2, <type 'int'>))]

            for index, couple in typed:
                arg, of_the_right_type = couple
                if isinstance(arg,of_the_right_type):
                    continue
                raise TypeError("arg #%d should be %s" % (index,of_the_right_type))

        def __xmlrpc(*args):
            checkable_args = args[1:]
            
            _check_types(checkable_args, in_)
            res = function(*args)

            if not type(res) in (tuple,list):
                checkable_res = (res,)
            else:
                checkable_res = res
            
            _check_types(checkable_res,out)

            return res
        return __xmlrpc
    return _xmlrpc

class RPCView(object):

    @xmlrpc((int,int))
    def fun1(self,int1,int2):
        print 'receives %d and %d' % (int1,int2)

    @xmlrpc((str,),(int,))
    def fun2(self,phrase):
        print 'received %s' % phrase
        return 12

         
print rpc_info

my = RPCView()
print my.fun1(1,2)

print my.fun2('2')
print my.fun2(2)


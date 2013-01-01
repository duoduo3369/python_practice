# -*- coding: utf-8 *-*
"""
P319 8.3
"""

import gc
def dump_garbage():
    print u'\n垃圾:'
    gc.collect()
    print u'垃圾对象 :'
    for g in gc.garbage:
        s = str(g)
        if len(s) > 80:
            s = s[:77] + '_'
        print type(g),'\n ',s

if __name__ == '__main__':
    gc.enable()
    gc.set_debug(gc.DEBUG_LEAK)
    l = ['abc']
    l.append(l)
    del l
    dump_garbage()
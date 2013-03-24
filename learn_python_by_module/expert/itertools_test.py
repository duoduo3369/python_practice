from itertools import (tee, islice)

seq = list(range(10))

a = list(islice(seq, 1))
b = list(islice(seq, 5))
c = list(islice(seq, 8))

aa = list(islice(seq, 1, 5))
bb = list(islice(seq, 1, 8))

aaa = list(islice(seq, 1, None, 2)) 
bbb = list(islice(seq, 1, None, 3)) 

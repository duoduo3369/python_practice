import pickle
f = file('banner.p')
p = pickle.load(f)
f.close()

f = file('result.txt','w')
try:
    for line in p:
        l = ''.join([k*v for k,v in line])
        f.write(l+'\n')
finally:
    f.close()

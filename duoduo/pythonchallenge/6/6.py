#import zipfile
#z = zipfile.ZipFile("channel.zip", "r")

from log import logger

next_fn = '90052'
def get_path(file_name):
    return 'channel/' + file_name + '.txt'
i = 1
while i< 920:
    fname = get_path(next_fn)
    f = file(fname)
    s = f.read()    
    f.close()
    logger.info(s)
    print s
    next_fn = s.split()[-1]
    i += 1


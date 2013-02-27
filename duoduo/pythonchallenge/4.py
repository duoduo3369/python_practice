import urllib
from log_4 import logger
url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
suffix = "12345"
i = 0
while i < 405:
    try:
        s = urllib.urlopen(url+suffix).read()
        logger.info(s)
        suffix = s.split()[-1]
        i = i + 1
    except:
        print 'done'
        break
    

'''
Created on 2013-2-19

@author: Administrator
'''

import logging
import logging.config
logging.config.fileConfig("logging.conf")

#create logger
logger = logging.getLogger("user")


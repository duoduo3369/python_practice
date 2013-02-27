'''
Created on 2013-2-19

@author: Administrator
'''

import logging
import logging.config
logging.config.fileConfig("logging_4.conf")

#create logger
logger = logging.getLogger("4")

#"application" code
logger.debug("#########")
logger.info("info message")
logger.warn("warn message")
logger.error("error message")
logger.critical("critical message")
#logger.info()


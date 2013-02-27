'''
Created on 2013-2-19

@author: Administrator
'''
# test.py
import logging
import logging.config
logging.config.fileConfig("logging.conf")

#create logger
logger = logging.getLogger("example")

#"application" code
logger.debug("debug message")
logger.info("info message")
logger.warn("warn message")
logger.error("error message")
logger.critical("critical message")
#logger.info()
logHello = logging.getLogger("hello")
logHello.info("Hello world!")

if __name__ == '__main__':
    pass
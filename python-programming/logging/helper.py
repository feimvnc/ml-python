from cmath import log
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%j/%d/%Y %H:%M:%S')
# base logger 
logging.debug('debug msg')
logging.info('info msg')
logging.warning('warning msg')
logging.error('error msg')
logging.critical('critical msg')
# 345/11/2022 18:19:41 - root - CRITICAL - critical msg

# create owner logger , not from root 
import logging 
logger = logging.getLogger(__name__)
logger.info("hello from helper")

# create logger handler to handle diff outputs 
import logging 
logger = logging.getLogger(__name__)

# create handler 
stream_h = logging.StreamHandler(logging.WARNING)
file_h = logging.FileHandler('./file.log')

# level and format 
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)
logger.addHandler(stream_h)
logger.addFilter(file_h)

logger.warning('warning msg')
logger.error('error msg')

import traceback
# include traceback 
try: 
    a = [1,2,3]
    val = a[4]
except IndexError as e:
    logging.error(e, exc_info=True)
    logging.error("Error is %s", traceback.format_exc())
 
# rotating file handler 
import logging 
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler

# A double underscore prefix causes the Python interpreter to rewrite the attribute name 
# in order to avoid naming conflicts in subclasses
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# roll over after 2kb, and keep backup logs app.log.1, app.log.2 ...
handler = RotatingFileHandler('app.log', maxBytes=2000, backupCount=5)
logger.addHandler(handler)

for _ in range(10):
    logger.info('Hello world')

# time based logging handdler 
# from logging.handlers import TimedRotatingFileHandler
# handler = TimedRotatingFileHandler('timed_test.log', when='s', interval=5, backupCount = 5)
# logger.addHandler(handler)

# json logging for micro services 
# python json logger 
# pip install python-json-logger 
# import logging 
# from pythonjsonlogger import jsonlogger 
# logger = logging.getLogger()

# logHandler = logging.StreamHandler()
# formatter = jsonlogger.JsonFormatter()
# logHandler.setFormatter(formatter)
# logger.addHandle(logHandler)



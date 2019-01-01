#!/usr/bin/python2.7
# -*-coding:utf-8-*-
import sys
import time
import logging, traceback
from logging.handlers import RotatingFileHandler


class VaiLogs:
    @classmethod
    def getLoger(cls, iName="ROOT"):
        logging.basicConfig(level=logging.INFO)
        Loger = logging.getLogger(iName)
        mFormat = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
        mSavefp = "./log/" + iName + "_" + time.strftime('%Y%m%d', time.localtime(time.time())) + ".log"
        mHandle = RotatingFileHandler(mSavefp, maxBytes=5 * 1024 * 1024, backupCount=20)
        mHandle.setLevel(logging.DEBUG)
        mHandle.setFormatter(mFormat)
        Loger.addHandler(mHandle)
        return Loger

    @classmethod
    def logBack(cls, type, value, trace):
        print(trace, value, type)
        VaiLogs.error(value)
        sys.__excepthook__(type, value, trace)


VaiLogs = VaiLogs.getLoger()
# reload(sys)
# sys.excepthook = IAMSLoges.logBack
# sys.setdefaultencoding('utf-8')


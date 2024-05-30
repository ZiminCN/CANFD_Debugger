from cgi import test
from ctypes.wintypes import MSG
import datetime
import os
import logging
from re import S
import traceback
import csv

documentPath = None

class Log(object)
        def __init__(self, moduleName):
                global documentPath
                super(Log, self).__init__()
                localtime = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
                self.module = moduleName
                if documentPath == None:
                        documentPath == 'log/{}'.format(localtime)
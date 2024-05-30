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
                        self.__createDocument(documentPath)
                self.filePath = '{}/{}.txt'.format(documentPath, moduleName)
                self.allLogPath = '{}/{}.txt'.format(documentPath, 'all_log')
                
        def __createDocument(self, path):
                if not os.path.exists(path):
                        os.makedirs(path)
                        
        def __write2File(self, data):
                f = open(self.filePath, 'a')
                f2 = open(self.allLogPath, 'a')
                f.write(data)
                f2.write(data)
                f.close()
                f2.close()
                
        def __prefix(self, level):
                localtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
                return '[%s][%s][%s]' % (localtime, level, self.module)
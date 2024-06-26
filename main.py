#
# Copyright (c) Direct Drive Technology Co., Ltd. All rights reserved.
# Author: zimin <jianming.zeng@directdrivetech.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from PyQt5.QtWidgets import *
from PyQt5 import QtCore

import sys,traceback


def Exception(tp, val, tb):
    log = Log('Exception')
    traceList = traceback.format_tb(tb)
    html = repr(tp) + "\n"
    html += (repr(val) + "\n")
    for line in traceList:
        html += (line + "\n")
    log.error(html)
    exit()

if __name__ == '__main__':
        print("Running test python!\r\n")
#!/usr/bin/env python
# -*- coding: UTF-8
import os
from datetime import date
'''
    Logger class that will save all of our issues inside the log dir
'''
__author__ = 'Jose Epifanio'
__licence__ = 'MIT'
__version__ = '0.0.1'
__email__ = 'jose.epifanio90@gmail.com'
__status__ = 'Development'


class Logger:
    def log(self, exc: str, msg: str) -> None:
        file_name = f'./bear_api/logs/log-{date.today()}.txt'
        mode = 'a' if os.path.exists(file_name) else 'w'
        file = open(file_name, f'{mode}+')
        last_line = file.readlines()
        if len(last_line) != 0:
            last_line = last_line[-1]
            counter = last_line[last_line.find('#') + 1: last_line.find('-') - 1]  # nopep8
            counter = int(counter) + 1
        else:
            counter = 0
        file.write(
            f'Exception #{counter} - '
            f'MESSAGE: {exc} - {msg}\n'
        )
        file.close()

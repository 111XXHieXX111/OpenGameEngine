import inspect
import time
import os

class Logging:
    def __init__(self):
        self.console = False
        self.last_log = ""
        self.debug = True

        self.log = []
    
    def getfile(self):
        frame = inspect.currentframe().f_back.f_back
        caller_file = os.path.basename(frame.f_code.co_filename)
        return caller_file
    
    def _log_add(self, text:str, maincolor:str, tag:str):
        timestamp = time.strftime("%H:%M:%S", time.localtime())

        log_text = f"{maincolor}{tag}|{timestamp}: {text}\033[0m"
        if self.console and self.last_log != text:
            print(log_text)

        self.last_log = text

        self.log.append(log_text)

    def AddInfo(self, text:str):
        self._log_add(text, '', 'INFO')

    def AddDInfo(self, text:str):
        if self.debug:
            self._log_add(text, '\033[96m', 'DINF')

    def AddWarn(self, text:str):
        self._log_add(text, '\033[33m', 'WARN')

    def AddDWarn(self, text:str):
        if self.debug:
            self._log_add(text, '\033[93m', 'DWAR')

    def AddError(self, text:str):
        self._log_add(text, '\033[31m', 'ERR ')

    def AddDError(self, text:str):
        if self.debug:
            self._log_add(text, '\033[91m', 'DERR')

    def AddCritical(self, text:str):
        self._log_add(text, '\033[31m\033[1m', 'CRIT')

    def ConsoleStream(self, stream:bool=True):
        self.console = stream

    def GetLog(self):
        for line in self.log:
            print(line)

    def SaveLog(self):
        log = 'EXPORTED LOG\n'
        for line in self.log:
            log += line + '\n'
        
        with open(str(time.time()) + '_log.txt', 'w') as f:
            f.write(log)

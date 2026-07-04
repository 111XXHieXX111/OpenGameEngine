from .modules import time, inspect, os

class Logging:
    def __init__(self, addtime:bool=True, colored:bool=False, calledfile:bool=False):
        self.addtime = addtime
        self.console = False
        self.colored = colored
        self.calledfile = calledfile

        self.log = []

    def getfile(self):
        frame = inspect.currentframe().f_back.f_back
        caller_file = os.path.basename(frame.f_code.co_filename)
        return caller_file
    
    def addInfo(self, text:str):
        if self.colored:
            pre = '<\033[34mINFO\033[0m> '
        else:
            pre = '<INFO> '
        
        if self.calledfile:
            if self.colored:
                pre += f'(\033[1m{self.getfile()}\033[0m) '
            else:
                pre += f'({self.getfile()}) '
        
        if self.addtime:
            if self.colored:
                pre += f'[\033[90m{time.strftime("%H:%M:%S", time.localtime())}\033[0m] -> '
            else:
                pre += f'[{time.strftime("%H:%M:%S", time.localtime())}] -> '
        self.log.append(pre + text)
        if self.console:
            print(pre + text)
    
    def addWarn(self, text:str):
        if self.colored:
            pre = '<\033[33mWARN\033[0m> '
        else:
            pre = '<WARN> '
        
        if self.calledfile:
            if self.colored:
                pre += f'(\033[1m{self.getfile()}\033[0m) '
            else:
                pre += f'({self.getfile()})'
        
        if self.addtime:
            if self.colored:
                pre += f'[\033[90m{time.strftime("%H:%M:%S", time.localtime())}\033[0m] -> '
            else:
                pre += f'[{time.strftime("%H:%M:%S", time.localtime())}] -> '
        self.log.append(pre + text)
        if self.console:
            print(pre + text)

    def addError(self, text:str):
        if self.colored:
            pre = '<\033[31mERROR\033[0m> '
        else:
            pre = '<ERROR> '
        
        if self.calledfile:
            if self.colored:
                pre += f'(\033[1m{self.getfile()}\033[0m) '
            else:
                pre += f'({self.getfile()})'
        
        if self.addtime:
            if self.colored:
                pre += f'[\033[90m{time.strftime("%H:%M:%S", time.localtime())}\033[0m] -> '
            else:
                pre += f'[{time.strftime("%H:%M:%S", time.localtime())}] -> '
        self.log.append(pre + text)
        if self.console:
            print(pre + text)

    def addCritical(self, text:str):
        if self.colored:
            pre = '<\033[31m\033[1mCRITICAL\033[0m> '
        else:
            pre = '<ERROR> '
        
        if self.calledfile:
            if self.colored:
                pre += f'(\033[1m{self.getfile()}\033[0m) '
            else:
                pre += f'({self.getfile()})'
        
        if self.addtime:
            if self.colored:
                pre += f'[\033[90m{time.strftime("%H:%M:%S", time.localtime())}\033[0m] -> '
            else:
                pre += f'[{time.strftime("%H:%M:%S", time.localtime())}] -> '
        self.log.append(pre + text)
        if self.console:
            print(pre + text)

    def consoleStream(self, stream:bool=True):
        self.console = stream

    def getLog(self):
        for line in self.log:
            print(line)

    def saveLog(self):
        log = 'EXPORTED LOG\n'
        for line in self.log:
            log += line + '\n'
        
        with open(str(time.time()) + '_log.txt', 'w') as f:
            f.write(log)

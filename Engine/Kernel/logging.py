from .modules import time, inspect, os, threading, queue

class Logging:
    def __init__(self):
        self.console = False
        self.last_log = ""

        self.log = []
        self.queue = queue.Queue()

        threading.Thread(target=self._console_process, daemon=True).start()

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

    def addInfo(self, text:str):
        self.queue.put([text, '', 'INFO'])

    def addDInfo(self, text:str):
        self.queue.put([text, '\033[96m', 'DINF'])

    def addWarn(self, text:str):
        self.queue.put([text, '\033[33m', 'WARN'])

    def addDWarn(self, text:str):
        self.queue.put([text, '\033[93m', 'DWAR'])

    def addError(self, text:str):
        self.queue.put([text, '\033[31m', 'ERR '])

    def addDError(self, text:str):
        self.queue.put([text, '\033[91m', 'DERR'])

    def addCritical(self, text:str):
        self.queue.put([text, '\033[31m\033[1m', 'CRIT'])

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

    def _console_process(self):
        while True:
            try:
                item = self.queue.get(timeout=0.1)
                self._log_add(item[0], item[1], item[2])
                self.queue.task_done()
            except queue.Empty:
                continue
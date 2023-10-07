import time

threadCondition:bool = True
_stateOfEmergency:bool = False
addressWhereSendEmergency:int = 0


class _terminalLog:
    def __init__(self):
        self.startProgramTime:float = time.time()

    def print(self, _condition:bool, _message:str):
        printTime:float = time.time()

        if(_condition):
            print("[%8.3f] "%(printTime - self.startProgramTime) + "[  OK  ] : " + _message)
        else:
            print("[%8.3f] "%(printTime - self.startProgramTime) + "[FAILED] : " + _message)
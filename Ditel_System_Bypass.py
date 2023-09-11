import time
from Ditel_DROS_Kernel import threadCondition

HEAD_WORD = 254
NO_SEND_DATA = 253

class ditelSystemBypass:
    def __init__(self, _address:int):
        self.avaiableData:bool = False
        self.toTxUse:bool = True
        self.requestSendData:bool = False
        self.readData:bytes = [None] * 6
        self.sendData:bytes = [None] * 6
        self.bypassAddress:int = _address
        
    def read(self):
        return self.readData
    
    def avaiable(self):
        return self.avaiableData
    
    def sendCommand(self, _command:bytes):
        while ((self.requestSendData != False) and (threadCondition == True)):
            time.sleep(0.001)
        self.requestSendData = True
        self.sendData[0] = HEAD_WORD
        self.sendData[1] = _command
        self.sendData[2] = NO_SEND_DATA
        self.sendData[3] = NO_SEND_DATA
        self.sendData[4] = NO_SEND_DATA
        self.sendData[5] = NO_SEND_DATA
    
    def send(self, _sendData:bytes):
        while ((self.requestSendData != False) and (threadCondition == True)):
            time.sleep(0.001)
        self.requestSendData = True
        for _i in range(0, 6, 1):
            self.sendData[_i] = _sendData[_i]
        

bypass = [None, 
          ditelSystemBypass(1), 
          ditelSystemBypass(2), 
          ditelSystemBypass(3), 
          ditelSystemBypass(4), 
          ditelSystemBypass(5), 
          ditelSystemBypass(6), 
          ditelSystemBypass(7), 
          ditelSystemBypass(8), 
          ditelSystemBypass(9), 
          ditelSystemBypass(10), 
          ditelSystemBypass(11), 
          ditelSystemBypass(12), 
          ditelSystemBypass(13), 
          ditelSystemBypass(14), 
          ditelSystemBypass(15), 
          ditelSystemBypass(16), 
          ditelSystemBypass(17), 
          ditelSystemBypass(18), 
          ditelSystemBypass(19), 
          ditelSystemBypass(20), 
         ]


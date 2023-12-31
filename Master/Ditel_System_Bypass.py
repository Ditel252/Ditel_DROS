import time
from Ditel_DROS_Kernel import threadCondition

HEAD_WORD =     254
NO_SEND_DATA =  242
INT_UNIT_MAX =  241

SEND_INT_MAX =  1600000000
SEND_INT_MIN =  -1600000000
SEND_INT_BASE = 1600000000

class ditelSystemBypass:
    def __init__(self, _address:int):
        self.avaiableData:bool = False
        self.toTxUse:bool = True
        self.requestAvaiableData:bool = False
        self.requestSendData:bool = False
        self.readData:bytes = [None] * 6
        self.sendData:bytes = [None] * 6
        self.bypassAddress:int = _address
        
    def read(self):
        return self.readData
    
    def readInt(self):
        _readData_Int:bytes = [None]*6

        _readData_Int = self.read()

        _readInt = [None]*2

        _readInt[0] = _readData_Int[1]
        _readInt[1] = _readData_Int[2] * INT_UNIT_MAX * INT_UNIT_MAX * INT_UNIT_MAX + _readData_Int[3] * INT_UNIT_MAX * INT_UNIT_MAX + _readData_Int[4] * INT_UNIT_MAX + _readData_Int[5]

        _readInt[1] -= SEND_INT_BASE
        
        return _readInt
    
    def readCommand(self):
        _readData_Command:bypass = [None]*6

        _readData_Command = self.read()

        _readCommand:bypass = _readData_Command[1]

        return _readCommand
    
    def avaiable(self):
        self.requestAvaiableData = True

        while(self.requestAvaiableData == True):
            time.sleep(0.001)

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
    
    def sendInt(self, _sendIntCommand:bytes, _sendInt:int):
        if(_sendInt > SEND_INT_MAX or _sendInt < SEND_INT_MIN):
            return False
        
        _sendInt += SEND_INT_BASE

        _sendData_Int:bytes = [None]*6

        _sendData_Int[0] = HEAD_WORD
        _sendData_Int[1] = _sendIntCommand

        _sendData_Int[2] = int(_sendInt / (INT_UNIT_MAX * INT_UNIT_MAX * INT_UNIT_MAX))
        _sendInt -= _sendData_Int[2] * INT_UNIT_MAX * INT_UNIT_MAX * INT_UNIT_MAX

        _sendData_Int[3] = int(_sendInt / (INT_UNIT_MAX * INT_UNIT_MAX))
        _sendInt -= _sendData_Int[2] * INT_UNIT_MAX * INT_UNIT_MAX

        _sendData_Int[4] = int(_sendInt / (INT_UNIT_MAX))
        _sendInt -= _sendData_Int[4] * INT_UNIT_MAX
        
        _sendData_Int[5] = int(_sendInt)
        _sendInt -= _sendData_Int[5]

        if(_sendInt != 0):
            return False

        self.send(_sendData_Int)

        return True
    
    def convertToInt(self, _convertData:bytes):
        _result:int = [None]*2

        _result[0] = _convertData[1]
        _result[1] = _convertData[2] * INT_UNIT_MAX * INT_UNIT_MAX * INT_UNIT_MAX + _convertData[3] * INT_UNIT_MAX * INT_UNIT_MAX + _convertData[4] * INT_UNIT_MAX + _convertData[5]

        _result[1] -= SEND_INT_BASE

        return _result
        

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
import struct
import glob
import serial
import threading
import time
import Ditel_DROS_Kernel
from Ditel_System_Bypass import bypass

HEAD_WORD = 254
NO_SEND_DATA = 253

COMMAND_CHECK_ADDRESS =         200
COMMAND_COMMUNICATION_BEGIN =   201
COMMAND_COMMUNICATION_END =     202
COMMAND_DECLARE_EMERGENCY =    203

def addressRead(_portName:str):
        serial1 = serial.Serial(_portName, 115200, timeout=0.2)

        serial1.write(bytes([int(HEAD_WORD)]))
        serial1.write(bytes([int(COMMAND_CHECK_ADDRESS)]))
        serial1.write(bytes([int(NO_SEND_DATA)]))
        serial1.write(bytes([int(NO_SEND_DATA)]))
        serial1.write(bytes([int(NO_SEND_DATA)]))
        serial1.write(bytes([int(NO_SEND_DATA)]))

        returnAddressData = serial1.readline()

        try:
            result:bytes = struct.unpack('8B', returnAddressData)

            serial1.close()

            return result
        except:
            return [0,0,0,0,0,0]
        
def portsRead():  #ポートを取得しすべてのPassを格納した配列を返す
        ports = glob.glob('/dev/tty[A-Za-z]*')

        result = []

        for port in ports:
            try:
                s = serial.Serial(port)
                s.close
                result.append(port)
            except (OSError, serial.SerialException):
                pass

        return result

class ditelSerial:
    def __init__(self, _sysAddress:int, _sysPortName:str):
        self.portName:str = _sysPortName
        self._serialAvaiableVariable:bool = False

        self._log_condition:bool = False
        self._log_contents:str = None
        self._rxLog:str =   None
        self._txLog:str =   None
        
        self.readData:bytes = [None]*6
        
        self.serialModule = serial.Serial(self.portName, 115200, timeout=0.2)
        self.useAddress:int = _sysAddress

    def _sysSerialRead(self):
        while Ditel_DROS_Kernel.threadCondition:
            self._serialAvaiableVariable = False

            sysSerialReadData:str = self.serialModule.readline()

            try:
                sysReadData:bytes = struct.unpack('8B', sysSerialReadData)

                if(sysReadData[0] == HEAD_WORD):
                    self._serialAvaiableVariable = True

                    if(sysReadData[1] == COMMAND_DECLARE_EMERGENCY):
                        Ditel_DROS_Kernel.addressWhereSendEmergency = self.useAddress
                    
                    for _i in range(0, 6, 1):
                        self.readData[_i] = sysReadData[_i]

                    self.rxLogPrint(self.readData[0], self.readData[1], self.readData[2], self.readData[3], self.readData[4], self.readData[5])

                    time.sleep(0.2)
                else:
                    pass
            except:
                pass

    def begin(self):
        try:
            self.serialThread = threading.Thread(target=self._sysSerialRead)
            self.serialThread.start()

            if (self.sendCommand(COMMAND_COMMUNICATION_BEGIN) == True):
                return True
            else:
                return False
        except:
            return False
        
    def send(self, _sendData:bytes):
        while (bypass[self.useAddress].toTxUse != True):
            time.sleep(0.001)
        bypass[self.useAddress].toTxUse = False
        self.serialModule.write(bytes([int(_sendData[0])]))
        self.serialModule.write(bytes([int(_sendData[1])]))
        self.serialModule.write(bytes([int(_sendData[2])]))
        self.serialModule.write(bytes([int(_sendData[3])]))
        self.serialModule.write(bytes([int(_sendData[4])]))
        self.serialModule.write(bytes([int(_sendData[5])]))

        self.txLogPrint(_sendData[0], _sendData[1], _sendData[2], _sendData[3], _sendData[4], _sendData[5])

        _readReturnDataTime = 0
        while(self.avaiable() == False):
            if(_readReturnDataTime >= 15):
                break
        
            time.sleep(0.02)
            _readReturnDataTime += 1
        
        if(_readReturnDataTime < 15):
            _returnData = self.read()
            bypass[self.useAddress].toTxUse = True

            if((_returnData[0] == _sendData[0]) and (_returnData[1] == _sendData[1] + 10)):
                return True
            else:
                return False
        else:
            bypass[self.useAddress].toTxUse = True
            return False
        
    def sendCommand(self, _command:bytes):
        while (bypass[self.useAddress].toTxUse != True):
            time.sleep(0.001)
        bypass[self.useAddress].toTxUse = False
        self.serialModule.write(bytes([int(HEAD_WORD)]))
        self.serialModule.write(bytes([int(_command)]))
        self.serialModule.write(bytes([int(NO_SEND_DATA)]))
        self.serialModule.write(bytes([int(NO_SEND_DATA)]))
        self.serialModule.write(bytes([int(NO_SEND_DATA)]))
        self.serialModule.write(bytes([int(NO_SEND_DATA)]))

        self.txLogPrint(HEAD_WORD, _command, NO_SEND_DATA, NO_SEND_DATA, NO_SEND_DATA, NO_SEND_DATA)

        _readReturnDataTime = 0
        while(self.avaiable() == False):
            if(_readReturnDataTime >= 15):
                break
        
            time.sleep(0.02)
            _readReturnDataTime += 1
        
        if(_readReturnDataTime < 15):
            _returnData = self.read()
            bypass[self.useAddress].toTxUse = True

            if((_returnData[0] == HEAD_WORD) and (_returnData[1] == _command + 10)):
                return True
            else:
                return False
        else:
            bypass[self.useAddress].toTxUse = True
            return False


    def read(self):
         return self.readData

    def avaiable(self):
        return self._serialAvaiableVariable
    
    def logPrint(self, _condition:bool, _logInfo:str):
        self._log_condition = _condition
        self._log_contents = _logInfo

    def txLogPrint(self, _txLogInfo0:int, _txLogInfo1:int, _txLogInfo2:int, _txLogInfo3:int, _txLogInfo4:int,_txLogInfo5:int):
        self._txLog = str(_txLogInfo0) + ":" + str(_txLogInfo1) + ":" + str(_txLogInfo2) + ":" + str(_txLogInfo3) + ":" + str(_txLogInfo4) + ":" + str(_txLogInfo5)

    def rxLogPrint(self, _rxLogInfo0:int, _rxLogInfo1:int, _rxLogInfo2:int, _rxLogInfo3:int, _rxLogInfo4:int,_rxLogInfo5:int):
        self._rxLog = str(_rxLogInfo0) + ":" + str(_rxLogInfo1) + ":" + str(_rxLogInfo2) + ":" + str(_rxLogInfo3) + ":" + str(_rxLogInfo4) + ":" + str(_rxLogInfo5)

    def end(self):
        if(Ditel_DROS_Kernel.threadCondition == False):
            try:
                self.serialThread.join()
                return True
            except:
                return False
        else:
            return False
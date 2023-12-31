import struct
import glob
import serial
import threading
import time
import Ditel_DROS_Kernel
from Ditel_System_Bypass import bypass

HEAD_WORD:bytes =                   254
NO_SEND_DATA:bytes =                242
INT_UNIT_MAX:bytes =                241
COMMUNICATION_BASE_VALUE:bytes =    11

COMMAND_CHECK_ADDRESS:bytes =       200
COMMAND_COMMUNICATION_BEGIN:bytes = 201
COMMAND_COMMUNICATION_END:bytes =   202
COMMAND_DECLARE_EMERGENCY:bytes =   203

SEND_INT_MAX:int =  1600000000
SEND_INT_MIN:int =  -1600000000
SEND_INT_BASE:int = 1600000000

def addressRead(_portName:str):
        serial1 = serial.Serial(_portName, 115200, timeout=1)

        serial1.write(bytes([int(HEAD_WORD)]))
        serial1.write(bytes([int(COMMAND_CHECK_ADDRESS + COMMUNICATION_BASE_VALUE)]))
        serial1.write(bytes([int(NO_SEND_DATA + COMMUNICATION_BASE_VALUE)]))
        serial1.write(bytes([int(NO_SEND_DATA + COMMUNICATION_BASE_VALUE)]))
        serial1.write(bytes([int(NO_SEND_DATA + COMMUNICATION_BASE_VALUE)]))
        serial1.write(bytes([int(NO_SEND_DATA + COMMUNICATION_BASE_VALUE)]))

        returnAddressData = serial1.readline()

        try:
            result:bytes = struct.unpack('8B', returnAddressData)

            resultAddress:bytes = [None]*6

            serial1.close()

            resultAddress[0] = result[0]

            for _i in range(1, 6, 1):
                resultAddress[_i] = result[_i] - COMMUNICATION_BASE_VALUE

            return resultAddress
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
        self._readDataIsReturnData:bool =   False

        self._log_condition:bool = False
        self._log_contents:str = None
        self._rxLog:str =   None
        self._txLog:str =   None
        
        self.readData:bytes = [None]*6
        
        self.serialModule = serial.Serial(self.portName, 115200, timeout=0.2)
        self.useAddress:int = _sysAddress

    def _sysSerialRead(self):
        while True:
            sysSerialReadData:str = self.serialModule.readline()

            try:
                sysReadData:bytes = struct.unpack('8B', sysSerialReadData)

                if(sysReadData[0] == HEAD_WORD):
                    self._serialAvaiableVariable = True

                    self.rxLogPrint(sysReadData[0], sysReadData[1], sysReadData[2], sysReadData[3], sysReadData[4], sysReadData[5])
                    Ditel_DROS_Kernel.terminalLog.print(True, "Address{:2d} Read | {:3d}:{:3d}:{:3d}:{:3d}:{:3d}:{:3d}".format(self.useAddress, int(sysReadData[0]), int(sysReadData[1]), int(sysReadData[2]), int(sysReadData[3]), int(sysReadData[4]), int(sysReadData[5])))
                    
                    self.readData[0] = sysReadData[0]
                    for _i in range(1, 6, 1):
                        self.readData[_i] = sysReadData[_i] - COMMUNICATION_BASE_VALUE

                    if(self._readDataIsReturnData == False):
                        while (bypass[self.useAddress].toTxUse != True):
                            time.sleep(0.001)
                        
                        bypass[self.useAddress].toTxUse = False
                        self.serialModule.write(bytes([int(self.readData[0])]))
                        self.serialModule.write(bytes([int(self.readData[1] + COMMUNICATION_BASE_VALUE + 10)]))
                        self.serialModule.write(bytes([int(self.readData[2] + COMMUNICATION_BASE_VALUE)]))
                        self.serialModule.write(bytes([int(self.readData[3] + COMMUNICATION_BASE_VALUE)]))
                        self.serialModule.write(bytes([int(self.readData[4] + COMMUNICATION_BASE_VALUE)]))
                        self.serialModule.write(bytes([int(self.readData[5] + COMMUNICATION_BASE_VALUE)]))

                        self.txLogPrint(self.readData[0], self.readData[1] + COMMUNICATION_BASE_VALUE + 10, self.readData[2] + COMMUNICATION_BASE_VALUE, self.readData[3] + COMMUNICATION_BASE_VALUE, self.readData[4] + COMMUNICATION_BASE_VALUE, self.readData[5] + COMMUNICATION_BASE_VALUE)
                        Ditel_DROS_Kernel.terminalLog.print(True, "Address{:2d} Send | {:3d}:{:3d}:{:3d}:{:3d}:{:3d}:{:3d}".format(self.useAddress, int(sysReadData[0]), int(sysReadData[1]), int(sysReadData[2]), int(sysReadData[3]), int(sysReadData[4]), int(sysReadData[5])))

                        bypass[self.useAddress].toTxUse = True

                    if(self.readData[1] == COMMAND_DECLARE_EMERGENCY):
                        Ditel_DROS_Kernel._stateOfEmergency = True
                        Ditel_DROS_Kernel.addressWhereSendEmergency = self.useAddress
                else:
                    pass
            except:
                pass

            if(Ditel_DROS_Kernel.threadCondition == False):
                break

    def begin(self):
        try:
            self.serialThread = threading.Thread(target=self._sysSerialRead)
            self.serialThread.start()

            Ditel_DROS_Kernel.terminalLog.print(True, "serial begin")

            if (self.sendCommand(COMMAND_COMMUNICATION_BEGIN) == True):
                return True
            else:
                return False
        except:
            Ditel_DROS_Kernel.terminalLog.print(False, "serial begin")
            return False
        
    def send(self, _sendData:bytes):
        while (bypass[self.useAddress].toTxUse != True):
            time.sleep(0.001)
        
        self._readDataIsReturnData = True
        
        bypass[self.useAddress].toTxUse = False
        self.serialModule.write(bytes([int(_sendData[0])]))
        self.serialModule.write(bytes([int(_sendData[1] + COMMUNICATION_BASE_VALUE)]))
        self.serialModule.write(bytes([int(_sendData[2] + COMMUNICATION_BASE_VALUE)]))
        self.serialModule.write(bytes([int(_sendData[3] + COMMUNICATION_BASE_VALUE)]))
        self.serialModule.write(bytes([int(_sendData[4] + COMMUNICATION_BASE_VALUE)]))
        self.serialModule.write(bytes([int(_sendData[5] + COMMUNICATION_BASE_VALUE)]))

        self.txLogPrint(_sendData[0], _sendData[1] + COMMUNICATION_BASE_VALUE, _sendData[2] + COMMUNICATION_BASE_VALUE, _sendData[3] + COMMUNICATION_BASE_VALUE, _sendData[4] + COMMUNICATION_BASE_VALUE, _sendData[5] + COMMUNICATION_BASE_VALUE)
        Ditel_DROS_Kernel.terminalLog.print(True, "Address%2d Read | %3d:%3d:%3d:%3d:%3d:%3d" % (self.useAddress, int(_sendData[0]), int(_sendData[1] + COMMUNICATION_BASE_VALUE), int(_sendData[2] + COMMUNICATION_BASE_VALUE), int(_sendData[3] + COMMUNICATION_BASE_VALUE), int(_sendData[4] + COMMUNICATION_BASE_VALUE), int(_sendData[5] + COMMUNICATION_BASE_VALUE)))
        _readReturnDataTime = 0
        while(self._serialAvaiableVariable == False):
            if(_readReturnDataTime >= 15):
                break
        
            time.sleep(0.02)
            _readReturnDataTime += 1

        self._serialAvaiableVariable = False

        self._readDataIsReturnData = False
        
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
        
    def unconditional(self):
        return Ditel_DROS_Kernel.threadCondition
        
    def sendCommand(self, _command:bytes):
        _sendData_Command:bytes = [None]*6

        _sendData_Command[0] = HEAD_WORD
        _sendData_Command[1] = _command
        _sendData_Command[2] = NO_SEND_DATA
        _sendData_Command[3] = NO_SEND_DATA
        _sendData_Command[4] = NO_SEND_DATA
        _sendData_Command[5] = NO_SEND_DATA

        return self.send(_sendData_Command)
        
    def sendInt(self, _sendIntCommand:bytes, _sendInt:int):
        _sendData_Int:bytes = [None]*6

        if(_sendInt > SEND_INT_MAX or _sendInt < SEND_INT_MIN):
            return False

        _sendInt += SEND_INT_BASE

        _sendData_Int[0] = HEAD_WORD
        _sendData_Int[1] = _sendIntCommand

        _sendData_Int[2] = int(_sendInt / (INT_UNIT_MAX * INT_UNIT_MAX * INT_UNIT_MAX))
        _sendInt -= _sendData_Int[2] * INT_UNIT_MAX * INT_UNIT_MAX * INT_UNIT_MAX

        _sendData_Int[3] = int(_sendInt / (INT_UNIT_MAX * INT_UNIT_MAX))
        _sendInt -= _sendData_Int[3] * INT_UNIT_MAX * INT_UNIT_MAX

        _sendData_Int[4] = int(_sendInt / (INT_UNIT_MAX))
        _sendInt -= _sendData_Int[4] * INT_UNIT_MAX
        
        _sendData_Int[5] = int(_sendInt)
        _sendInt -= _sendData_Int[5]

        if(_sendInt != 0):
            self.logPrint(False, "send int data")
            return False

        return self.send(_sendData_Int)


    def read(self):
         return self.readData
    
    def readCommand(self):
        _readData_Command:bytes = [None]*6

        _readData_Command = self.read()

        _readCommand:bytes = _readData_Command[1]

        return _readCommand
    
    def readInt(self):
        _readData_Int:bytes = [None]*6

        _readData_Int = self.read()

        _readInt:int = [None]*2

        _readInt[0] = _readData_Int[1]
        _readInt[1] = (_readData_Int[2] * INT_UNIT_MAX * INT_UNIT_MAX * INT_UNIT_MAX) + (_readData_Int[3] * INT_UNIT_MAX * INT_UNIT_MAX) + (_readData_Int[4] * INT_UNIT_MAX) + _readData_Int[5]

        _readInt[1] -= SEND_INT_BASE
        
        return _readInt

    def avaiable(self):
        if((self._serialAvaiableVariable == True) and (self._readDataIsReturnData == False)):
            self._serialAvaiableVariable = False
            return True
        else:
            return False
    
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
        
    def stateOfEmergency(self):
        return Ditel_DROS_Kernel._stateOfEmergency
    
    def convertToInt(self, _convertData:bytes):
        _result:int = [None]*2

        _result[0] = _convertData[1]
        _result[1] = _convertData[2] * INT_UNIT_MAX * INT_UNIT_MAX * INT_UNIT_MAX + _convertData[3] * INT_UNIT_MAX * INT_UNIT_MAX + _convertData[4] * INT_UNIT_MAX + _convertData[5]

        _result[1] -= SEND_INT_BASE

        return _result
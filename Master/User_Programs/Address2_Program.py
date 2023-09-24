"""=======================================
<DROS User Program>
Address : 2
======================================="""

from Ditel_Serial import *
from Ditel_System_Bypass import bypass
from User_Programs.Data_Bypass import dataBypass


#===============↓↓User記入(ここから)↓↓===============

#===============↑↑User記入(ここまで)↑↑===============


class program:
#===============↓↓User記入(ここから)↓↓===============

    def __init__(self, _portName:str):  #変数の宣言はここ
        self._serial = ditelSerial(2, _portName)    #削除禁止

        self.readData:bytes = [None]*6
        self.readIntData:int = [None]*2

    def _setup(self):   #通信が始まった際に1回だけ実行される関数
        pass

    def _loop(self):    #_setup関数が終了した後に実行される関数, 関数は無条件ループする
        while(self._serial.unconditional()):
            if(bypass[1].avaiable() == True):
                self.readData = bypass[1].read()
    
                if(self.readData[1] != READ_FAILURE):
                    self._serial.logPrint(True, "read Data")

                    break
                else:
                    self._serial.logPrint(False, "read Data")
                time.sleep(0.05)

        if(self.readData[1] == 150):
            self.readIntData = self._serial.convertToInt(self.readData)

            self._serial.logPrint(True, "read = " + str(self.readIntData[0]) + " : " +  str(self.readIntData[1]))

            self.readIntData[0] += 1
            self.readIntData[1] += 1

            while(self._serial.unconditional()):
                if(self._serial.sendInt(self.readIntData[0],self.readIntData[1]) == True):
                    self._serial.logPrint(True, "send = " + str(self.readIntData[0]) + " : " +  str(self.readIntData[1]))
                    break
                else:
                    self._serial.logPrint(False, "send = " + str(self.readIntData[0]) + " : " +  str(self.readIntData[1]))
                    time.sleep(0.05)

#===============↑↑User記入(ここまで)↑↑===============
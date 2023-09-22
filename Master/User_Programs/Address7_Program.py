"""=======================================
<DROS User Program>
Address : 7
======================================="""

from Ditel_Serial import *
from Ditel_System_Bypass import bypass
from User_Programs.Data_Bypass import dataBypass


#===============↓↓User記入(ここから)↓↓===============

#===============↑↑User記入(ここまで)↑↑===============


class program:
#===============↓↓User記入(ここから)↓↓===============

    def __init__(self, _portName:str):  #変数の宣言はここ
        self._serial = ditelSerial(7, _portName)    #削除禁止

    def _setup(self):   #通信が始まった際に1回だけ実行される関数
        pass

    def _loop(self):    #_setup関数が終了した後に実行される関数, 関数は無条件ループする
        pass

#===============↑↑User記入(ここまで)↑↑===============
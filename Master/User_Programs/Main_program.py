"""=======================================
<DROS User Program>
Main
======================================="""

from Ditel_System_Bypass import bypass
from User_Programs.Data_Bypass import dataBypass
import time

class program:
#===============↓↓User記入(ここから)↓↓===============

    def __init__(self): #変数の宣言はここ
        pass

    def _setup(self):   #通信が始まった際に1回だけ実行される関数
        pass

    def _loop(self):    #_setup関数が終了した後に実行される関数, 関数は無条件ループする
        pass

    def _emergencyProgram(self):    #緊急事態が宣言された際に実行される関数
        pass

#===============↑↑User記入(ここまで)↑↑===============
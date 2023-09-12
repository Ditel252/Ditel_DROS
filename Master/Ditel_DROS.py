"""=======================================
<Ditel Robot Operateting System>
バージョン : v1.1.5
======================================="""

import tkinter
import tkinter.ttk
import tkinter.filedialog
import Ditel_DROS_Kernel
from Ditel_Serial import *
import time
import Ditel_System_Bypass

import User_Programs.Address1_Program as add1
import User_Programs.Address2_Program as add2
import User_Programs.Address3_Program as add3
import User_Programs.Address4_Program as add4
import User_Programs.Address5_Program as add5
import User_Programs.Address6_Program as add6
import User_Programs.Address7_Program as add7
import User_Programs.Address8_Program as add8
import User_Programs.Address9_Program as add9
import User_Programs.Address10_Program as add10
import User_Programs.Address11_Program as add11
import User_Programs.Address12_Program as add12
import User_Programs.Address13_Program as add13
import User_Programs.Address14_Program as add14
import User_Programs.Address15_Program as add15
import User_Programs.Address16_Program as add16
import User_Programs.Address17_Program as add17
import User_Programs.Address18_Program as add18
import User_Programs.Address19_Program as add19
import User_Programs.Address20_Program as add20
import User_Programs.Main_program as addMain


#===============↓↓定数の宣言(ここから)↓↓===============
#バージョン設定
VERSION = "1.1.5"

#window1の大きさとタイトルの設定
WINDOW1_HEIGHT =    1920                                    #高さ
WINDOW1_WIDETH =    1080                                    #横幅
WINDOW1_TITEL =     "Ditel Robot Operating System  v0.2.0"  #タイトル

#window2の大きさとタイトルの設定
WINDOW2_HEIGHT =    150
WINDOW2_WIDETH =    400
WINDOW2_TITEL =     "ポート・アドレスの設定"

#window2_1の大きさとタイトルの設定
WINDOW2_1_HEIGHT =  460
WINDOW2_1_WIDETH =  540
WINDOW2_1_TITEL =   "ポート・アドレスの設定(自動)"

#window2_2の大きさとタイトルの設定
WINDOW2_2_HEIGHT =  370
WINDOW2_2_WIDETH =  1000
WINDOW2_2_TITEL =   "ポート・アドレスの設定(手動)"

#window2_2_1の大きさとタイトルの設定
WINDOW2_2_1_HEIGHT =  380
WINDOW2_2_1_WIDETH =  680
WINDOW2_2_1_TITEL =   "ポート・アドレスの設定の確認"

#色の設定
COLOR_PORT_CONDITION_NORMAL = "green2"  #通信が正常の際のテキストボックスの色
COLOR_PORT_CONDITION_ERROR  = "red2"    #通信に異常が発生した際の色

COLOR_WINDOW =      "#1c1c1c"       #ウィンドウの背景
COLOR_LABEL_TEXT =  "white"         #ラベルのテキストの色
COLOR_LABEL_BACK =  COLOR_WINDOW    #ラベルの背景の色

COLOR_CHECKBUTTON_BACK =        COLOR_WINDOW    #チェックボタンの背景の色
COLOR_CHECKBUTTON_TEXT =        "white"         #チェックボタンのテキストの色
COLOR_CHECKBUTTON_TOUCH_BACK =  "gray30"        #チェックボタンにカーソルが触れた時の背景の色
COLOR_CHECKBUTTON_TOUCH_TEXT =  "goldenrod1"    #チェックボタンにカーソルが振れた時のテキストの色

COLOR_MENU_BAR_BACK =        "white"    #メニューバーの背景の色
COLOR_MENU_BAR_TEXT =   COLOR_WINDOW    #メニューバーのテキストの色

COLOR_SCROOLBAR_BACK =  COLOR_WINDOW    #スクロールバーの背景の色
COLOR_SCROOLBAR_BAR =   "#2c3434"       #スクロールバーのバーの色

COLOR_BUTTON_BORDER =           "#2c3434"       #ボタンの枠の色
COLOR_BUTTON_NORMAL_BACK =      "#2c3434"       #ボタンが有効の際のボタンの色
COLOR_BUTTON_NORMAL_TEXT =      "#dcdcdc"       #ボタンが有効の際のテキストの色
COLOR_BUTTON_DISABLED_BACK =    "black"         #ボタンが無効の際のボタンの色
COLOR_BUTTON_DISABLED_TEXT =    "#2c3434"       #ボタンが無効の際のテキストの色
COLOR_BUTTON_TOUCH_BACK =       "gray30"        #カーソルがボタンに触れた際のボタンの色
COLOR_BUTTON_TOUCH_TEXT =       "goldenrod1"    #カーソルがボタンに触れた際のテキストの色
COLOR_BUTTON_CLICK_BACK =       "gray13"        #ボタンがクリックされた際のボタンの色
COLOR_BUTTON_CLICK_TEXT =       "goldenrod4"    #ボタンがクリックされた際のテキストの色
#===============↑↑定数の宣言(ここまで)↑↑===============


#===============↓↓変数の宣言(ここから)↓↓===============
portAddressRelationships:str = [None] * 21  #ポートとアドレスの関係を保存するリスト
portAddressCondition:bool = [False] * 21    #各アドレスを使用するかを保存するリスト
programHasStarted:bool = False              #通信が始まっているかを示す変数
#===============↑↑変数の宣言(ここまで)↑↑===============


#==================↓↓宣言(ここから)↓↓==================
tkinter.Tk().withdraw() #tkinterの宣言

font1 = ("HG明朝B", 12) #基準の文字のフォント
font2 = ("HG明朝B", 10) #ログを表示する際に用いるフォント
#==================↑↑宣言(ここまで)↑↑==================


#==============↓↓window1関係(ここから)↓↓=============== #TODOwindow1関係
class window1_Contents:
    def __init__(self):
        GENERAL_SPACE =             "  "            #ウィジェット間の横の間隔
        RIGHT_LEFT_BETWEEN_SPACE =  "             " #右のアドレスの列と左のアドレスの列の横の間隔

        ADDRESS_LOG_LIST_BOX_HEIGHT =   3   #アドレスごとのログを表示するリストボックスの高さ
        ADDRESS_LOG_LIST_BOX_WIDTH =    23  #アドレスごとのログを表示するリストボックスの幅

        MAIN_LOG_LIST_BOX_HEIGHT =  11  #メインのログを表示するリストボックスの高さ

        self.window1_frame = tkinter.Tk()               #window1を宣言する
        self.frame = tkinter.Frame(self.window1_frame)  #window1のフレームを作成する
        self.window1_frame.withdraw()                   #window1を非表示にする
        self.style = tkinter.ttk.Style(self.frame)      #window1のスタイルを宣言する

        #Labelのスタイルの設定
        self.style.configure("TLabel",
                             foreground=COLOR_LABEL_TEXT,   #テキストの色を設定
                             background=COLOR_LABEL_BACK    #背景の色を設定
                             )

        #Scrollbarのスタイルの設定
        self.style.configure("TScrollbar",
                             gripcount=0,                       #グリップ数を設定
                             background=COLOR_SCROOLBAR_BAR,    #背景の色を設定
                             darkcolor=COLOR_SCROOLBAR_BAR,     #スクロールバーのバーの色を設定
                             lightcolor=COLOR_SCROOLBAR_BAR,
                             troughcolor=COLOR_SCROOLBAR_BACK,  #スクロールバーのレールの色の設定
                             bordercolor=COLOR_SCROOLBAR_BACK,
                             arrowcolor=COLOR_SCROOLBAR_BAR
                            )
        
        #Buttonのスタイルの設定
        self.style.configure("TButton",
                             padding=6,                             #ボタン内部の間隔を設定
                             relief="flat",                         #スタイルを設定
                             background=COLOR_BUTTON_NORMAL_BACK,   #ボタンの色を設定
                             foreground=COLOR_BUTTON_NORMAL_TEXT,   #テキストの色を設定
                             font=font1
                            )

        #Buttonのアクションごとのスタイルの設定
        self.style.map("TButton",
                       foreground=[('pressed', '!disabled', COLOR_BUTTON_CLICK_TEXT),   #ボタンが押された時のテキストの色を設定
                                   ('disabled', COLOR_BUTTON_DISABLED_TEXT),            #ボタンが無効の時のテキストの色を設定
                                   ('active', COLOR_BUTTON_TOUCH_TEXT)                  #カーソルがボタンに触れた時のテキストの色を設定
                                  ],
                       background=[('pressed', '!disabled', COLOR_BUTTON_CLICK_BACK),   #ボタンが押されたときのボタンの色を設定
                                   ('disabled', COLOR_BUTTON_DISABLED_BACK),            #ボタンが無効の時のボタンの色を設定
                                   ('active', COLOR_BUTTON_TOUCH_BACK)                  #カーソルがボンタンに触れた時のボタンの色を設定
                                  ]
                    )

        self.window1_frame.protocol('WM_DELETE_WINDOW', self.quitWindow)    #ウィンドウが閉じられた時の動作を設定

        #列の説明関係のモジュールの宣言
        self.label0_1 = tkinter.ttk.Label(self.frame, text="アドレス番号", font=font1)
        self.label0_2 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.label0_3 = tkinter.ttk.Label(self.frame, text="ポート番号         ", font=font1)
        self.label0_4 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.label0_5 = tkinter.ttk.Label(self.frame, text="アドレスのRX   " + "                  ", font=font1)
        self.label0_6 = tkinter.ttk.Label(self.frame, text="", font=font1)
        self.label0_7 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.label0_8 = tkinter.ttk.Label(self.frame, text="アドレスのTX   " + "                  ", font=font1)
        self.label0_9 = tkinter.ttk.Label(self.frame, text="", font=font1)
        self.label0_10 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.label0_11 = tkinter.ttk.Label(self.frame, text="アドレスのログ" + "                  ", font=font1)
        self.label0_12 = tkinter.ttk.Label(self.frame, text="", font=font1)

        self.label0_13 = tkinter.ttk.Label(self.frame, text=RIGHT_LEFT_BETWEEN_SPACE, font=font1)

        self.label0_14 = tkinter.ttk.Label(self.frame, text="アドレス番号", font=font1)
        self.label0_15 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.label0_16 = tkinter.ttk.Label(self.frame, text="ポート番号         ", font=font1)
        self.label0_17 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.label0_18 = tkinter.ttk.Label(self.frame, text="アドレスのRX  " + "                  ", font=font1)
        self.label0_19 = tkinter.ttk.Label(self.frame, text="", font=font1)
        self.label0_20 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.label0_21 = tkinter.ttk.Label(self.frame, text="アドレスのTX  " + "                  ", font=font1)
        self.label0_22 = tkinter.ttk.Label(self.frame, text="", font=font1)
        self.label0_23 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.label0_24 = tkinter.ttk.Label(self.frame, text="アドレスのログ" + "                  ", font=font1)
        self.label0_25 = tkinter.ttk.Label(self.frame, text="", font=font1)


        self.label1_1 = tkinter.ttk.Label(self.frame, text="アドレス   1 : ", font=font1)
        self.label1_2 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.entry1_1 = tkinter.Entry(self.frame, readonlybackground='#ff0000', fg='#ffffff', font=font1, relief="solid", bd=1, state='disabled', width=14)
        self.label1_3 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.listbox1_1 = tkinter.Listbox(self.frame, width=ADDRESS_LOG_LIST_BOX_WIDTH, height=ADDRESS_LOG_LIST_BOX_HEIGHT, relief="sunken", font=font2, state='disabled')
        self.listbox1_1_scroolbar = tkinter.ttk.Scrollbar(self.frame, orient=tkinter.VERTICAL, command=self.listbox1_1.yview)
        self.label1_4 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.listbox1_2 = tkinter.Listbox(self.frame, width=ADDRESS_LOG_LIST_BOX_WIDTH, height=ADDRESS_LOG_LIST_BOX_HEIGHT, relief="sunken", font=font2, state='disabled')
        self.listbox1_2_scroolbar = tkinter.ttk.Scrollbar(self.frame, orient=tkinter.VERTICAL, command=self.listbox1_2.yview)
        self.label1_5 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.listbox1_3 = tkinter.Listbox(self.frame, width=ADDRESS_LOG_LIST_BOX_WIDTH, height=ADDRESS_LOG_LIST_BOX_HEIGHT, relief="sunken", font=font2, state='disabled')
        self.listbox1_3_scroolbar = tkinter.ttk.Scrollbar(self.frame, orient=tkinter.VERTICAL, command=self.listbox1_3.yview)
        
        self.label1_6 = tkinter.ttk.Label(self.frame, text=RIGHT_LEFT_BETWEEN_SPACE, font=font1)
        
        self.label1_7 = tkinter.ttk.Label(self.frame, text="アドレス  11 : ", font=font1)
        self.label1_8 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.entry1_2 = tkinter.Entry(self.frame, readonlybackground='#ff0000', fg='#ffffff', font=font1, relief="solid", bd=1,state='disabled', width=14)
        self.label1_9 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.listbox1_4 = tkinter.Listbox(self.frame, width=ADDRESS_LOG_LIST_BOX_WIDTH, height=ADDRESS_LOG_LIST_BOX_HEIGHT, relief="sunken", font=font2, state='disabled')
        self.listbox1_4_scroolbar = tkinter.ttk.Scrollbar(self.frame, orient=tkinter.VERTICAL, command=self.listbox1_4.yview)
        self.label1_10 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.listbox1_5 = tkinter.Listbox(self.frame, width=ADDRESS_LOG_LIST_BOX_WIDTH, height=ADDRESS_LOG_LIST_BOX_HEIGHT, relief="sunken", font=font2, state='disabled')
        self.listbox1_5_scroolbar = tkinter.ttk.Scrollbar(self.frame, orient=tkinter.VERTICAL, command=self.listbox1_5.yview)
        self.label1_11 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.listbox1_6 = tkinter.Listbox(self.frame, width=ADDRESS_LOG_LIST_BOX_WIDTH, height=ADDRESS_LOG_LIST_BOX_HEIGHT, relief="sunken", font=font2, state='disabled')
        self.listbox1_6_scroolbar = tkinter.ttk.Scrollbar(self.frame, orient=tkinter.VERTICAL, command=self.listbox1_6.yview)
        self.label0_25 = tkinter.ttk.Label(self.frame, text="", font=font1)


        self.label2_1 = tkinter.ttk.Label(self.frame, text="アドレス   2 : ", font=font1)
        self.label2_2 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.entry2_1 = tkinter.Entry(self.frame, readonlybackground='#ff0000', fg='#ffffff', font=font1, relief="solid", bd=1,state='disabled', width=14)
        self.label2_3 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.listbox2_1 = tkinter.Listbox(self.frame, width=ADDRESS_LOG_LIST_BOX_WIDTH, height=ADDRESS_LOG_LIST_BOX_HEIGHT, relief="sunken", font=font2, state='disabled')
        self.listbox2_1_scroolbar = tkinter.ttk.Scrollbar(self.frame, orient=tkinter.VERTICAL, command=self.listbox2_1.yview)
        self.label2_4 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.listbox2_2 = tkinter.Listbox(self.frame, width=ADDRESS_LOG_LIST_BOX_WIDTH, height=ADDRESS_LOG_LIST_BOX_HEIGHT, relief="sunken", font=font2, state='disabled')
        self.listbox2_2_scroolbar = tkinter.ttk.Scrollbar(self.frame, orient=tkinter.VERTICAL, command=self.listbox2_2.yview)
        self.label2_5 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.listbox2_3 = tkinter.Listbox(self.frame, width=ADDRESS_LOG_LIST_BOX_WIDTH, height=ADDRESS_LOG_LIST_BOX_HEIGHT, relief="sunken", font=font2, state='disabled')
        self.listbox2_3_scroolbar = tkinter.ttk.Scrollbar(self.frame, orient=tkinter.VERTICAL, command=self.listbox2_3.yview)
        
        self.label2_6 = tkinter.ttk.Label(self.frame, text=RIGHT_LEFT_BETWEEN_SPACE, font=font1)
        
        self.label2_7 = tkinter.ttk.Label(self.frame, text="アドレス  12 : ", font=font1)
        self.label2_8 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.entry2_2 = tkinter.Entry(self.frame, readonlybackground='#ff0000', fg='#ffffff', font=font1, relief="solid", bd=1,state='disabled', width=14)
        self.label2_9 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.listbox2_4 = tkinter.Listbox(self.frame, width=ADDRESS_LOG_LIST_BOX_WIDTH, height=ADDRESS_LOG_LIST_BOX_HEIGHT, relief="sunken", font=font2, state='disabled')
        self.listbox2_4_scroolbar = tkinter.ttk.Scrollbar(self.frame, orient=tkinter.VERTICAL, command=self.listbox2_4.yview)
        self.label2_10 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.listbox2_5 = tkinter.Listbox(self.frame, width=ADDRESS_LOG_LIST_BOX_WIDTH, height=ADDRESS_LOG_LIST_BOX_HEIGHT, relief="sunken", font=font2, state='disabled')
        self.listbox2_5_scroolbar = tkinter.ttk.Scrollbar(self.frame, orient=tkinter.VERTICAL, command=self.listbox2_5.yview)
        self.label2_11 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.listbox2_6 = tkinter.Listbox(self.frame, width=ADDRESS_LOG_LIST_BOX_WIDTH, height=ADDRESS_LOG_LIST_BOX_HEIGHT, relief="sunken", font=font2, state='disabled')
        self.listbox2_6_scroolbar = tkinter.ttk.Scrollbar(self.frame, orient=tkinter.VERTICAL, command=self.listbox2_6.yview)
        self.label0_25 = tkinter.ttk.Label(self.frame, text="", font=font1)


        self.label3_1 = tkinter.ttk.Label(self.frame, text="アドレス   3 : ", font=font1)
        self.label3_2 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.entry3_1 = tkinter.Entry(self.frame, readonlybackground='#ff0000', fg='#ffffff', font=font1, relief="solid", bd=1,state='disabled', width=14)
        self.label3_3 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.listbox3_1 = tkinter.Listbox(self.frame, width=ADDRESS_LOG_LIST_BOX_WIDTH, height=ADDRESS_LOG_LIST_BOX_HEIGHT, relief="sunken", font=font2, state='disabled')
        self.listbox3_1_scroolbar = tkinter.ttk.Scrollbar(self.frame, orient=tkinter.VERTICAL, command=self.listbox3_1.yview)
        self.label3_4 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.listbox3_2 = tkinter.Listbox(self.frame, width=ADDRESS_LOG_LIST_BOX_WIDTH, height=ADDRESS_LOG_LIST_BOX_HEIGHT, relief="sunken", font=font2, state='disabled')
        self.listbox3_2_scroolbar = tkinter.ttk.Scrollbar(self.frame, orient=tkinter.VERTICAL, command=self.listbox3_2.yview)
        self.label3_5 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.listbox3_3 = tkinter.Listbox(self.frame, width=ADDRESS_LOG_LIST_BOX_WIDTH, height=ADDRESS_LOG_LIST_BOX_HEIGHT, relief="sunken", font=font2, state='disabled')
        self.listbox3_3_scroolbar = tkinter.ttk.Scrollbar(self.frame, orient=tkinter.VERTICAL, command=self.listbox3_3.yview)
        
        self.label3_6 = tkinter.ttk.Label(self.frame, text=RIGHT_LEFT_BETWEEN_SPACE, font=font1)
        
        self.label3_7 = tkinter.ttk.Label(self.frame, text="アドレス  13 : ", font=font1)
        self.label3_8 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.entry3_2 = tkinter.Entry(self.frame, readonlybackground='#ff0000', fg='#ffffff', font=font1, relief="solid", bd=1,state='disabled', width=14)
        self.label3_9 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.listbox3_4 = tkinter.Listbox(self.frame, width=ADDRESS_LOG_LIST_BOX_WIDTH, height=ADDRESS_LOG_LIST_BOX_HEIGHT, relief="sunken", font=font2, state='disabled')
        self.listbox3_4_scroolbar = tkinter.ttk.Scrollbar(self.frame, orient=tkinter.VERTICAL, command=self.listbox3_4.yview)
        self.label3_10 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.listbox3_5 = tkinter.Listbox(self.frame, width=ADDRESS_LOG_LIST_BOX_WIDTH, height=ADDRESS_LOG_LIST_BOX_HEIGHT, relief="sunken", font=font2, state='disabled')
        self.listbox3_5_scroolbar = tkinter.ttk.Scrollbar(self.frame, orient=tkinter.VERTICAL, command=self.listbox3_5.yview)
        self.label3_11 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.listbox3_6 = tkinter.Listbox(self.frame, width=ADDRESS_LOG_LIST_BOX_WIDTH, height=ADDRESS_LOG_LIST_BOX_HEIGHT, relief="sunken", font=font2, state='disabled')
        self.listbox3_6_scroolbar = tkinter.ttk.Scrollbar(self.frame, orient=tkinter.VERTICAL, command=self.listbox3_6.yview)
        self.label0_25 = tkinter.ttk.Label(self.frame, text="", font=font1)


        self.label4_1 = tkinter.ttk.Label(self.frame, text="アドレス   4 : ", font=font1)
        self.label4_2 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.entry4_1 = tkinter.Entry(self.frame, readonlybackground='#ff0000', fg='#ffffff', font=font1, relief="solid", bd=1,state='disabled', width=14)
        self.label4_3 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.listbox4_1 = tkinter.Listbox(self.frame, width=ADDRESS_LOG_LIST_BOX_WIDTH, height=ADDRESS_LOG_LIST_BOX_HEIGHT, relief="sunken", font=font2, state='disabled')
        self.listbox4_1_scroolbar = tkinter.ttk.Scrollbar(self.frame, orient=tkinter.VERTICAL, command=self.listbox4_1.yview)
        self.label4_4 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.listbox4_2 = tkinter.Listbox(self.frame, width=ADDRESS_LOG_LIST_BOX_WIDTH, height=ADDRESS_LOG_LIST_BOX_HEIGHT, relief="sunken", font=font2, state='disabled')
        self.listbox4_2_scroolbar = tkinter.ttk.Scrollbar(self.frame, orient=tkinter.VERTICAL, command=self.listbox4_2.yview)
        self.label4_5 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.listbox4_3 = tkinter.Listbox(self.frame, width=ADDRESS_LOG_LIST_BOX_WIDTH, height=ADDRESS_LOG_LIST_BOX_HEIGHT, relief="sunken", font=font2, state='disabled')
        self.listbox4_3_scroolbar = tkinter.ttk.Scrollbar(self.frame, orient=tkinter.VERTICAL, command=self.listbox4_3.yview)
        
        self.label4_6 = tkinter.ttk.Label(self.frame, text=RIGHT_LEFT_BETWEEN_SPACE, font=font1)
        
        self.label4_7 = tkinter.ttk.Label(self.frame, text="アドレス  14 : ", font=font1)
        self.label4_8 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.entry4_2 = tkinter.Entry(self.frame, readonlybackground='#ff0000', fg='#ffffff', font=font1, relief="solid", bd=1,state='disabled', width=14)
        self.label4_9 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.listbox4_4 = tkinter.Listbox(self.frame, width=ADDRESS_LOG_LIST_BOX_WIDTH, height=ADDRESS_LOG_LIST_BOX_HEIGHT, relief="sunken", font=font2, state='disabled')
        self.listbox4_4_scroolbar = tkinter.ttk.Scrollbar(self.frame, orient=tkinter.VERTICAL, command=self.listbox4_4.yview)
        self.label4_10 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.listbox4_5 = tkinter.Listbox(self.frame, width=ADDRESS_LOG_LIST_BOX_WIDTH, height=ADDRESS_LOG_LIST_BOX_HEIGHT, relief="sunken", font=font2, state='disabled')
        self.listbox4_5_scroolbar = tkinter.ttk.Scrollbar(self.frame, orient=tkinter.VERTICAL, command=self.listbox4_5.yview)
        self.label4_11 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.listbox4_6 = tkinter.Listbox(self.frame, width=ADDRESS_LOG_LIST_BOX_WIDTH, height=ADDRESS_LOG_LIST_BOX_HEIGHT, relief="sunken", font=font2, state='disabled')
        self.listbox4_6_scroolbar = tkinter.ttk.Scrollbar(self.frame, orient=tkinter.VERTICAL, command=self.listbox4_6.yview)
        self.label0_25 = tkinter.ttk.Label(self.frame, text="", font=font1)


        self.label5_1 = tkinter.ttk.Label(self.frame, text="アドレス   5 : ", font=font1)
        self.label5_2 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.entry5_1 = tkinter.Entry(self.frame, readonlybackground='#ff0000', fg='#ffffff', font=font1, relief="solid", bd=1,state='disabled', width=14)
        self.label5_3 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.listbox5_1 = tkinter.Listbox(self.frame, width=ADDRESS_LOG_LIST_BOX_WIDTH, height=ADDRESS_LOG_LIST_BOX_HEIGHT, relief="sunken", font=font2, state='disabled')
        self.listbox5_1_scroolbar = tkinter.ttk.Scrollbar(self.frame, orient=tkinter.VERTICAL, command=self.listbox5_1.yview)
        self.label5_4 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.listbox5_2 = tkinter.Listbox(self.frame, width=ADDRESS_LOG_LIST_BOX_WIDTH, height=ADDRESS_LOG_LIST_BOX_HEIGHT, relief="sunken", font=font2, state='disabled')
        self.listbox5_2_scroolbar = tkinter.ttk.Scrollbar(self.frame, orient=tkinter.VERTICAL, command=self.listbox5_2.yview)
        self.label5_5 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.listbox5_3 = tkinter.Listbox(self.frame, width=ADDRESS_LOG_LIST_BOX_WIDTH, height=ADDRESS_LOG_LIST_BOX_HEIGHT, relief="sunken", font=font2, state='disabled')
        self.listbox5_3_scroolbar = tkinter.ttk.Scrollbar(self.frame, orient=tkinter.VERTICAL, command=self.listbox5_3.yview)
        
        self.label5_6 = tkinter.ttk.Label(self.frame, text=RIGHT_LEFT_BETWEEN_SPACE, font=font1)
        
        self.label5_7 = tkinter.ttk.Label(self.frame, text="アドレス  15 : ", font=font1)
        self.label5_8 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.entry5_2 = tkinter.Entry(self.frame, readonlybackground='#ff0000', fg='#ffffff', font=font1, relief="solid", bd=1,state='disabled', width=14)
        self.label5_9 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.listbox5_4 = tkinter.Listbox(self.frame, width=ADDRESS_LOG_LIST_BOX_WIDTH, height=ADDRESS_LOG_LIST_BOX_HEIGHT, relief="sunken", font=font2, state='disabled')
        self.listbox5_4_scroolbar = tkinter.ttk.Scrollbar(self.frame, orient=tkinter.VERTICAL, command=self.listbox5_4.yview)
        self.label5_10 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.listbox5_5 = tkinter.Listbox(self.frame, width=ADDRESS_LOG_LIST_BOX_WIDTH, height=ADDRESS_LOG_LIST_BOX_HEIGHT, relief="sunken", font=font2, state='disabled')
        self.listbox5_5_scroolbar = tkinter.ttk.Scrollbar(self.frame, orient=tkinter.VERTICAL, command=self.listbox5_5.yview)
        self.label5_11 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.listbox5_6 = tkinter.Listbox(self.frame, width=ADDRESS_LOG_LIST_BOX_WIDTH, height=ADDRESS_LOG_LIST_BOX_HEIGHT, relief="sunken", font=font2, state='disabled')
        self.listbox5_6_scroolbar = tkinter.ttk.Scrollbar(self.frame, orient=tkinter.VERTICAL, command=self.listbox5_6.yview)
        self.label0_25 = tkinter.ttk.Label(self.frame, text="", font=font1)


        self.label6_1 = tkinter.ttk.Label(self.frame, text="アドレス   6 : ", font=font1)
        self.label6_2 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.entry6_1 = tkinter.Entry(self.frame, readonlybackground='#ff0000', fg='#ffffff', font=font1, relief="solid", bd=1,state='disabled', width=14)
        self.label6_3 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.listbox6_1 = tkinter.Listbox(self.frame, width=ADDRESS_LOG_LIST_BOX_WIDTH, height=ADDRESS_LOG_LIST_BOX_HEIGHT, relief="sunken", font=font2, state='disabled')
        self.listbox6_1_scroolbar = tkinter.ttk.Scrollbar(self.frame, orient=tkinter.VERTICAL, command=self.listbox6_1.yview)
        self.label6_4 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.listbox6_2 = tkinter.Listbox(self.frame, width=ADDRESS_LOG_LIST_BOX_WIDTH, height=ADDRESS_LOG_LIST_BOX_HEIGHT, relief="sunken", font=font2, state='disabled')
        self.listbox6_2_scroolbar = tkinter.ttk.Scrollbar(self.frame, orient=tkinter.VERTICAL, command=self.listbox6_2.yview)
        self.label6_5 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.listbox6_3 = tkinter.Listbox(self.frame, width=ADDRESS_LOG_LIST_BOX_WIDTH, height=ADDRESS_LOG_LIST_BOX_HEIGHT, relief="sunken", font=font2, state='disabled')
        self.listbox6_3_scroolbar = tkinter.ttk.Scrollbar(self.frame, orient=tkinter.VERTICAL, command=self.listbox6_3.yview)
        
        self.label6_6 = tkinter.ttk.Label(self.frame, text=RIGHT_LEFT_BETWEEN_SPACE, font=font1)
        
        self.label6_7 = tkinter.ttk.Label(self.frame, text="アドレス  16 : ", font=font1)
        self.label6_8 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.entry6_2 = tkinter.Entry(self.frame, readonlybackground='#ff0000', fg='#ffffff', font=font1, relief="solid", bd=1,state='disabled', width=14)
        self.label6_9 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.listbox6_4 = tkinter.Listbox(self.frame, width=ADDRESS_LOG_LIST_BOX_WIDTH, height=ADDRESS_LOG_LIST_BOX_HEIGHT, relief="sunken", font=font2, state='disabled')
        self.listbox6_4_scroolbar = tkinter.ttk.Scrollbar(self.frame, orient=tkinter.VERTICAL, command=self.listbox6_4.yview)
        self.label6_10 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.listbox6_5 = tkinter.Listbox(self.frame, width=ADDRESS_LOG_LIST_BOX_WIDTH, height=ADDRESS_LOG_LIST_BOX_HEIGHT, relief="sunken", font=font2, state='disabled')
        self.listbox6_5_scroolbar = tkinter.ttk.Scrollbar(self.frame, orient=tkinter.VERTICAL, command=self.listbox6_5.yview)
        self.label6_11 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.listbox6_6 = tkinter.Listbox(self.frame, width=ADDRESS_LOG_LIST_BOX_WIDTH, height=ADDRESS_LOG_LIST_BOX_HEIGHT, relief="sunken", font=font2, state='disabled')
        self.listbox6_6_scroolbar = tkinter.ttk.Scrollbar(self.frame, orient=tkinter.VERTICAL, command=self.listbox6_6.yview)
        self.label0_25 = tkinter.ttk.Label(self.frame, text="", font=font1)


        self.label7_1 = tkinter.ttk.Label(self.frame, text="アドレス   7 : ", font=font1)
        self.label7_2 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.entry7_1 = tkinter.Entry(self.frame, readonlybackground='#ff0000', fg='#ffffff', font=font1, relief="solid", bd=1,state='disabled', width=14)
        self.label7_3 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.listbox7_1 = tkinter.Listbox(self.frame, width=ADDRESS_LOG_LIST_BOX_WIDTH, height=ADDRESS_LOG_LIST_BOX_HEIGHT, relief="sunken", font=font2, state='disabled')
        self.listbox7_1_scroolbar = tkinter.ttk.Scrollbar(self.frame, orient=tkinter.VERTICAL, command=self.listbox7_1.yview)
        self.label7_4 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.listbox7_2 = tkinter.Listbox(self.frame, width=ADDRESS_LOG_LIST_BOX_WIDTH, height=ADDRESS_LOG_LIST_BOX_HEIGHT, relief="sunken", font=font2, state='disabled')
        self.listbox7_2_scroolbar = tkinter.ttk.Scrollbar(self.frame, orient=tkinter.VERTICAL, command=self.listbox7_2.yview)
        self.label7_5 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.listbox7_3 = tkinter.Listbox(self.frame, width=ADDRESS_LOG_LIST_BOX_WIDTH, height=ADDRESS_LOG_LIST_BOX_HEIGHT, relief="sunken", font=font2, state='disabled')
        self.listbox7_3_scroolbar = tkinter.ttk.Scrollbar(self.frame, orient=tkinter.VERTICAL, command=self.listbox7_3.yview)
        
        self.label7_6 = tkinter.ttk.Label(self.frame, text=RIGHT_LEFT_BETWEEN_SPACE, font=font1)
        
        self.label7_7 = tkinter.ttk.Label(self.frame, text="アドレス  17 : ", font=font1)
        self.label7_8 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.entry7_2 = tkinter.Entry(self.frame, readonlybackground='#ff0000', fg='#ffffff', font=font1, relief="solid", bd=1,state='disabled', width=14)
        self.label7_9 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.listbox7_4 = tkinter.Listbox(self.frame, width=ADDRESS_LOG_LIST_BOX_WIDTH, height=ADDRESS_LOG_LIST_BOX_HEIGHT, relief="sunken", font=font2, state='disabled')
        self.listbox7_4_scroolbar = tkinter.ttk.Scrollbar(self.frame, orient=tkinter.VERTICAL, command=self.listbox7_4.yview)
        self.label7_10 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.listbox7_5 = tkinter.Listbox(self.frame, width=ADDRESS_LOG_LIST_BOX_WIDTH, height=ADDRESS_LOG_LIST_BOX_HEIGHT, relief="sunken", font=font2, state='disabled')
        self.listbox7_5_scroolbar = tkinter.ttk.Scrollbar(self.frame, orient=tkinter.VERTICAL, command=self.listbox7_5.yview)
        self.label7_11 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.listbox7_6 = tkinter.Listbox(self.frame, width=ADDRESS_LOG_LIST_BOX_WIDTH, height=ADDRESS_LOG_LIST_BOX_HEIGHT, relief="sunken", font=font2, state='disabled')
        self.listbox7_6_scroolbar = tkinter.ttk.Scrollbar(self.frame, orient=tkinter.VERTICAL, command=self.listbox7_6.yview)
        self.label0_25 = tkinter.ttk.Label(self.frame, text="", font=font1)


        self.label8_1 = tkinter.ttk.Label(self.frame, text="アドレス   8 : ", font=font1)
        self.label8_2 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.entry8_1 = tkinter.Entry(self.frame, readonlybackground='#ff0000', fg='#ffffff', font=font1, relief="solid", bd=1,state='disabled', width=14)
        self.label8_3 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.listbox8_1 = tkinter.Listbox(self.frame, width=ADDRESS_LOG_LIST_BOX_WIDTH, height=ADDRESS_LOG_LIST_BOX_HEIGHT, relief="sunken", font=font2, state='disabled')
        self.listbox8_1_scroolbar = tkinter.ttk.Scrollbar(self.frame, orient=tkinter.VERTICAL, command=self.listbox8_1.yview)
        self.label8_4 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.listbox8_2 = tkinter.Listbox(self.frame, width=ADDRESS_LOG_LIST_BOX_WIDTH, height=ADDRESS_LOG_LIST_BOX_HEIGHT, relief="sunken", font=font2, state='disabled')
        self.listbox8_2_scroolbar = tkinter.ttk.Scrollbar(self.frame, orient=tkinter.VERTICAL, command=self.listbox8_2.yview)
        self.label8_5 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.listbox8_3 = tkinter.Listbox(self.frame, width=ADDRESS_LOG_LIST_BOX_WIDTH, height=ADDRESS_LOG_LIST_BOX_HEIGHT, relief="sunken", font=font2, state='disabled')
        self.listbox8_3_scroolbar = tkinter.ttk.Scrollbar(self.frame, orient=tkinter.VERTICAL, command=self.listbox8_3.yview)
        
        self.label8_6 = tkinter.ttk.Label(self.frame, text=RIGHT_LEFT_BETWEEN_SPACE, font=font1)
        
        self.label8_7 = tkinter.ttk.Label(self.frame, text="アドレス  18 : ", font=font1)
        self.label8_8 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.entry8_2 = tkinter.Entry(self.frame, readonlybackground='#ff0000', fg='#ffffff', font=font1, relief="solid", bd=1,state='disabled', width=14)
        self.label8_9 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.listbox8_4 = tkinter.Listbox(self.frame, width=ADDRESS_LOG_LIST_BOX_WIDTH, height=ADDRESS_LOG_LIST_BOX_HEIGHT, relief="sunken", font=font2, state='disabled')
        self.listbox8_4_scroolbar = tkinter.ttk.Scrollbar(self.frame, orient=tkinter.VERTICAL, command=self.listbox8_4.yview)
        self.label8_10 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.listbox8_5 = tkinter.Listbox(self.frame, width=ADDRESS_LOG_LIST_BOX_WIDTH, height=ADDRESS_LOG_LIST_BOX_HEIGHT, relief="sunken", font=font2, state='disabled')
        self.listbox8_5_scroolbar = tkinter.ttk.Scrollbar(self.frame, orient=tkinter.VERTICAL, command=self.listbox8_5.yview)
        self.label8_11 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.listbox8_6 = tkinter.Listbox(self.frame, width=ADDRESS_LOG_LIST_BOX_WIDTH, height=ADDRESS_LOG_LIST_BOX_HEIGHT, relief="sunken", font=font2, state='disabled')
        self.listbox8_6_scroolbar = tkinter.ttk.Scrollbar(self.frame, orient=tkinter.VERTICAL, command=self.listbox8_6.yview)
        self.label0_25 = tkinter.ttk.Label(self.frame, text="", font=font1)


        self.label9_1 = tkinter.ttk.Label(self.frame, text="アドレス   9 : ", font=font1)
        self.label9_2 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.entry9_1 = tkinter.Entry(self.frame, readonlybackground='#ff0000', fg='#ffffff', font=font1, relief="solid", bd=1,state='disabled', width=14)
        self.label9_3 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.listbox9_1 = tkinter.Listbox(self.frame, width=ADDRESS_LOG_LIST_BOX_WIDTH, height=ADDRESS_LOG_LIST_BOX_HEIGHT, relief="sunken", font=font2, state='disabled')
        self.listbox9_1_scroolbar = tkinter.ttk.Scrollbar(self.frame, orient=tkinter.VERTICAL, command=self.listbox9_1.yview)
        self.label9_4 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.listbox9_2 = tkinter.Listbox(self.frame, width=ADDRESS_LOG_LIST_BOX_WIDTH, height=ADDRESS_LOG_LIST_BOX_HEIGHT, relief="sunken", font=font2, state='disabled')
        self.listbox9_2_scroolbar = tkinter.ttk.Scrollbar(self.frame, orient=tkinter.VERTICAL, command=self.listbox9_2.yview)
        self.label9_5 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.listbox9_3 = tkinter.Listbox(self.frame, width=ADDRESS_LOG_LIST_BOX_WIDTH, height=ADDRESS_LOG_LIST_BOX_HEIGHT, relief="sunken", font=font2, state='disabled')
        self.listbox9_3_scroolbar = tkinter.ttk.Scrollbar(self.frame, orient=tkinter.VERTICAL, command=self.listbox9_3.yview)
        
        self.label9_6 = tkinter.ttk.Label(self.frame, text=RIGHT_LEFT_BETWEEN_SPACE, font=font1)
        
        self.label9_7 = tkinter.ttk.Label(self.frame, text="アドレス  19 : ", font=font1)
        self.label9_8 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.entry9_2 = tkinter.Entry(self.frame, readonlybackground='#ff0000', fg='#ffffff', font=font1, relief="solid", bd=1,state='disabled', width=14)
        self.label9_9 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.listbox9_4 = tkinter.Listbox(self.frame, width=ADDRESS_LOG_LIST_BOX_WIDTH, height=ADDRESS_LOG_LIST_BOX_HEIGHT, relief="sunken", font=font2, state='disabled')
        self.listbox9_4_scroolbar = tkinter.ttk.Scrollbar(self.frame, orient=tkinter.VERTICAL, command=self.listbox9_4.yview)
        self.label9_10 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.listbox9_5 = tkinter.Listbox(self.frame, width=ADDRESS_LOG_LIST_BOX_WIDTH, height=ADDRESS_LOG_LIST_BOX_HEIGHT, relief="sunken", font=font2, state='disabled')
        self.listbox9_5_scroolbar = tkinter.ttk.Scrollbar(self.frame, orient=tkinter.VERTICAL, command=self.listbox9_5.yview)
        self.label9_11 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.listbox9_6 = tkinter.Listbox(self.frame, width=ADDRESS_LOG_LIST_BOX_WIDTH, height=ADDRESS_LOG_LIST_BOX_HEIGHT, relief="sunken", font=font2, state='disabled')
        self.listbox9_6_scroolbar = tkinter.ttk.Scrollbar(self.frame, orient=tkinter.VERTICAL, command=self.listbox9_6.yview)
        self.label0_25 = tkinter.ttk.Label(self.frame, text="", font=font1)


        self.label10_1 = tkinter.ttk.Label(self.frame, text="アドレス  10 : ", font=font1)
        self.label10_2 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.entry10_1 = tkinter.Entry(self.frame, readonlybackground='#ff0000', fg='#ffffff', font=font1, relief="solid", bd=1,state='disabled', width=14)
        self.label10_3 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.listbox10_1 = tkinter.Listbox(self.frame, width=ADDRESS_LOG_LIST_BOX_WIDTH, height=ADDRESS_LOG_LIST_BOX_HEIGHT, relief="sunken", font=font2, state='disabled')
        self.listbox10_1_scroolbar = tkinter.ttk.Scrollbar(self.frame, orient=tkinter.VERTICAL, command=self.listbox10_1.yview)
        self.label10_4 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.listbox10_2 = tkinter.Listbox(self.frame, width=ADDRESS_LOG_LIST_BOX_WIDTH, height=ADDRESS_LOG_LIST_BOX_HEIGHT, relief="sunken", font=font2, state='disabled')
        self.listbox10_2_scroolbar = tkinter.ttk.Scrollbar(self.frame, orient=tkinter.VERTICAL, command=self.listbox10_2.yview)
        self.label10_5 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.listbox10_3 = tkinter.Listbox(self.frame, width=ADDRESS_LOG_LIST_BOX_WIDTH, height=ADDRESS_LOG_LIST_BOX_HEIGHT, relief="sunken", font=font2, state='disabled')
        self.listbox10_3_scroolbar = tkinter.ttk.Scrollbar(self.frame, orient=tkinter.VERTICAL, command=self.listbox10_3.yview)
        
        self.label10_6 = tkinter.ttk.Label(self.frame, text=RIGHT_LEFT_BETWEEN_SPACE, font=font1)
        
        self.label10_7 = tkinter.ttk.Label(self.frame, text="アドレス  20 : ", font=font1)
        self.label10_8 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.entry10_2 = tkinter.Entry(self.frame, readonlybackground='#ff0000', fg='#ffffff', font=font1, relief="solid", bd=1,state='disabled', width=14)
        self.label10_9 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.listbox10_4 = tkinter.Listbox(self.frame, width=ADDRESS_LOG_LIST_BOX_WIDTH, height=ADDRESS_LOG_LIST_BOX_HEIGHT, relief="sunken", font=font2, state='disabled')
        self.listbox10_4_scroolbar = tkinter.ttk.Scrollbar(self.frame, orient=tkinter.VERTICAL, command=self.listbox10_4.yview)
        self.label10_10 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.listbox10_5 = tkinter.Listbox(self.frame, width=ADDRESS_LOG_LIST_BOX_WIDTH, height=ADDRESS_LOG_LIST_BOX_HEIGHT, relief="sunken", font=font2, state='disabled')
        self.listbox10_5_scroolbar = tkinter.ttk.Scrollbar(self.frame, orient=tkinter.VERTICAL, command=self.listbox10_5.yview)
        self.label10_11 = tkinter.ttk.Label(self.frame, text=GENERAL_SPACE, font=font1)
        self.listbox10_6 = tkinter.Listbox(self.frame, width=ADDRESS_LOG_LIST_BOX_WIDTH, height=ADDRESS_LOG_LIST_BOX_HEIGHT, relief="sunken", font=font2, state='disabled')
        self.listbox10_6_scroolbar = tkinter.ttk.Scrollbar(self.frame, orient=tkinter.VERTICAL, command=self.listbox10_6.yview)

        self.labelA_1 = tkinter.ttk.Label(self.frame, text="全体のログ     ", font=font1)
        self.listboxA_1 = tkinter.Listbox(self.frame, height=MAIN_LOG_LIST_BOX_HEIGHT, font=font2, state='disabled')
        self.listboxA_1_scroolbar = tkinter.ttk.Scrollbar(self.frame, orient=tkinter.VERTICAL, command=self.listboxA_1.yview)

        self.labelA_2 = tkinter.ttk.Label(self.frame, text="操作ボタン     ", font=font1)
        self.buttonA_1 = tkinter.ttk.Button(self.frame, text="ポート設定", command=self.portAddressSetting, width=15, state='nlogPrint(0ormal')
        self.buttonA_2 = tkinter.ttk.Button(self.frame, text="ポート設定の確認", command=self.portAddressSettingCheck, width=15, state='disable')
        self.buttonA_3 = tkinter.ttk.Button(self.frame, text="通信開始", command=self.communicationStart, width=15, state='disable')
        self.buttonA_4 = tkinter.ttk.Button(self.frame, text="通信終了", command=self.stopCommunication, width=15, state='disable')
        self.buttonA_5 = tkinter.ttk.Button(self.frame, text="終了", command=lambda:exit(), width=15, state='normal')

        self.threadForLog = threading.Thread(target=self.logPrintProgram)
    
    def logPrint(self, _address:int, _condition:bool, _logInfo:str):
        if (_condition):
            _conditionForPrint = "[  OK  ] "
            _entryColor = COLOR_PORT_CONDITION_NORMAL
        else:
            _conditionForPrint = "[FAILED] "
            _entryColor = COLOR_PORT_CONDITION_ERROR

        match _address:
            case 1 :
                self.listbox1_3.insert(tkinter.END, _conditionForPrint + _logInfo)
                self.listbox1_3.see("end")
                self.entry1_1['readonlybackground'] = _entryColor
            case 2 :
                self.listbox2_3.insert(tkinter.END, _conditionForPrint + _logInfo)
                self.listbox2_3.see("end")
                self.entry2_1['readonlybackground'] = _entryColor
            case 3 :
                self.listbox3_3.insert(tkinter.END, _conditionForPrint + _logInfo)
                self.listbox3_3.see("end")
                self.entry3_1['readonlybackground'] = _entryColor
            case 4 :
                self.listbox4_3.insert(tkinter.END, _conditionForPrint + _logInfo)
                self.listbox4_3.see("end")
                self.entry4_1['readonlybackground'] = _entryColor
            case 5 :
                self.listbox5_3.insert(tkinter.END, _conditionForPrint + _logInfo)
                self.listbox5_3.see("end")
                self.entry5_1['readonlybackground'] = _entryColor
            case 6 :
                self.listbox6_3.insert(tkinter.END, _conditionForPrint + _logInfo)
                self.listbox6_3.see("end")
                self.entry6_1['readonlybackground'] = _entryColor
            case 7 :
                self.listbox7_3.insert(tkinter.END, _conditionForPrint + _logInfo)
                self.listbox7_3.see("end")
                self.entry7_1['readonlybackground'] = _entryColor
            case 8 :
                self.listbox8_3.insert(tkinter.END, _conditionForPrint + _logInfo)
                self.listbox8_3.see("end")
                self.entry8_1['readonlybackground'] = _entryColor
            case 9 :
                self.listbox9_3.insert(tkinter.END, _conditionForPrint + _logInfo)
                self.listbox9_3.see("end")
                self.entry9_1['readonlybackground'] = _entryColor
            case 10 :
                self.listbox10_3.insert(tkinter.END, _conditionForPrint + _logInfo)
                self.listbox10_3.see("end")
                self.entry10_1['readonlybackground'] = _entryColor
            case 11 :
                self.listbox1_6.insert(tkinter.END, _conditionForPrint + _logInfo)
                self.listbox1_6.see("end")
                self.entry1_2['readonlybackground'] = _entryColor
            case 12 :
                self.listbox2_6.insert(tkinter.END, _conditionForPrint + _logInfo)
                self.listbox2_6.see("end")
                self.entry2_2['readonlybackground'] = _entryColor
            case 13 :
                self.listbox3_6.insert(tkinter.END, _conditionForPrint + _logInfo)
                self.listbox3_6.see("end")
                self.entry3_2['readonlybackground'] = _entryColor
            case 14 :
                self.listbox4_6.insert(tkinter.END, _conditionForPrint + _logInfo)
                self.listbox4_6.see("end")
                self.entry4_2['readonlybackground'] = _entryColor
            case 15 :
                self.listbox5_6.insert(tkinter.END, _conditionForPrint + _logInfo)
                self.listbox5_6.see("end")
                self.entry5_2['readonlybackground'] = _entryColor
            case 16 :
                self.listbox6_6.insert(tkinter.END, _conditionForPrint + _logInfo)
                self.listbox6_6.see("end")
                self.entry6_2['readonlybackground'] = _entryColor
            case 17 :
                self.listbox7_6.insert(tkinter.END, _conditionForPrint + _logInfo)
                self.listbox7_6.see("end")
                self.entry7_2['readonlybackground'] = _entryColor
            case 18 :
                self.listbox8_6.insert(tkinter.END, _conditionForPrint + _logInfo)
                self.listbox8_6.see("end")
                self.entry8_2['readonlybackground'] = _entryColor
            case 19 :
                self.listbox9_6.insert(tkinter.END, _conditionForPrint + _logInfo)
                self.listbox9_6.see("end")
                self.entry9_2['readonlybackground'] = _entryColor
            case 20 :
                self.listbox10_6.insert(tkinter.END, _conditionForPrint + _logInfo)
                self.listbox10_6.see("end")
                self.entry10_2['readonlybackground'] = _entryColor
            case _ :
                self.listboxA_1.insert(tkinter.END, _conditionForPrint + _logInfo)
                self.listboxA_1.see("end")

    def txLogPrint(self, _address:int, _logInfo:str):
        match _address:
            case 1 :
                self.listbox1_2.insert(tkinter.END, _logInfo)
                self.listbox1_2.see("end")
            case 2 :
                self.listbox2_2.insert(tkinter.END, _logInfo)
                self.listbox2_2.see("end")
            case 3 :
                self.listbox3_2.insert(tkinter.END, _logInfo)
                self.listbox3_2.see("end")
            case 4 :
                self.listbox4_2.insert(tkinter.END, _logInfo)
                self.listbox4_2.see("end")
            case 5 :
                self.listbox5_2.insert(tkinter.END, _logInfo)
                self.listbox5_2.see("end")
            case 6 :
                self.listbox6_2.insert(tkinter.END, _logInfo)
                self.listbox6_2.see("end")
            case 7 :
                self.listbox7_2.insert(tkinter.END, _logInfo)
                self.listbox7_2.see("end")
            case 8 :
                self.listbox8_2.insert(tkinter.END, _logInfo)
                self.listbox8_2.see("end")
            case 9 :
                self.listbox9_2.insert(tkinter.END, _logInfo)
                self.listbox9_2.see("end")
            case 10 :
                self.listbox10_2.insert(tkinter.END, _logInfo)
                self.listbox10_2.see("end")
            case 11 :
                self.listbox1_5.insert(tkinter.END, _logInfo)
                self.listbox1_5.see("end")
            case 12 :
                self.listbox2_5.insert(tkinter.END, _logInfo)
                self.listbox2_5.see("end")
            case 13 :
                self.listbox3_5.insert(tkinter.END, _logInfo)
                self.listbox3_5.see("end")
            case 14 :
                self.listbox4_5.insert(tkinter.END, _logInfo)
                self.listbox4_5.see("end")
            case 15 :
                self.listbox5_5.insert(tkinter.END, _logInfo)
                self.listbox5_5.see("end")
            case 16 :
                self.listbox6_5.insert(tkinter.END, _logInfo)
                self.listbox6_5.see("end")
            case 17 :
                self.listbox7_5.insert(tkinter.END, _logInfo)
                self.listbox7_5.see("end")
            case 18 :
                self.listbox8_5.insert(tkinter.END, _logInfo)
                self.listbox8_5.see("end")
            case 19 :
                self.listbox9_5.insert(tkinter.END, _logInfo)
                self.listbox1_5.see("end")
            case 20 :
                self.listbox10_5.insert(tkinter.END, _logInfo)
                self.listbox1_5.see("end")

    def rxLogPrint(self, _address:int, _logInfo:str):
        match _address:
            case 1 :
                self.listbox1_1.insert(tkinter.END, _logInfo)
                self.listbox1_1.see("end")
            case 2 :
                self.listbox2_1.insert(tkinter.END, _logInfo)
                self.listbox2_1.see("end")
            case 3 :
                self.listbox3_1.insert(tkinter.END, _logInfo)
                self.listbox3_1.see("end")
            case 4 :
                self.listbox4_1.insert(tkinter.END, _logInfo)
                self.listbox4_1.see("end")
            case 5 :
                self.listbox5_1.insert(tkinter.END, _logInfo)
                self.listbox5_1.see("end")
            case 6 :
                self.listbox6_1.insert(tkinter.END, _logInfo)
                self.listbox6_1.see("end")
            case 7 :
                self.listbox7_1.insert(tkinter.END, _logInfo)
                self.listbox7_1.see("end")
            case 8 :
                self.listbox8_1.insert(tkinter.END, _logInfo)
                self.listbox8_1.see("end")
            case 9 :
                self.listbox9_1.insert(tkinter.END, _logInfo)
                self.listbox9_1.see("end")
            case 10 :
                self.listbox10_1.insert(tkinter.END, _logInfo)
                self.listbox10_1.see("end")
            case 11 :
                self.listbox1_4.insert(tkinter.END, _logInfo)
                self.listbox1_4.see("end")
            case 12 :
                self.listbox2_4.insert(tkinter.END, _logInfo)
                self.listbox2_4.see("end")
            case 13 :
                self.listbox3_4.insert(tkinter.END, _logInfo)
                self.listbox3_4.see("end")
            case 14 :
                self.listbox4_4.insert(tkinter.END, _logInfo)
                self.listbox4_4.see("end")
            case 15 :
                self.listbox5_4.insert(tkinter.END, _logInfo)
                self.listbox5_4.see("end")
            case 16 :
                self.listbox6_4.insert(tkinter.END, _logInfo)
                self.listbox6_4.see("end")
            case 17 :
                self.listbox7_4.insert(tkinter.END, _logInfo)
                self.listbox7_4.see("end")
            case 18 :
                self.listbox8_4.insert(tkinter.END, _logInfo)
                self.listbox8_4.see("end")
            case 19 :
                self.listbox9_4.insert(tkinter.END, _logInfo)
                self.listbox9_4.see("end")
            case 20 :
                self.listbox10_4.insert(tkinter.END, _logInfo)
                self.listbox10_4.see("end")

    def portAddressSetting(self):
        portAddressSettingWindow.startWindow()
    
    def portAddressSettingCheck(self):
        portAddressSettingCheckWindow.startWindow()

    def communicationStart(self):
        result = tkinter.messagebox.askquestion(title="通信の開始", message="本当に通信を開始しますか?")
        if(result == "yes"):
            global programHasStarted
            programHasStarted = True
            self.logPrint(0, True, "read number of thread : thread count = " + str(threading.active_count()))

            programsys.startUserProgram()
            self.threadForLog.start()
            serialsys.startSerial()

            try:
                bypasssys._bypassStart()
                self.logPrint(0, True, "start bypass thread")
            except:
                self.logPrint(0, False, "start bypass thread")

            try:
                emergencysys._startStateRead()
                self.logPrint(0, True, "start state read thread")
            except:
                self.logPrint(0, False, "start state read thread")

            self.buttonA_1['state'] = "disable"
            self.buttonA_2['state'] = "disable"
            self.buttonA_3['state'] = "disable"
            self.buttonA_4['state'] = "normal"

            self.logPrint(0, True, "read number of thread : thread count = " + str(threading.active_count()))
        elif (result == "no"):
            pass

    def logPrintProgram(self):
        while Ditel_DROS_Kernel.threadCondition:
            for _i in range(1, 21, 1):
                if(programsys.addressProgram[_i]._serial._log_contents != None):
                    mainWindow.logPrint(_i, programsys.addressProgram[_i]._serial._log_condition,programsys.addressProgram[_i]._serial._log_contents)
                    programsys.addressProgram[_i]._serial._log_contents = None
                
                if(programsys.addressProgram[_i]._serial._txLog != None):
                    mainWindow.txLogPrint(_i, programsys.addressProgram[_i]._serial._txLog)
                    programsys.addressProgram[_i]._serial._txLog = None

                if(programsys.addressProgram[_i]._serial._rxLog != None):
                    mainWindow.rxLogPrint(_i, programsys.addressProgram[_i]._serial._rxLog)
                    programsys.addressProgram[_i]._serial._rxLog = None
                    
            time.sleep(0.1)

    def startWindow(self):
        self.window1_frame.deiconify()
        self.window1_frame.geometry(str(WINDOW1_HEIGHT) + "x" + str(WINDOW1_WIDETH))
        self.window1_frame.title(WINDOW1_TITEL)
        self.frame['bg'] = COLOR_WINDOW
        self.window1_frame['bg'] = COLOR_WINDOW

        self.window1Menubar = tkinter.Menu(self.window1_frame, fg= COLOR_MENU_BAR_TEXT,bg=COLOR_MENU_BAR_BACK)
        self.window1_frame.config(menu=self.window1Menubar)

        #メニューバーの内容の作成
        self.window1FileMenu = tkinter.Menu(self.window1_frame, fg=COLOR_MENU_BAR_TEXT, bg=COLOR_MENU_BAR_BACK, tearoff=False)
        self.window1SettingMenu = tkinter.Menu(self.window1_frame, fg=COLOR_MENU_BAR_TEXT, bg=COLOR_MENU_BAR_BACK, tearoff=False)

        #メニューバーの内容の設定
        self.window1Menubar.add_cascade(label="ファイル", menu=self.window1FileMenu)  #ファイルのメニュー
        self.window1Menubar.add_cascade(label="設定", menu=self.window1SettingMenu)  #設定のメニュー

        #ファイルメニューの内容
        self.window1FileMenu.add_command(label="終了", command=self.quitWindow)

        #設定の内容
        self.window1SettingMenu.add_command(label="ポート・アドレスの設定", command=self.portAddressSetting)
        self.window1SettingMenu.add_command(label="ポート・アドレスの確認", command=portAddressSettingCheckWindow.startWindow)

        self.frame.grid(row=0, column=0)
        self.label0_1.grid(row=0, column=0)
        self.label0_2.grid(row=0, column=1)
        self.label0_3.grid(row=0, column=2)
        self.label0_4.grid(row=0, column=3)
        self.label0_5.grid(row=0, column=4)
        self.label0_6.grid(row=0, column=5)
        self.label0_7.grid(row=0, column=6)
        self.label0_8.grid(row=0, column=7)
        self.label0_9.grid(row=0, column=8)
        self.label0_10.grid(row=0, column=9)
        self.label0_11.grid(row=0, column=10)
        self.label0_12.grid(row=0, column=11)
        
        self.label0_13.grid(row=0, column=12)

        self.label0_14.grid(row=0, column=13)
        self.label0_15.grid(row=0, column=14)
        self.label0_16.grid(row=0, column=15)
        self.label0_17.grid(row=0, column=16)
        self.label0_18.grid(row=0, column=17)
        self.label0_19.grid(row=0, column=18)
        self.label0_20.grid(row=0, column=19)
        self.label0_21.grid(row=0, column=20)
        self.label0_22.grid(row=0, column=21)
        self.label0_23.grid(row=0, column=22)
        self.label0_24.grid(row=0, column=23)
        self.label0_25.grid(row=0, column=24)


        self.label1_1.grid(row=1, column=0)
        self.label1_2.grid(row=1, column=1)
        self.entry1_1.grid(row=1, column=2)
        self.label1_3.grid(row=1, column=3)
        self.listbox1_1.grid(row=1, column=4)
        self.listbox1_1_scroolbar.grid(row=1, column=5, sticky=(tkinter.N, tkinter.S))
        self.label1_4.grid(row=1, column=6)
        self.listbox1_2.grid(row=1, column=7)
        self.listbox1_2_scroolbar.grid(row=1, column=8, sticky=(tkinter.N, tkinter.S))
        self.label1_5.grid(row=1, column=9)
        self.listbox1_3.grid(row=1, column=10)
        self.listbox1_3_scroolbar.grid(row=1, column=11, sticky=(tkinter.N, tkinter.S))

        self.label1_6.grid(row=1, column=12)
        
        self.label1_7.grid(row=1, column=13)
        self.label1_8.grid(row=1, column=14)
        self.entry1_2.grid(row=1, column=15)
        self.label1_9.grid(row=1, column=16)
        self.listbox1_4.grid(row=1, column=17)
        self.listbox1_4_scroolbar.grid(row=1, column=18, sticky=(tkinter.N, tkinter.S))
        self.label1_10.grid(row=1, column=19)
        self.listbox1_5.grid(row=1, column=20)
        self.listbox1_5_scroolbar.grid(row=1, column=21, sticky=(tkinter.N, tkinter.S))
        self.label1_11.grid(row=1, column=22)
        self.listbox1_6.grid(row=1, column=23)
        self.listbox1_6_scroolbar.grid(row=1, column=24, sticky=(tkinter.N, tkinter.S))


        self.label2_1.grid(row=2, column=0)
        self.label2_2.grid(row=2, column=1)
        self.entry2_1.grid(row=2, column=2)
        self.label2_3.grid(row=2, column=3)
        self.listbox2_1.grid(row=2, column=4)
        self.listbox2_1_scroolbar.grid(row=2, column=5, sticky=(tkinter.N, tkinter.S))
        self.label2_4.grid(row=2, column=6)
        self.listbox2_2.grid(row=2, column=7)
        self.listbox2_2_scroolbar.grid(row=2, column=8, sticky=(tkinter.N, tkinter.S))
        self.label2_5.grid(row=2, column=9)
        self.listbox2_3.grid(row=2, column=10)
        self.listbox2_3_scroolbar.grid(row=2, column=11, sticky=(tkinter.N, tkinter.S))

        self.label2_6.grid(row=2, column=12)
        
        self.label2_7.grid(row=2, column=13)
        self.label2_8.grid(row=2, column=14)
        self.entry2_2.grid(row=2, column=15)
        self.label2_9.grid(row=2, column=16)
        self.listbox2_4.grid(row=2, column=17)
        self.listbox2_4_scroolbar.grid(row=2, column=18, sticky=(tkinter.N, tkinter.S))
        self.label2_10.grid(row=2, column=19)
        self.listbox2_5.grid(row=2, column=20)
        self.listbox2_5_scroolbar.grid(row=2, column=21, sticky=(tkinter.N, tkinter.S))
        self.label2_11.grid(row=2, column=22)
        self.listbox2_6.grid(row=2, column=23)
        self.listbox2_6_scroolbar.grid(row=2, column=24, sticky=(tkinter.N, tkinter.S))


        self.label3_1.grid(row=3, column=0)
        self.label3_2.grid(row=3, column=1)
        self.entry3_1.grid(row=3, column=2)
        self.label3_3.grid(row=3, column=3)
        self.listbox3_1.grid(row=3, column=4)
        self.listbox3_1_scroolbar.grid(row=3, column=5, sticky=(tkinter.N, tkinter.S))
        self.label3_4.grid(row=3, column=6)
        self.listbox3_2.grid(row=3, column=7)
        self.listbox3_2_scroolbar.grid(row=3, column=8, sticky=(tkinter.N, tkinter.S))
        self.label3_5.grid(row=3, column=9)
        self.listbox3_3.grid(row=3, column=10)
        self.listbox3_3_scroolbar.grid(row=3, column=11, sticky=(tkinter.N, tkinter.S))

        self.label3_6.grid(row=3, column=12)
        
        self.label3_7.grid(row=3, column=13)
        self.label3_8.grid(row=3, column=14)
        self.entry3_2.grid(row=3, column=15)
        self.label3_9.grid(row=3, column=16)
        self.listbox3_4.grid(row=3, column=17)
        self.listbox3_4_scroolbar.grid(row=3, column=18, sticky=(tkinter.N, tkinter.S))
        self.label3_10.grid(row=3, column=19)
        self.listbox3_5.grid(row=3, column=20)
        self.listbox3_5_scroolbar.grid(row=3, column=21, sticky=(tkinter.N, tkinter.S))
        self.label3_11.grid(row=3, column=22)
        self.listbox3_6.grid(row=3, column=23)
        self.listbox3_6_scroolbar.grid(row=3, column=24, sticky=(tkinter.N, tkinter.S))


        self.label4_1.grid(row=4, column=0)
        self.label4_2.grid(row=4, column=1)
        self.entry4_1.grid(row=4, column=2)
        self.label4_3.grid(row=4, column=3)
        self.listbox4_1.grid(row=4, column=4)
        self.listbox4_1_scroolbar.grid(row=4, column=5, sticky=(tkinter.N, tkinter.S))
        self.label4_4.grid(row=4, column=6)
        self.listbox4_2.grid(row=4, column=7)
        self.listbox4_2_scroolbar.grid(row=4, column=8, sticky=(tkinter.N, tkinter.S))
        self.label4_5.grid(row=4, column=9)
        self.listbox4_3.grid(row=4, column=10)
        self.listbox4_3_scroolbar.grid(row=4, column=11, sticky=(tkinter.N, tkinter.S))

        self.label4_6.grid(row=4, column=12)
        
        self.label4_7.grid(row=4, column=13)
        self.label4_8.grid(row=4, column=14)
        self.entry4_2.grid(row=4, column=15)
        self.label4_9.grid(row=4, column=16)
        self.listbox4_4.grid(row=4, column=17)
        self.listbox4_4_scroolbar.grid(row=4, column=18, sticky=(tkinter.N, tkinter.S))
        self.label4_10.grid(row=4, column=19)
        self.listbox4_5.grid(row=4, column=20)
        self.listbox4_5_scroolbar.grid(row=4, column=21, sticky=(tkinter.N, tkinter.S))
        self.label4_11.grid(row=4, column=22)
        self.listbox4_6.grid(row=4, column=23)
        self.listbox4_6_scroolbar.grid(row=4, column=24, sticky=(tkinter.N, tkinter.S))


        self.label5_1.grid(row=5, column=0)
        self.label5_2.grid(row=5, column=1)
        self.entry5_1.grid(row=5, column=2)
        self.label5_3.grid(row=5, column=3)
        self.listbox5_1.grid(row=5, column=4)
        self.listbox5_1_scroolbar.grid(row=5, column=5, sticky=(tkinter.N, tkinter.S))
        self.label5_4.grid(row=5, column=6)
        self.listbox5_2.grid(row=5, column=7)
        self.listbox5_2_scroolbar.grid(row=5, column=8, sticky=(tkinter.N, tkinter.S))
        self.label5_5.grid(row=5, column=9)
        self.listbox5_3.grid(row=5, column=10)
        self.listbox5_3_scroolbar.grid(row=5, column=11, sticky=(tkinter.N, tkinter.S))

        self.label5_6.grid(row=5, column=12)
        
        self.label5_7.grid(row=5, column=13)
        self.label5_8.grid(row=5, column=14)
        self.entry5_2.grid(row=5, column=15)
        self.label5_9.grid(row=5, column=16)
        self.listbox5_4.grid(row=5, column=17)
        self.listbox5_4_scroolbar.grid(row=5, column=18, sticky=(tkinter.N, tkinter.S))
        self.label5_10.grid(row=5, column=19)
        self.listbox5_5.grid(row=5, column=20)
        self.listbox5_5_scroolbar.grid(row=5, column=21, sticky=(tkinter.N, tkinter.S))
        self.label5_11.grid(row=5, column=22)
        self.listbox5_6.grid(row=5, column=23)
        self.listbox5_6_scroolbar.grid(row=5, column=24, sticky=(tkinter.N, tkinter.S))


        self.label6_1.grid(row=6, column=0)
        self.label6_2.grid(row=6, column=1)
        self.entry6_1.grid(row=6, column=2)
        self.label6_3.grid(row=6, column=3)
        self.listbox6_1.grid(row=6, column=4)
        self.listbox6_1_scroolbar.grid(row=6, column=5, sticky=(tkinter.N, tkinter.S))
        self.label6_4.grid(row=6, column=6)
        self.listbox6_2.grid(row=6, column=7)
        self.listbox6_2_scroolbar.grid(row=6, column=8, sticky=(tkinter.N, tkinter.S))
        self.label6_5.grid(row=6, column=9)
        self.listbox6_3.grid(row=6, column=10)
        self.listbox6_3_scroolbar.grid(row=6, column=11, sticky=(tkinter.N, tkinter.S))

        self.label6_6.grid(row=6, column=12)
        
        self.label6_7.grid(row=6, column=13)
        self.label6_8.grid(row=6, column=14)
        self.entry6_2.grid(row=6, column=15)
        self.label6_9.grid(row=6, column=16)
        self.listbox6_4.grid(row=6, column=17)
        self.listbox6_4_scroolbar.grid(row=6, column=18, sticky=(tkinter.N, tkinter.S))
        self.label6_10.grid(row=6, column=19)
        self.listbox6_5.grid(row=6, column=20)
        self.listbox6_5_scroolbar.grid(row=6, column=21, sticky=(tkinter.N, tkinter.S))
        self.label6_11.grid(row=6, column=22)
        self.listbox6_6.grid(row=6, column=23)
        self.listbox6_6_scroolbar.grid(row=6, column=24, sticky=(tkinter.N, tkinter.S))


        self.label7_1.grid(row=7, column=0)
        self.label7_2.grid(row=7, column=1)
        self.entry7_1.grid(row=7, column=2)
        self.label7_3.grid(row=7, column=3)
        self.listbox7_1.grid(row=7, column=4)
        self.listbox7_1_scroolbar.grid(row=7, column=5, sticky=(tkinter.N, tkinter.S))
        self.label7_4.grid(row=7, column=6)
        self.listbox7_2.grid(row=7, column=7)
        self.listbox7_2_scroolbar.grid(row=7, column=8, sticky=(tkinter.N, tkinter.S))
        self.label7_5.grid(row=7, column=9)
        self.listbox7_3.grid(row=7, column=10)
        self.listbox7_3_scroolbar.grid(row=7, column=11, sticky=(tkinter.N, tkinter.S))

        self.label7_6.grid(row=7, column=12)
        
        self.label7_7.grid(row=7, column=13)
        self.label7_8.grid(row=7, column=14)
        self.entry7_2.grid(row=7, column=15)
        self.label7_9.grid(row=7, column=16)
        self.listbox7_4.grid(row=7, column=17)
        self.listbox7_4_scroolbar.grid(row=7, column=18, sticky=(tkinter.N, tkinter.S))
        self.label7_10.grid(row=7, column=19)
        self.listbox7_5.grid(row=7, column=20)
        self.listbox7_5_scroolbar.grid(row=7, column=21, sticky=(tkinter.N, tkinter.S))
        self.label7_11.grid(row=7, column=22)
        self.listbox7_6.grid(row=7, column=23)
        self.listbox7_6_scroolbar.grid(row=7, column=24, sticky=(tkinter.N, tkinter.S))


        self.label8_1.grid(row=8, column=0)
        self.label8_2.grid(row=8, column=1)
        self.entry8_1.grid(row=8, column=2)
        self.label8_3.grid(row=8, column=3)
        self.listbox8_1.grid(row=8, column=4)
        self.listbox8_1_scroolbar.grid(row=8, column=5, sticky=(tkinter.N, tkinter.S))
        self.label8_4.grid(row=8, column=6)
        self.listbox8_2.grid(row=8, column=7)
        self.listbox8_2_scroolbar.grid(row=8, column=8, sticky=(tkinter.N, tkinter.S))
        self.label8_5.grid(row=8, column=9)
        self.listbox8_3.grid(row=8, column=10)
        self.listbox8_3_scroolbar.grid(row=8, column=11, sticky=(tkinter.N, tkinter.S))

        self.label8_6.grid(row=8, column=12)
        
        self.label8_7.grid(row=8, column=13)
        self.label8_8.grid(row=8, column=14)
        self.entry8_2.grid(row=8, column=15)
        self.label8_9.grid(row=8, column=16)
        self.listbox8_4.grid(row=8, column=17)
        self.listbox8_4_scroolbar.grid(row=8, column=18, sticky=(tkinter.N, tkinter.S))
        self.label8_10.grid(row=8, column=19)
        self.listbox8_5.grid(row=8, column=20)
        self.listbox8_5_scroolbar.grid(row=8, column=21, sticky=(tkinter.N, tkinter.S))
        self.label8_11.grid(row=8, column=22)
        self.listbox8_6.grid(row=8, column=23)
        self.listbox8_6_scroolbar.grid(row=8, column=24, sticky=(tkinter.N, tkinter.S))


        self.label9_1.grid(row=9, column=0)
        self.label9_2.grid(row=9, column=1)
        self.entry9_1.grid(row=9, column=2)
        self.label9_3.grid(row=9, column=3)
        self.listbox9_1.grid(row=9, column=4)
        self.listbox9_1_scroolbar.grid(row=9, column=5, sticky=(tkinter.N, tkinter.S))
        self.label9_4.grid(row=9, column=6)
        self.listbox9_2.grid(row=9, column=7)
        self.listbox9_2_scroolbar.grid(row=9, column=8, sticky=(tkinter.N, tkinter.S))
        self.label9_5.grid(row=9, column=9)
        self.listbox9_3.grid(row=9, column=10)
        self.listbox9_3_scroolbar.grid(row=9, column=11, sticky=(tkinter.N, tkinter.S))

        self.label9_6.grid(row=9, column=12)
        
        self.label9_7.grid(row=9, column=13)
        self.label9_8.grid(row=9, column=14)
        self.entry9_2.grid(row=9, column=15)
        self.label9_9.grid(row=9, column=16)
        self.listbox9_4.grid(row=9, column=17)
        self.listbox9_4_scroolbar.grid(row=9, column=18, sticky=(tkinter.N, tkinter.S))
        self.label9_10.grid(row=9, column=19)
        self.listbox9_5.grid(row=9, column=20)
        self.listbox9_5_scroolbar.grid(row=9, column=21, sticky=(tkinter.N, tkinter.S))
        self.label9_11.grid(row=9, column=22)
        self.listbox9_6.grid(row=9, column=23)
        self.listbox9_6_scroolbar.grid(row=9, column=24, sticky=(tkinter.N, tkinter.S))


        self.label10_1.grid(row=10, column=0)
        self.label10_2.grid(row=10, column=1)
        self.entry10_1.grid(row=10, column=2)
        self.label10_3.grid(row=10, column=3)
        self.listbox10_1.grid(row=10, column=4)
        self.listbox10_1_scroolbar.grid(row=10, column=5, sticky=(tkinter.N, tkinter.S))
        self.label10_4.grid(row=10, column=6)
        self.listbox10_2.grid(row=10, column=7)
        self.listbox10_2_scroolbar.grid(row=10, column=8, sticky=(tkinter.N, tkinter.S))
        self.label10_5.grid(row=10, column=9)
        self.listbox10_3.grid(row=10, column=10)
        self.listbox10_3_scroolbar.grid(row=10, column=11, sticky=(tkinter.N, tkinter.S))

        self.label10_6.grid(row=10, column=12)
        
        self.label10_7.grid(row=10, column=13)
        self.label10_8.grid(row=10, column=14)
        self.entry10_2.grid(row=10, column=15)
        self.label10_9.grid(row=10, column=16)
        self.listbox10_4.grid(row=10, column=17)
        self.listbox10_4_scroolbar.grid(row=10, column=18, sticky=(tkinter.N, tkinter.S))
        self.label10_10.grid(row=10, column=19)
        self.listbox10_5.grid(row=10, column=20)
        self.listbox10_5_scroolbar.grid(row=10, column=21, sticky=(tkinter.N, tkinter.S))
        self.label10_11.grid(row=10, column=22)
        self.listbox10_6.grid(row=10, column=23)
        self.listbox10_6_scroolbar.grid(row=10, column=24, sticky=(tkinter.N, tkinter.S))

        
        self.labelA_1.grid(row=11, column=0)
        self.labelA_2.grid(row=11, column=23)
        self.listboxA_1.grid(rowspan=5,columnspan=21, row=12, column=0, sticky=tkinter.W+tkinter.E+tkinter.N+tkinter.S)
        self.listboxA_1_scroolbar.grid(rowspan=5, row=12, column=21, sticky=(tkinter.N, tkinter.S))
        self.buttonA_1.grid(row= 12, column=23)
        self.buttonA_2.grid(row= 13, column=23)
        self.buttonA_3.grid(row= 14, column=23)
        self.buttonA_4.grid(row= 15, column=23)
        self.buttonA_5.grid(row= 16, column=23)
        

        self.window1_frame.mainloop()

        exit()

    def quitWindow(self):
        if(programHasStarted):
            stopCommunicationReturn = self.stopCommunication()
            if(stopCommunicationReturn):
                print("[  OK  ] stop communication and thread")
                self.window1_frame.destroy()
            else:
                print("[FAIED] stop communication and thread")
        else:
            self.window1_frame.destroy()

        print("[  OK  ] DROS will shutdown soon....")
        exit()

    def stopCommunication(self):
        result = tkinter.messagebox.askquestion(title="通信の終了", message="本当に通信を終了しますか?")
        if (result  == "yes"):
            self.logPrint(0, True, "read number of thread : thread count = " + str(threading.active_count()))
            self.logPrint(0, True, "start address threads stopping")
            Ditel_DROS_Kernel.threadCondition = False

            
            for _i in range(1, 21, 1):
                self.logPrint(_i, programsys.addressProgram[_i]._serial.end(), "serial thread stoped")
                try:
                    programsys.addressThread[_i].join()
                    self.logPrint(_i, True, " user program thread stoped")
                except:
                    self.logPrint(_i, False,  " user program thread stoped")
            
            
            try:
                programsys.addressThread[0].join()
                self.logPrint(0, True,  " user program thread stoped")
            except:
                self.logPrint(0, False, "user program thread stoped")

            self.logPrint(0, True, "finish all serial thread and user program thread stopping")

            self.logPrint(0, True, "read number of thread : thread count = " + str(threading.active_count()))

            
            try:
                self.threadForLog.join()
                self.logPrint(0, True, "log print thread stoped")
            except:
                self.logPrint(0, False, "log print thread stoped")
            
            
            try:
                bypasssys._bypassThread.join()
                self.logPrint(0, True, "bypass thread stop")
            except:
                self.logPrint(0, False, "bypass thread stop")
            
            try:
                emergencysys._emergencyThread.join()
                self.logPrint(0, True, "state read thread stop")
            except:
                self.logPrint(0, False, "state read thread stop")
            

            self.logPrint(0, True, "finish all thread stopping")

            self.logPrint(0, True, "read number of thread : thread count = " + str(threading.active_count()))

            self.buttonA_4['state'] = "disable"
            self.buttonA_5['state'] = "normal"
            return True
        elif (result == "no"):
            return False

#==============↑↑window1関係(ここまで)↑↑===============


#==============↓↓window2関係(ここから)↓↓=============== #TODOwindow2関係
class window2_Contents:
    def __init__(self):
        self.window2_frame = tkinter.Tk()
        self.frame = tkinter.Frame(self.window2_frame)
        self.window2_frame.withdraw()

        self.window2_frame.protocol('WM_DELETE_WINDOW', self.quitWindow)

        self.style = tkinter.ttk.Style(self.frame)
        self.text = tkinter.StringVar(self.frame)
        self.label1 = tkinter.ttk.Label(self.frame, text="ポートとアドレスの設定方法を\n選択してください.", font=font1)
        self.button1 = tkinter.ttk.Button(self.frame, text="自動で設定する", command=self.window2ToAutoMode, width=14)
        self.button2 = tkinter.ttk.Button(self.frame, text="手動で設定する", command=self.window2ToManualMode, width=14)

        self.hasMade:bool = False

        self.style.configure("TLabel",
                             foreground=COLOR_LABEL_TEXT,
                             background=COLOR_LABEL_BACK
                             )

        self.style.configure("TScrollbar",
                             gripcount=0, 
                             background=COLOR_SCROOLBAR_BAR, 
                             darkcolor=COLOR_SCROOLBAR_BAR, 
                             lightcolor=COLOR_SCROOLBAR_BAR, 
                             troughcolor=COLOR_SCROOLBAR_BACK, 
                             bordercolor=COLOR_SCROOLBAR_BACK, 
                             arrowcolor=COLOR_SCROOLBAR_BAR
                            )
        
        self.style.configure("TButton",
                             padding=6,
                             relief="flat", 
                             background=COLOR_BUTTON_NORMAL_BACK, 
                             foreground=COLOR_BUTTON_NORMAL_TEXT, 
                             font=font1
                            )

        self.style.map("TButton",
                       foreground=[('pressed', '!disabled', COLOR_BUTTON_CLICK_TEXT), 
                                   ('disabled', COLOR_BUTTON_DISABLED_TEXT), 
                                   ('active', COLOR_BUTTON_TOUCH_TEXT)
                                  ],
                       background=[('pressed', '!disabled', COLOR_BUTTON_CLICK_BACK), 
                                   ('disabled', COLOR_BUTTON_DISABLED_BACK), 
                                   ('active', COLOR_BUTTON_TOUCH_BACK)
                                  ]
                    )

    def window2ToAutoMode(self):
        portAddressAutoSettingWindow.startWindow()
        self.window2_frame.withdraw()

    def window2ToManualMode(self):
        portAddressManualSettingWindow.startWindow()
        self.window2_frame.withdraw()

    def startWindow(self):
        self.window2_frame.deiconify()
        self.window2_frame.lift()
        self.window2_frame.maxsize(width=WINDOW2_WIDETH, height=WINDOW2_HEIGHT)
        self.window2_frame.minsize(width=WINDOW2_WIDETH, height=WINDOW2_HEIGHT)
        self.window2_frame.title(WINDOW2_TITEL)
        self.frame['bg'] = COLOR_WINDOW
        self.window2_frame['bg'] = COLOR_WINDOW

        self.text.set("Serch")

        if (self.hasMade == False):
            self.frame.pack(fill=tkinter.BOTH, padx=1, pady=5)

            self.label1.pack()
            self.button1.pack(side=tkinter.LEFT, padx=40, pady=20)
            self.button2.pack(side=tkinter.LEFT, padx=0, pady=0)
        
        self.hasMade = True

    def quitWindow(self):
        self.window2_frame.withdraw()

#==============↑↑window2関係(ここまで)↑↑===============


#==============↓↓window2_1関係(ここから)↓↓=============== #TODOwindow2_1関係
class window2_1_Contens:
    def __init__(self):
        self.window2_1_frame = tkinter.Tk()
        self.window2_1_frame.protocol('WM_DELETE_WINDOW', self.quitWindow)
        self.frame = tkinter.Frame(self.window2_1_frame)
        self.window2_1_frame.withdraw()

        self.style = tkinter.ttk.Style(self.frame)

        self.style.configure("TLabel",
                             foreground=COLOR_LABEL_TEXT,
                             background=COLOR_LABEL_BACK
                             )

        self.style.configure("TScrollbar",
                             gripcount=0, 
                             background=COLOR_SCROOLBAR_BAR, 
                             darkcolor=COLOR_SCROOLBAR_BAR, 
                             lightcolor=COLOR_SCROOLBAR_BAR, 
                             troughcolor=COLOR_SCROOLBAR_BACK, 
                             bordercolor=COLOR_SCROOLBAR_BACK, 
                             arrowcolor=COLOR_SCROOLBAR_BAR
                            )
        
        self.style.configure("TButton",
                             padding=6,
                             relief="flat", 
                             background=COLOR_BUTTON_NORMAL_BACK, 
                             foreground=COLOR_BUTTON_NORMAL_TEXT, 
                             font=font1
                            )

        self.style.map("TButton",
                       foreground=[('pressed', '!disabled', COLOR_BUTTON_CLICK_TEXT), 
                                   ('disabled', COLOR_BUTTON_DISABLED_TEXT), 
                                   ('active', COLOR_BUTTON_TOUCH_TEXT)
                                  ],
                       background=[('pressed', '!disabled', COLOR_BUTTON_CLICK_BACK), 
                                   ('disabled', COLOR_BUTTON_DISABLED_BACK), 
                                   ('active', COLOR_BUTTON_TOUCH_BACK)
                                  ]
                    )

        self.label1 = tkinter.ttk.Label(self.frame, text="ログ", font=font1)

        self.listbox1 = tkinter.Listbox(self.frame, width=65, height=18, relief="sunken", font=font2)
        self.listbox1_scroolbar = tkinter.ttk.Scrollbar(self.frame, orient=tkinter.VERTICAL, command=self.listbox1.yview)

        self.button1 = tkinter.ttk.Button(self.frame, text="完了", command=self.quitWindow, width=10)

        self.hasMade = False
    
    def setSerialPort(self):
        for _i in range(len(portAddressRelationships)):
            portAddressRelationships[_i] = None

        self.listbox1.insert(tkinter.END, "[  OK  ] start read serial port")
        self.listSerialPort = portsRead()
        for _i in range(len(self.listSerialPort)):
            self.listbox1.insert(tkinter.END, "  port" + str(_i) + " : " + self.listSerialPort[_i])
        self.listbox1.insert(tkinter.END, "[  OK  ] finish read serial port")

        self.listbox1.insert(tkinter.END, "[  OK  ] start read address")
        try:
            for _i in range(len(self.listSerialPort)):
                self.listbox1.insert(tkinter.END, "[  OK  ] start read address of port" + str(_i))
                self.returnInfo = addressRead(self.listSerialPort[_i])
                
                if((self.returnInfo[0] != HEAD_WORD) or (self.returnInfo[1] != COMMAND_CHECK_ADDRESS)):
                    self.listbox1.insert(tkinter.END, "[FAILED] finish read address of port" + str(_i))
                else:
                    self.listbox1.insert(tkinter.END, "[  OK  ] finish read address of port" + str(_i) + "  : port = " + str(self.listSerialPort[_i]) + "  : address = " + str(self.returnInfo[2]))
                    portAddressRelationships[int(self.returnInfo[2])] = self.listSerialPort[_i]
        except:
            tkinter.messagebox.showerror("エラー", "ありえないアドレスを要求されました.\n・マイコンがリセットされているか. \n・正しいアドレスが設定されているか. \n上記のことを確認してください.")
        
    def startWindow(self):
        self.window2_1_frame.deiconify()
        self.frame.pack(fill=tkinter.BOTH, padx=1, pady=5)

        self.window2_1_frame.lift()
        self.window2_1_frame.maxsize(width=WINDOW2_1_WIDETH, height=WINDOW2_1_HEIGHT)
        self.window2_1_frame.minsize(width=WINDOW2_1_WIDETH, height=WINDOW2_1_HEIGHT)
        self.window2_1_frame.title(WINDOW2_1_TITEL)
        self.frame['bg'] = COLOR_WINDOW
        self.window2_1_frame['bg'] = COLOR_WINDOW

        if(self.hasMade == False):
            self.frame.grid(row=0, column=0)

            self.label1.grid(row=0, column=0)
            self.listbox1.grid(row=1, column=0)
            self.listbox1_scroolbar.grid(row=1, column=1, sticky=(tkinter.N, tkinter.S))
            self.button1.grid(row=2, column=0)

        self.listbox1.delete(0, tkinter.END)
        self.setSerialPort()

        self.hasMade = True

    def quitWindow(self):
        self.window2_1_frame.withdraw()
        portAddressSettingCheckWindow.startWindow()

#==============↑↑window2_1関係(ここまで)↑↑===============


#==============↓↓window2_2関係(ここから)↓↓=============== #TODOwindow2_2関係
class window2_2_Contents:
    def __init__(self):
        COMBOBOX_ENTRY_BETWEEN_WIDETH = "   "
        LEFT_RIGHT_BETWEEN_WIDETH =     "        "

        self.window2_2_frame = tkinter.Tk()
        self.frame = tkinter.Frame(self.window2_2_frame)
        self.window2_2_frame.protocol('WM_DELETE_WINDOW', self.quitWindow)
        self.window2_2_frame.withdraw()

        self.style = tkinter.ttk.Style(self.frame)

        self.style.configure("TLabel",
                             foreground=COLOR_LABEL_TEXT,
                             background=COLOR_LABEL_BACK
                             )

        self.style.configure("TScrollbar",
                             gripcount=0, 
                             background=COLOR_SCROOLBAR_BAR, 
                             darkcolor=COLOR_SCROOLBAR_BAR, 
                             lightcolor=COLOR_SCROOLBAR_BAR, 
                             troughcolor=COLOR_SCROOLBAR_BACK, 
                             bordercolor=COLOR_SCROOLBAR_BACK, 
                             arrowcolor=COLOR_SCROOLBAR_BAR
                            )
        
        self.style.configure("TButton",
                             padding=6,
                             relief="flat", 
                             background=COLOR_BUTTON_NORMAL_BACK, 
                             foreground=COLOR_BUTTON_NORMAL_TEXT, 
                             font=font1
                            )

        self.style.map("TButton",
                       foreground=[('pressed', '!disabled', COLOR_BUTTON_CLICK_TEXT), 
                                   ('disabled', COLOR_BUTTON_DISABLED_TEXT), 
                                   ('active', COLOR_BUTTON_TOUCH_TEXT)
                                  ],
                       background=[('pressed', '!disabled', COLOR_BUTTON_CLICK_BACK), 
                                   ('disabled', COLOR_BUTTON_DISABLED_BACK), 
                                   ('active', COLOR_BUTTON_TOUCH_BACK)
                                  ]
                    )

        self.style.configure("TCheckbutton",
                             foreground=COLOR_CHECKBUTTON_TEXT,
                             background=COLOR_CHECKBUTTON_BACK
                             )
        
        self.style.map("TCheckbutton",
                       foreground=[('active', COLOR_CHECKBUTTON_TOUCH_TEXT)],
                       background=[('active', COLOR_CHECKBUTTON_TOUCH_BACK)]
                    )

        self.ComboboxList = []
        self.ComboboxList = portsRead()

        self.combobox1_1 = tkinter.ttk.Combobox(self.frame, values=self.ComboboxList, state="disable")
        self.combobox1_2 = tkinter.ttk.Combobox(self.frame, values=self.ComboboxList, state="disable")
        self.combobox2_1 = tkinter.ttk.Combobox(self.frame, values=self.ComboboxList, state="disable")
        self.combobox2_2 = tkinter.ttk.Combobox(self.frame, values=self.ComboboxList, state="disable")
        self.combobox3_1 = tkinter.ttk.Combobox(self.frame, values=self.ComboboxList, state="disable")
        self.combobox3_2 = tkinter.ttk.Combobox(self.frame, values=self.ComboboxList, state="disable")
        self.combobox4_1 = tkinter.ttk.Combobox(self.frame, values=self.ComboboxList, state="disable")
        self.combobox4_2 = tkinter.ttk.Combobox(self.frame, values=self.ComboboxList, state="disable")
        self.combobox5_1 = tkinter.ttk.Combobox(self.frame, values=self.ComboboxList, state="disable")
        self.combobox5_2 = tkinter.ttk.Combobox(self.frame, values=self.ComboboxList, state="disable")
        self.combobox6_1 = tkinter.ttk.Combobox(self.frame, values=self.ComboboxList, state="disable")
        self.combobox6_2 = tkinter.ttk.Combobox(self.frame, values=self.ComboboxList, state="disable")
        self.combobox7_1 = tkinter.ttk.Combobox(self.frame, values=self.ComboboxList, state="disable")
        self.combobox7_2 = tkinter.ttk.Combobox(self.frame, values=self.ComboboxList, state="disable")
        self.combobox8_1 = tkinter.ttk.Combobox(self.frame, values=self.ComboboxList, state="disable")
        self.combobox8_2 = tkinter.ttk.Combobox(self.frame, values=self.ComboboxList, state="disable")
        self.combobox9_1 = tkinter.ttk.Combobox(self.frame, values=self.ComboboxList, state="disable")
        self.combobox9_2 = tkinter.ttk.Combobox(self.frame, values=self.ComboboxList, state="disable")
        self.combobox10_1 = tkinter.ttk.Combobox(self.frame, values=self.ComboboxList, state="disable")
        self.combobox10_2 = tkinter.ttk.Combobox(self.frame, values=self.ComboboxList, state="disable")


        self.checkbutton1_1_value = tkinter.BooleanVar(self.frame)
        self.checkbutton1_1 = tkinter.ttk.Checkbutton(self.frame, text="このアドレスを使用する", command=self.Checkbutton1_1Command, variable=self.checkbutton1_1_value)
        self.checkbutton1_2_value = tkinter.BooleanVar(self.frame)
        self.checkbutton1_2 = tkinter.ttk.Checkbutton(self.frame, text="このアドレスを使用する", command=self.Checkbutton1_2Command, variable=self.checkbutton1_2_value)

        self.checkbutton2_1_value = tkinter.BooleanVar(self.frame)
        self.checkbutton2_1 = tkinter.ttk.Checkbutton(self.frame, text="このアドレスを使用する", command=self.Checkbutton2_1Command, variable=self.checkbutton2_1_value)
        self.checkbutton2_2_value = tkinter.BooleanVar(self.frame)
        self.checkbutton2_2 = tkinter.ttk.Checkbutton(self.frame, text="このアドレスを使用する", command=self.Checkbutton2_2Command, variable=self.checkbutton2_2_value)

        self.checkbutton3_1_value = tkinter.BooleanVar(self.frame)
        self.checkbutton3_1 = tkinter.ttk.Checkbutton(self.frame, text="このアドレスを使用する", command=self.Checkbutton3_1Command, variable=self.checkbutton3_1_value)
        self.checkbutton3_2_value = tkinter.BooleanVar(self.frame)
        self.checkbutton3_2 = tkinter.ttk.Checkbutton(self.frame, text="このアドレスを使用する", command=self.Checkbutton3_2Command, variable=self.checkbutton3_2_value)

        self.checkbutton4_1_value = tkinter.BooleanVar(self.frame)
        self.checkbutton4_1 = tkinter.ttk.Checkbutton(self.frame, text="このアドレスを使用する", command=self.Checkbutton4_1Command, variable=self.checkbutton4_1_value)
        self.checkbutton4_2_value = tkinter.BooleanVar(self.frame)
        self.checkbutton4_2 = tkinter.ttk.Checkbutton(self.frame, text="このアドレスを使用する", command=self.Checkbutton4_2Command, variable=self.checkbutton4_2_value)

        self.checkbutton5_1_value = tkinter.BooleanVar(self.frame)
        self.checkbutton5_1 = tkinter.ttk.Checkbutton(self.frame, text="このアドレスを使用する", command=self.Checkbutton5_1Command, variable=self.checkbutton5_1_value)
        self.checkbutton5_2_value = tkinter.BooleanVar(self.frame)
        self.checkbutton5_2 = tkinter.ttk.Checkbutton(self.frame, text="このアドレスを使用する", command=self.Checkbutton5_2Command, variable=self.checkbutton5_2_value)

        self.checkbutton6_1_value = tkinter.BooleanVar(self.frame)
        self.checkbutton6_1 = tkinter.ttk.Checkbutton(self.frame, text="このアドレスを使用する", command=self.Checkbutton6_1Command, variable=self.checkbutton6_1_value)
        self.checkbutton6_2_value = tkinter.BooleanVar(self.frame)
        self.checkbutton6_2 = tkinter.ttk.Checkbutton(self.frame, text="このアドレスを使用する", command=self.Checkbutton6_2Command, variable=self.checkbutton6_2_value)

        self.checkbutton7_1_value = tkinter.BooleanVar(self.frame)
        self.checkbutton7_1 = tkinter.ttk.Checkbutton(self.frame, text="このアドレスを使用する", command=self.Checkbutton7_1Command, variable=self.checkbutton7_1_value)
        self.checkbutton7_2_value = tkinter.BooleanVar(self.frame)
        self.checkbutton7_2 = tkinter.ttk.Checkbutton(self.frame, text="このアドレスを使用する", command=self.Checkbutton7_2Command, variable=self.checkbutton7_2_value)

        self.checkbutton8_1_value = tkinter.BooleanVar(self.frame)
        self.checkbutton8_1 = tkinter.ttk.Checkbutton(self.frame, text="このアドレスを使用する", command=self.Checkbutton8_1Command, variable=self.checkbutton8_1_value)
        self.checkbutton8_2_value = tkinter.BooleanVar(self.frame)
        self.checkbutton8_2 = tkinter.ttk.Checkbutton(self.frame, text="このアドレスを使用する", command=self.Checkbutton8_2Command, variable=self.checkbutton8_2_value)

        self.checkbutton9_1_value = tkinter.BooleanVar(self.frame)
        self.checkbutton9_1 = tkinter.ttk.Checkbutton(self.frame, text="このアドレスを使用する", command=self.Checkbutton9_1Command, variable=self.checkbutton9_1_value)
        self.checkbutton9_2_value = tkinter.BooleanVar(self.frame)
        self.checkbutton9_2 = tkinter.ttk.Checkbutton(self.frame, text="このアドレスを使用する", command=self.Checkbutton9_2Command, variable=self.checkbutton9_2_value)

        self.checkbutton10_1_value = tkinter.BooleanVar(self.frame)
        self.checkbutton10_1 = tkinter.ttk.Checkbutton(self.frame, text="このアドレスを使用する", command=self.Checkbutton10_1Command, variable=self.checkbutton10_1_value)
        self.checkbutton10_2_value = tkinter.BooleanVar(self.frame)
        self.checkbutton10_2 = tkinter.ttk.Checkbutton(self.frame, text="このアドレスを使用する", command=self.Checkbutton10_2Command, variable=self.checkbutton10_2_value)

        self.label0_1 = tkinter.ttk.Label(self.frame, text="アドレス番号 ", font=font1)
        self.label0_2 = tkinter.ttk.Label(self.frame, text=" アドレスの使用 ", font=font1)
        self.label0_3 = tkinter.ttk.Label(self.frame, text=COMBOBOX_ENTRY_BETWEEN_WIDETH, font=font1)
        self.label0_4 = tkinter.ttk.Label(self.frame, text=" ポートの選択 ", font=font1)
        self.label0_5 = tkinter.ttk.Label(self.frame, text=LEFT_RIGHT_BETWEEN_WIDETH)

        self.label0_6 = tkinter.ttk.Label(self.frame, text="アドレス番号", font=font1)
        self.label0_7 = tkinter.ttk.Label(self.frame, text=" アドレスの使用 ", font=font1)
        self.label0_8 = tkinter.ttk.Label(self.frame, text=COMBOBOX_ENTRY_BETWEEN_WIDETH, font=font1)
        self.label0_9 = tkinter.ttk.Label(self.frame, text=" ポートの選択 ", font=font1)


        self.label1_1 = tkinter.ttk.Label(self.frame, text="アドレス   1 : ", font=font1)
        self.label1_2 = tkinter.ttk.Label(self.frame, text=COMBOBOX_ENTRY_BETWEEN_WIDETH, font=font1)

        self.label1_A = tkinter.ttk.Label(self.frame, text=LEFT_RIGHT_BETWEEN_WIDETH)

        self.label1_3 = tkinter.ttk.Label(self.frame, text="アドレス  11 : ", font=font1)
        self.label1_4 = tkinter.ttk.Label(self.frame, text=COMBOBOX_ENTRY_BETWEEN_WIDETH, font=font1)


        self.label2_1 = tkinter.ttk.Label(self.frame, text="アドレス   2 : ", font=font1)
        self.label2_2 = tkinter.ttk.Label(self.frame, text=COMBOBOX_ENTRY_BETWEEN_WIDETH, font=font1)

        self.label2_A = tkinter.ttk.Label(self.frame, text=LEFT_RIGHT_BETWEEN_WIDETH)

        self.label2_3 = tkinter.ttk.Label(self.frame, text="アドレス  12 : ", font=font1)
        self.label2_4 = tkinter.ttk.Label(self.frame, text=COMBOBOX_ENTRY_BETWEEN_WIDETH, font=font1)


        self.label3_1 = tkinter.ttk.Label(self.frame, text="アドレス   3 : ", font=font1)
        self.label3_2 = tkinter.ttk.Label(self.frame, text=COMBOBOX_ENTRY_BETWEEN_WIDETH, font=font1)

        self.label3_A = tkinter.ttk.Label(self.frame, text=LEFT_RIGHT_BETWEEN_WIDETH)

        self.label3_3 = tkinter.ttk.Label(self.frame, text="アドレス  13 : ", font=font1)
        self.label3_4 = tkinter.ttk.Label(self.frame, text=COMBOBOX_ENTRY_BETWEEN_WIDETH, font=font1)


        self.label4_1 = tkinter.ttk.Label(self.frame, text="アドレス   4 : ", font=font1)
        self.label4_2 = tkinter.ttk.Label(self.frame, text=COMBOBOX_ENTRY_BETWEEN_WIDETH, font=font1)

        self.label4_A = tkinter.ttk.Label(self.frame, text=LEFT_RIGHT_BETWEEN_WIDETH)

        self.label4_3 = tkinter.ttk.Label(self.frame, text="アドレス  14 : ", font=font1)
        self.label4_4 = tkinter.ttk.Label(self.frame, text=COMBOBOX_ENTRY_BETWEEN_WIDETH, font=font1)


        self.label5_1 = tkinter.ttk.Label(self.frame, text="アドレス   5 : ", font=font1)
        self.label5_2 = tkinter.ttk.Label(self.frame, text=COMBOBOX_ENTRY_BETWEEN_WIDETH, font=font1)

        self.label5_A = tkinter.ttk.Label(self.frame, text=LEFT_RIGHT_BETWEEN_WIDETH)

        self.label5_3 = tkinter.ttk.Label(self.frame, text="アドレス  15 : ", font=font1)
        self.label5_4 = tkinter.ttk.Label(self.frame, text=COMBOBOX_ENTRY_BETWEEN_WIDETH, font=font1)


        self.label6_1 = tkinter.ttk.Label(self.frame, text="アドレス   6 : ", font=font1)
        self.label6_2 = tkinter.ttk.Label(self.frame, text=COMBOBOX_ENTRY_BETWEEN_WIDETH, font=font1)

        self.label6_A = tkinter.ttk.Label(self.frame, text=LEFT_RIGHT_BETWEEN_WIDETH)

        self.label6_3 = tkinter.ttk.Label(self.frame, text="アドレス  16 : ", font=font1)
        self.label6_4 = tkinter.ttk.Label(self.frame, text=COMBOBOX_ENTRY_BETWEEN_WIDETH, font=font1)


        self.label7_1 = tkinter.ttk.Label(self.frame, text="アドレス   7 : ", font=font1)
        self.label7_2 = tkinter.ttk.Label(self.frame, text=COMBOBOX_ENTRY_BETWEEN_WIDETH, font=font1)

        self.label7_A = tkinter.ttk.Label(self.frame, text=LEFT_RIGHT_BETWEEN_WIDETH)

        self.label7_3 = tkinter.ttk.Label(self.frame, text="アドレス  17 : ", font=font1)
        self.label7_4 = tkinter.ttk.Label(self.frame, text=COMBOBOX_ENTRY_BETWEEN_WIDETH, font=font1)


        self.label8_1 = tkinter.ttk.Label(self.frame, text="アドレス   8 : ", font=font1)
        self.label8_2 = tkinter.ttk.Label(self.frame, text=COMBOBOX_ENTRY_BETWEEN_WIDETH, font=font1)

        self.label8_A = tkinter.ttk.Label(self.frame, text=LEFT_RIGHT_BETWEEN_WIDETH)

        self.label8_3 = tkinter.ttk.Label(self.frame, text="アドレス  18 : ", font=font1)
        self.label8_4 = tkinter.ttk.Label(self.frame, text=COMBOBOX_ENTRY_BETWEEN_WIDETH, font=font1)


        self.label9_1 = tkinter.ttk.Label(self.frame, text="アドレス   9 : ", font=font1)
        self.label9_2 = tkinter.ttk.Label(self.frame, text=COMBOBOX_ENTRY_BETWEEN_WIDETH, font=font1)

        self.label9_A = tkinter.ttk.Label(self.frame, text=LEFT_RIGHT_BETWEEN_WIDETH)

        self.label9_3 = tkinter.ttk.Label(self.frame, text="アドレス  19 : ", font=font1)
        self.label9_4 = tkinter.ttk.Label(self.frame, text=COMBOBOX_ENTRY_BETWEEN_WIDETH, font=font1)


        self.label10_1 = tkinter.ttk.Label(self.frame, text="アドレス  10 : ", font=font1)
        self.label10_2 = tkinter.ttk.Label(self.frame, text=COMBOBOX_ENTRY_BETWEEN_WIDETH, font=font1)

        self.label10_A = tkinter.ttk.Label(self.frame, text=LEFT_RIGHT_BETWEEN_WIDETH)

        self.label10_3 = tkinter.ttk.Label(self.frame, text="アドレス  20 : ", font=font1)
        self.label10_4 = tkinter.ttk.Label(self.frame, text=COMBOBOX_ENTRY_BETWEEN_WIDETH, font=font1)


        self.button1 = tkinter.ttk.Button(self.frame, text="完了", command=self.finish, width=10)
        self.button2 = tkinter.ttk.Button(self.frame, text="キャンセル", command=self.quitWindow, width=10)
        self.button3 = tkinter.ttk.Button(self.frame, text="ポート再読込み", command=self.ComboboxReload, width=14)

        self.checkbutton1_1.checkbutton1_1_value = self.checkbutton1_1_value

        self.hasMade = False
        

    def Checkbutton1_1Command(self):
        if (self.checkbutton1_1_value.get()):
            self.combobox1_1['state'] = 'normal'
        else :
            self.combobox1_1['state'] = 'disable'

    def Checkbutton1_2Command(self):
        if (self.checkbutton1_2_value.get()):
            self.combobox1_2['state'] = 'normal'
        else :
            self.combobox1_2['state'] = 'disable'
        

    def Checkbutton2_1Command(self):
        if (self.checkbutton2_1_value.get()):
            self.combobox2_1['state'] = 'normal'
        else :
            self.combobox2_1['state'] = 'disable'

    def Checkbutton2_2Command(self):
        if (self.checkbutton2_2_value.get()):
            self.combobox2_2['state'] = 'normal'
        else :
            self.combobox2_2['state'] = 'disable'
        

    def Checkbutton3_1Command(self):
        if (self.checkbutton3_1_value.get()):
            self.combobox3_1['state'] = 'normal'
        else :
            self.combobox3_1['state'] = 'disable'

    def Checkbutton3_2Command(self):
        if (self.checkbutton3_2_value.get()):
            self.combobox3_2['state'] = 'normal'
        else :
            self.combobox3_2['state'] = 'disable'
        

    def Checkbutton4_1Command(self):
        if (self.checkbutton4_1_value.get()):
            self.combobox4_1['state'] = 'normal'
        else :
            self.combobox4_1['state'] = 'disable'

    def Checkbutton4_2Command(self):
        if (self.checkbutton4_2_value.get()):
            self.combobox4_2['state'] = 'normal'
        else :
            self.combobox4_2['state'] = 'disable'
        

    def Checkbutton5_1Command(self):
        if (self.checkbutton5_1_value.get()):
            self.combobox5_1['state'] = 'normal'
        else :
            self.combobox5_1['state'] = 'disable'

    def Checkbutton5_2Command(self):
        if (self.checkbutton5_2_value.get()):
            self.combobox5_2['state'] = 'normal'
        else :
            self.combobox5_2['state'] = 'disable'
        

    def Checkbutton6_1Command(self):
        if (self.checkbutton6_1_value.get()):
            self.combobox6_1['state'] = 'normal'
        else :
            self.combobox6_1['state'] = 'disable'

    def Checkbutton6_2Command(self):
        if (self.checkbutton6_2_value.get()):
            self.combobox6_2['state'] = 'normal'
        else :
            self.combobox6_2['state'] = 'disable'
        

    def Checkbutton7_1Command(self):
        if (self.checkbutton7_1_value.get()):
            self.combobox7_1['state'] = 'normal'
        else :
            self.combobox7_1['state'] = 'disable'

    def Checkbutton7_2Command(self):
        if (self.checkbutton7_2_value.get()):
            self.combobox7_2['state'] = 'normal'
        else :
            self.combobox7_2['state'] = 'disable'
        

    def Checkbutton8_1Command(self):
        if (self.checkbutton8_1_value.get()):
            self.combobox8_1['state'] = 'normal'
        else :
            self.combobox8_1['state'] = 'disable'

    def Checkbutton8_2Command(self):
        if (self.checkbutton8_2_value.get()):
            self.combobox8_2['state'] = 'normal'
        else :
            self.combobox8_2['state'] = 'disable'
        

    def Checkbutton9_1Command(self):
        if (self.checkbutton9_1_value.get()):
            self.combobox9_1['state'] = 'normal'
        else :
            self.combobox9_1['state'] = 'disable'

    def Checkbutton9_2Command(self):
        if (self.checkbutton9_2_value.get()):
            self.combobox9_2['state'] = 'normal'
        else :
            self.combobox9_2['state'] = 'disable'
        

    def Checkbutton10_1Command(self):
        if (self.checkbutton10_1_value.get()):
            self.combobox10_1['state'] = 'normal'
        else :
            self.combobox10_1['state'] = 'disable'

    def Checkbutton10_2Command(self):
        if (self.checkbutton10_2_value.get()):
            self.combobox10_2['state'] = 'normal'
        else :
            self.combobox10_2['state'] = 'disable'
            
        
    def ComboboxReload(self):
        self.ComboboxList = portsRead()
        self.combobox1_1['values'] = self.ComboboxList
        self.combobox1_2['values'] = self.ComboboxList
        self.combobox2_1['values'] = self.ComboboxList
        self.combobox2_2['values'] = self.ComboboxList
        self.combobox3_1['values'] = self.ComboboxList
        self.combobox3_2['values'] = self.ComboboxList
        self.combobox4_1['values'] = self.ComboboxList
        self.combobox4_2['values'] = self.ComboboxList
        self.combobox5_1['values'] = self.ComboboxList
        self.combobox5_2['values'] = self.ComboboxList
        self.combobox6_1['values'] = self.ComboboxList
        self.combobox6_2['values'] = self.ComboboxList
        self.combobox7_1['values'] = self.ComboboxList
        self.combobox7_2['values'] = self.ComboboxList
        self.combobox8_1['values'] = self.ComboboxList
        self.combobox8_2['values'] = self.ComboboxList
        self.combobox9_1['values'] = self.ComboboxList
        self.combobox9_2['values'] = self.ComboboxList
        self.combobox10_1['values'] = self.ComboboxList
        self.combobox10_2['values'] = self.ComboboxList

    def startWindow(self):
        self.window2_2_frame.deiconify()
        self.frame.pack(fill=tkinter.BOTH, padx=1, pady=5)

        self.frame.grid(row=0, column=0)

        self.window2_2_frame.lift()
        self.window2_2_frame.maxsize(width=WINDOW2_2_WIDETH, height=WINDOW2_2_HEIGHT)
        self.window2_2_frame.minsize(width=WINDOW2_2_WIDETH, height=WINDOW2_2_HEIGHT)
        self.window2_2_frame.title(WINDOW2_2_TITEL)
        self.frame['bg'] = COLOR_WINDOW
        self.window2_2_frame['bg'] = COLOR_WINDOW

        
        if(self.hasMade == False):
            self.label0_1.grid(row=0, column=0)
            self.label0_2.grid(row=0, column=1)
            self.label0_3.grid(row=0, column=2)
            self.label0_4.grid(row=0, column=3)
            self.label0_5.grid(row=0, column=4)

            self.label0_6.grid(row=0, column=5)
            self.label0_7.grid(row=0, column=6)
            self.label0_8.grid(row=0, column=7)
            self.label0_9.grid(row=0, column=8)


            self.label1_1.grid(row=1, column=0)
            self.checkbutton1_1.grid(row=1, column=1)
            self.label1_2.grid(row=1, column=2)
            self.combobox1_1.grid(row=1, column=3)
            
            self.label1_A.grid(row=1, column=4)

            self.label1_3.grid(row=1, column=5)
            self.checkbutton1_2.grid(row=1, column=6)
            self.label1_4.grid(row=1, column=7)
            self.combobox1_2.grid(row=1, column=8)


            self.label2_1.grid(row=2, column=0)
            self.checkbutton2_1.grid(row=2, column=1)
            self.label2_2.grid(row=2, column=2)
            self.combobox2_1.grid(row=2, column=3)
            
            self.label2_A.grid(row=2, column=4)

            self.label2_3.grid(row=2, column=5)
            self.checkbutton2_2.grid(row=2, column=6)
            self.label2_4.grid(row=2, column=7)
            self.combobox2_2.grid(row=2, column=8)


            self.label3_1.grid(row=3, column=0)
            self.checkbutton3_1.grid(row=3, column=1)
            self.label3_2.grid(row=3, column=2)
            self.combobox3_1.grid(row=3, column=3)
            
            self.label3_A.grid(row=3, column=4)

            self.label3_3.grid(row=3, column=5)
            self.checkbutton3_2.grid(row=3, column=6)
            self.label3_4.grid(row=3, column=7)
            self.combobox3_2.grid(row=3, column=8)


            self.label4_1.grid(row=4, column=0)
            self.checkbutton4_1.grid(row=4, column=1)
            self.label4_2.grid(row=4, column=2)
            self.combobox4_1.grid(row=4, column=3)
            
            self.label4_A.grid(row=4, column=4)

            self.label4_3.grid(row=4, column=5)
            self.checkbutton4_2.grid(row=4, column=6)
            self.label4_4.grid(row=4, column=7)
            self.combobox4_2.grid(row=4, column=8)


            self.label5_1.grid(row=5, column=0)
            self.checkbutton5_1.grid(row=5, column=1)
            self.label5_2.grid(row=5, column=2)
            self.combobox5_1.grid(row=5, column=3)
            
            self.label5_A.grid(row=5, column=4)

            self.label5_3.grid(row=5, column=5)
            self.checkbutton5_2.grid(row=5, column=6)
            self.label5_4.grid(row=5, column=7)
            self.combobox5_2.grid(row=5, column=8)


            self.label6_1.grid(row=6, column=0)
            self.checkbutton6_1.grid(row=6, column=1)
            self.label6_2.grid(row=6, column=2)
            self.combobox6_1.grid(row=6, column=3)
            
            self.label6_A.grid(row=6, column=4)

            self.label6_3.grid(row=6, column=5)
            self.checkbutton6_2.grid(row=6, column=6)
            self.label6_4.grid(row=6, column=7)
            self.combobox6_2.grid(row=6, column=8)


            self.label7_1.grid(row=7, column=0)
            self.checkbutton7_1.grid(row=7, column=1)
            self.label7_2.grid(row=7, column=2)
            self.combobox7_1.grid(row=7, column=3)
            
            self.label7_A.grid(row=7, column=4)

            self.label7_3.grid(row=7, column=5)
            self.checkbutton7_2.grid(row=7, column=6)
            self.label7_4.grid(row=7, column=7)
            self.combobox7_2.grid(row=7, column=8)


            self.label8_1.grid(row=8, column=0)
            self.checkbutton8_1.grid(row=8, column=1)
            self.label8_2.grid(row=8, column=2)
            self.combobox8_1.grid(row=8, column=3)
            
            self.label8_A.grid(row=8, column=4)

            self.label8_3.grid(row=8, column=5)
            self.checkbutton8_2.grid(row=8, column=6)
            self.label8_4.grid(row=8, column=7)
            self.combobox8_2.grid(row=8, column=8)


            self.label9_1.grid(row=9, column=0)
            self.checkbutton9_1.grid(row=9, column=1)
            self.label9_2.grid(row=9, column=2)
            self.combobox9_1.grid(row=9, column=3)
            
            self.label9_A.grid(row=9, column=4)

            self.label9_3.grid(row=9, column=5)
            self.checkbutton9_2.grid(row=9, column=6)
            self.label9_4.grid(row=9, column=7)
            self.combobox9_2.grid(row=9, column=8)


            self.label10_1.grid(row=10, column=0)
            self.checkbutton10_1.grid(row=10, column=1)
            self.label10_2.grid(row=10, column=2)
            self.combobox10_1.grid(row=10, column=3)
            
            self.label10_A.grid(row=10, column=4)

            self.label10_3.grid(row=10, column=5)
            self.checkbutton10_2.grid(row=10, column=6)
            self.label10_4.grid(row=10, column=7)
            self.combobox10_2.grid(row=10, column=8)

            self.button1.grid(row=11, column=5)
            self.button2.grid(row=11, column=6)
            self.button3.grid(row=11, column=8)

        self.hasMade = True

    def savePort(self):
        if (self.checkbutton1_1_value.get()):
            portAddressRelationships[1] = self.combobox1_1.get()
        else:
            portAddressRelationships[1] = None
        if (self.checkbutton2_1_value.get()):
            portAddressRelationships[2] = self.combobox2_1.get()
        else:
            portAddressRelationships[2] = None
        if (self.checkbutton3_1_value.get()):
            portAddressRelationships[3] = self.combobox3_1.get()
        else:
            portAddressRelationships[3] = None
        if (self.checkbutton4_1_value.get()):
            portAddressRelationships[4] = self.combobox4_1.get()
        else:
            portAddressRelationships[4] = None
        if (self.checkbutton5_1_value.get()):
            portAddressRelationships[5] = self.combobox5_1.get()
        else:
            portAddressRelationships[5] = None
        if (self.checkbutton6_1_value.get()):
            portAddressRelationships[6] = self.combobox6_1.get()
        else:
            portAddressRelationships[6] = None
        if (self.checkbutton7_1_value.get()):
            portAddressRelationships[7] = self.combobox7_1.get()
        else:
            portAddressRelationships[7] = None
        if (self.checkbutton8_1_value.get()):
            portAddressRelationships[8] = self.combobox8_1.get()
        else:
            portAddressRelationships[8] = None
        if (self.checkbutton9_1_value.get()):
            portAddressRelationships[9] = self.combobox9_1.get()
        else:
            portAddressRelationships[9] = None
        if (self.checkbutton10_1_value.get()):
            portAddressRelationships[10] = self.combobox10_1.get()
        else:
            portAddressRelationships[10] = None

        if (self.checkbutton1_2_value.get()):
            portAddressRelationships[11] = self.combobox1_2.get()
        else:
            portAddressRelationships[11] = None
        if (self.checkbutton2_2_value.get()):
            portAddressRelationships[12] = self.combobox2_2.get()
        else:
            portAddressRelationships[12] = None
        if (self.checkbutton3_2_value.get()):
            portAddressRelationships[13] = self.combobox3_2.get()
        else:
            portAddressRelationships[13] = None
        if (self.checkbutton4_2_value.get()):
            portAddressRelationships[14] = self.combobox4_2.get()
        else:
            portAddressRelationships[14] = None
        if (self.checkbutton5_2_value.get()):
            portAddressRelationships[15] = self.combobox5_2.get()
        else:
            portAddressRelationships[15] = None
        if (self.checkbutton6_2_value.get()):
            portAddressRelationships[16] = self.combobox6_2.get()
        else:
            portAddressRelationships[16] = None
        if (self.checkbutton7_2_value.get()):
            portAddressRelationships[17] = self.combobox7_2.get()
        else:
            portAddressRelationships[17] = None
        if (self.checkbutton8_2_value.get()):
            portAddressRelationships[18] = self.combobox8_2.get()
        else:
            portAddressRelationships[18] = None
        if (self.checkbutton9_2_value.get()):
            portAddressRelationships[19] = self.combobox9_2.get()
        else:
            portAddressRelationships[19] = None
        if (self.checkbutton10_2_value.get()):
            portAddressRelationships[20] = self.combobox10_2.get()
        else:
            portAddressRelationships[20] = None

        self.window2_2_frame.withdraw()
        portAddressSettingCheckWindow.startWindow()
          
    def finish(self):
        result = tkinter.messagebox.askquestion(title="ポート・アドレス設定", message="この設定で保存しますか?")
        if(result == "yes"):
            self.window2_2_frame.withdraw()
            self.savePort()
        elif(result == "no"):
            pass

    def quitWindow(self):
        result = tkinter.messagebox.askquestion(title="ポート・アドレス設定", message="本当にキャンセルしますか?")

        if(result == "yes"):
            self.window2_2_frame.withdraw()
        elif(result == "no"):
            pass

#==============↑↑window2_2関係(ここまで)↑↑===============


#==============↓↓window2_3_関係(ここから)↓↓=============== #TODOwindow2_3_関係
class window2_3_Contens:
    def __init__(self):
        COMBOBOX_ENTRY_BETWEEN_WIDETH = "   "
        LEFT_RIGHT_BETWEEN_WIDETH =     "        "

        self.window2_3_frame = tkinter.Tk()
        self.frame = tkinter.Frame(self.window2_3_frame)
        self.window2_3_frame.protocol('WM_DELETE_WINDOW', self.quitWindow)
        self.window2_3_frame.withdraw()

        self.style = tkinter.ttk.Style(self.frame)

        self.style.configure("TLabel",
                             foreground=COLOR_LABEL_TEXT,
                             background=COLOR_LABEL_BACK
                             )

        self.style.configure("TScrollbar",
                             gripcount=0, 
                             background=COLOR_SCROOLBAR_BAR, 
                             darkcolor=COLOR_SCROOLBAR_BAR, 
                             lightcolor=COLOR_SCROOLBAR_BAR, 
                             troughcolor=COLOR_SCROOLBAR_BACK, 
                             bordercolor=COLOR_SCROOLBAR_BACK, 
                             arrowcolor=COLOR_SCROOLBAR_BAR
                            )
        
        self.style.configure("TButton",
                             padding=6,
                             relief="flat", 
                             background=COLOR_BUTTON_NORMAL_BACK, 
                             foreground=COLOR_BUTTON_NORMAL_TEXT, 
                             font=font1
                            )

        self.style.map("TButton",
                       foreground=[('pressed', '!disabled', COLOR_BUTTON_CLICK_TEXT), 
                                   ('disabled', COLOR_BUTTON_DISABLED_TEXT), 
                                   ('active', COLOR_BUTTON_TOUCH_TEXT)
                                  ],
                       background=[('pressed', '!disabled', COLOR_BUTTON_CLICK_BACK), 
                                   ('disabled', COLOR_BUTTON_DISABLED_BACK), 
                                   ('active', COLOR_BUTTON_TOUCH_BACK)
                                  ]
                    )

        self.entry1_1 = tkinter.Entry(self.frame, readonlybackground='#ff0000', fg='#ffffff', font=font1, relief="solid", bd=1, state='normal')
        self.entry1_2 = tkinter.Entry(self.frame, readonlybackground='#ff0000', fg='#ffffff', font=font1, relief="solid", bd=1, state='normal')
        self.entry2_1 = tkinter.Entry(self.frame, readonlybackground='#ff0000', fg='#ffffff', font=font1, relief="solid", bd=1, state='normal')
        self.entry2_2 = tkinter.Entry(self.frame, readonlybackground='#ff0000', fg='#ffffff', font=font1, relief="solid", bd=1, state='normal')
        self.entry3_1 = tkinter.Entry(self.frame, readonlybackground='#ff0000', fg='#ffffff', font=font1, relief="solid", bd=1, state='normal')
        self.entry3_2 = tkinter.Entry(self.frame, readonlybackground='#ff0000', fg='#ffffff', font=font1, relief="solid", bd=1, state='normal')
        self.entry4_1 = tkinter.Entry(self.frame, readonlybackground='#ff0000', fg='#ffffff', font=font1, relief="solid", bd=1, state='normal')
        self.entry4_2 = tkinter.Entry(self.frame, readonlybackground='#ff0000', fg='#ffffff', font=font1, relief="solid", bd=1, state='normal')
        self.entry5_1 = tkinter.Entry(self.frame, readonlybackground='#ff0000', fg='#ffffff', font=font1, relief="solid", bd=1, state='normal')
        self.entry5_2 = tkinter.Entry(self.frame, readonlybackground='#ff0000', fg='#ffffff', font=font1, relief="solid", bd=1, state='normal')
        self.entry6_1 = tkinter.Entry(self.frame, readonlybackground='#ff0000', fg='#ffffff', font=font1, relief="solid", bd=1, state='normal')
        self.entry6_2 = tkinter.Entry(self.frame, readonlybackground='#ff0000', fg='#ffffff', font=font1, relief="solid", bd=1, state='normal')
        self.entry7_1 = tkinter.Entry(self.frame, readonlybackground='#ff0000', fg='#ffffff', font=font1, relief="solid", bd=1, state='normal')
        self.entry7_2 = tkinter.Entry(self.frame, readonlybackground='#ff0000', fg='#ffffff', font=font1, relief="solid", bd=1, state='normal')
        self.entry8_1 = tkinter.Entry(self.frame, readonlybackground='#ff0000', fg='#ffffff', font=font1, relief="solid", bd=1, state='normal')
        self.entry8_2 = tkinter.Entry(self.frame, readonlybackground='#ff0000', fg='#ffffff', font=font1, relief="solid", bd=1, state='normal')
        self.entry9_1 = tkinter.Entry(self.frame, readonlybackground='#ff0000', fg='#ffffff', font=font1, relief="solid", bd=1, state='normal')
        self.entry9_2 = tkinter.Entry(self.frame, readonlybackground='#ff0000', fg='#ffffff', font=font1, relief="solid", bd=1, state='normal')
        self.entry10_1 = tkinter.Entry(self.frame, readonlybackground='#ff0000', fg='#ffffff', font=font1, relief="solid", bd=1, state='normal')
        self.entry10_2 = tkinter.Entry(self.frame, readonlybackground='#ff0000', fg='#ffffff', font=font1, relief="solid", bd=1, state='normal')

        self.entry1_1.insert(0, '使用しない')
        self.entry1_2.insert(0, '使用しない')
        self.entry2_1.insert(0, '使用しない')
        self.entry2_2.insert(0, '使用しない')
        self.entry3_1.insert(0, '使用しない')
        self.entry3_2.insert(0, '使用しない')
        self.entry4_1.insert(0, '使用しない')
        self.entry4_2.insert(0, '使用しない')
        self.entry5_1.insert(0, '使用しない')
        self.entry5_2.insert(0, '使用しない')
        self.entry6_1.insert(0, '使用しない')
        self.entry6_2.insert(0, '使用しない')
        self.entry7_1.insert(0, '使用しない')
        self.entry7_2.insert(0, '使用しない')
        self.entry8_1.insert(0, '使用しない')
        self.entry8_2.insert(0, '使用しない')
        self.entry9_1.insert(0, '使用しない')
        self.entry9_2.insert(0, '使用しない')
        self.entry10_1.insert(0, '使用しない')
        self.entry10_2.insert(0, '使用しない')

        self.entry1_1['state'] = 'readonly'
        self.entry1_2['state'] = 'readonly'

        self.label0_1 = tkinter.ttk.Label(self.frame, text="アドレス番号  ", font=font1)
        self.label0_3 = tkinter.ttk.Label(self.frame, text=COMBOBOX_ENTRY_BETWEEN_WIDETH, font=font1)
        self.label0_4 = tkinter.ttk.Label(self.frame, text=" 使用するポート ", font=font1)

        self.label0_5 = tkinter.ttk.Label(self.frame, text=LEFT_RIGHT_BETWEEN_WIDETH)

        self.label0_1 = tkinter.ttk.Label(self.frame, text="アドレス番号", font=font1)
        self.label0_3 = tkinter.ttk.Label(self.frame, text=COMBOBOX_ENTRY_BETWEEN_WIDETH, font=font1)
        self.label0_4 = tkinter.ttk.Label(self.frame, text=" 使用するポート ", font=font1)


        self.label1_1 = tkinter.ttk.Label(self.frame, text="アドレス   1 : ", font=font1)
        self.label1_2 = tkinter.ttk.Label(self.frame, text=COMBOBOX_ENTRY_BETWEEN_WIDETH, font=font1)

        self.label1_3 = tkinter.ttk.Label(self.frame, text=LEFT_RIGHT_BETWEEN_WIDETH, font=font1)

        self.label1_4 = tkinter.ttk.Label(self.frame, text="アドレス  11 : ", font=font1)
        self.label1_5 = tkinter.ttk.Label(self.frame, text=COMBOBOX_ENTRY_BETWEEN_WIDETH, font=font1)


        self.label2_1 = tkinter.ttk.Label(self.frame, text="アドレス   2 : ", font=font1)
        self.label2_2 = tkinter.ttk.Label(self.frame, text=COMBOBOX_ENTRY_BETWEEN_WIDETH, font=font1)

        self.label2_3 = tkinter.ttk.Label(self.frame, text=LEFT_RIGHT_BETWEEN_WIDETH, font=font1)

        self.label2_4 = tkinter.ttk.Label(self.frame, text="アドレス  12 : ", font=font1)
        self.label2_5 = tkinter.ttk.Label(self.frame, text=COMBOBOX_ENTRY_BETWEEN_WIDETH, font=font1)


        self.label3_1 = tkinter.ttk.Label(self.frame, text="アドレス   3 : ", font=font1)
        self.label3_2 = tkinter.ttk.Label(self.frame, text=COMBOBOX_ENTRY_BETWEEN_WIDETH, font=font1)

        self.label3_3 = tkinter.ttk.Label(self.frame, text=LEFT_RIGHT_BETWEEN_WIDETH, font=font1)

        self.label3_4 = tkinter.ttk.Label(self.frame, text="アドレス  13 : ", font=font1)
        self.label3_5 = tkinter.ttk.Label(self.frame, text=COMBOBOX_ENTRY_BETWEEN_WIDETH, font=font1)


        self.label4_1 = tkinter.ttk.Label(self.frame, text="アドレス   4 : ", font=font1)
        self.label4_2 = tkinter.ttk.Label(self.frame, text=COMBOBOX_ENTRY_BETWEEN_WIDETH, font=font1)

        self.label4_3 = tkinter.ttk.Label(self.frame, text=LEFT_RIGHT_BETWEEN_WIDETH, font=font1)

        self.label4_4 = tkinter.ttk.Label(self.frame, text="アドレス  14 : ", font=font1)
        self.label4_5 = tkinter.ttk.Label(self.frame, text=COMBOBOX_ENTRY_BETWEEN_WIDETH, font=font1)


        self.label5_1 = tkinter.ttk.Label(self.frame, text="アドレス   5 : ", font=font1)
        self.label5_2 = tkinter.ttk.Label(self.frame, text=COMBOBOX_ENTRY_BETWEEN_WIDETH, font=font1)

        self.label5_3 = tkinter.ttk.Label(self.frame, text=LEFT_RIGHT_BETWEEN_WIDETH, font=font1)

        self.label5_4 = tkinter.ttk.Label(self.frame, text="アドレス  15 : ", font=font1)
        self.label5_5 = tkinter.ttk.Label(self.frame, text=COMBOBOX_ENTRY_BETWEEN_WIDETH, font=font1)


        self.label6_1 = tkinter.ttk.Label(self.frame, text="アドレス   6 : ", font=font1)
        self.label6_2 = tkinter.ttk.Label(self.frame, text=COMBOBOX_ENTRY_BETWEEN_WIDETH, font=font1)

        self.label6_3 = tkinter.ttk.Label(self.frame, text=LEFT_RIGHT_BETWEEN_WIDETH, font=font1)

        self.label6_4 = tkinter.ttk.Label(self.frame, text="アドレス  16 : ", font=font1)
        self.label6_5 = tkinter.ttk.Label(self.frame, text=COMBOBOX_ENTRY_BETWEEN_WIDETH, font=font1)


        self.label7_1 = tkinter.ttk.Label(self.frame, text="アドレス   7 : ", font=font1)
        self.label7_2 = tkinter.ttk.Label(self.frame, text=COMBOBOX_ENTRY_BETWEEN_WIDETH, font=font1)

        self.label7_3 = tkinter.ttk.Label(self.frame, text=LEFT_RIGHT_BETWEEN_WIDETH, font=font1)

        self.label7_4 = tkinter.ttk.Label(self.frame, text="アドレス  17 : ", font=font1)
        self.label7_5 = tkinter.ttk.Label(self.frame, text=COMBOBOX_ENTRY_BETWEEN_WIDETH, font=font1)


        self.label8_1 = tkinter.ttk.Label(self.frame, text="アドレス   8 : ", font=font1)
        self.label8_2 = tkinter.ttk.Label(self.frame, text=COMBOBOX_ENTRY_BETWEEN_WIDETH, font=font1)

        self.label8_3 = tkinter.ttk.Label(self.frame, text=LEFT_RIGHT_BETWEEN_WIDETH, font=font1)

        self.label8_4 = tkinter.ttk.Label(self.frame, text="アドレス  18 : ", font=font1)
        self.label8_5 = tkinter.ttk.Label(self.frame, text=COMBOBOX_ENTRY_BETWEEN_WIDETH, font=font1)


        self.label9_1 = tkinter.ttk.Label(self.frame, text="アドレス   9 : ", font=font1)
        self.label9_2 = tkinter.ttk.Label(self.frame, text=COMBOBOX_ENTRY_BETWEEN_WIDETH, font=font1)

        self.label9_3 = tkinter.ttk.Label(self.frame, text=LEFT_RIGHT_BETWEEN_WIDETH, font=font1)

        self.label9_4 = tkinter.ttk.Label(self.frame, text="アドレス  19 : ", font=font1)
        self.label9_5 = tkinter.ttk.Label(self.frame, text=COMBOBOX_ENTRY_BETWEEN_WIDETH, font=font1)


        self.label10_1 = tkinter.ttk.Label(self.frame, text="アドレス  10 : ", font=font1)
        self.label10_2 = tkinter.ttk.Label(self.frame, text=COMBOBOX_ENTRY_BETWEEN_WIDETH, font=font1)

        self.label10_3 = tkinter.ttk.Label(self.frame, text=LEFT_RIGHT_BETWEEN_WIDETH, font=font1)

        self.label10_4 = tkinter.ttk.Label(self.frame, text="アドレス  20 : ", font=font1)
        self.label10_5 = tkinter.ttk.Label(self.frame, text=COMBOBOX_ENTRY_BETWEEN_WIDETH, font=font1)

        self.button1 = tkinter.ttk.Button(self.frame, text="完了", command=self.quitWindow, width=10)

        self.hasMade:bool = False

    def startWindow(self):
        self.window2_3_frame.deiconify()
        self.frame.pack(fill=tkinter.BOTH, padx=1, pady=5)

        self.frame.grid(row=0, column=0)

        self.window2_3_frame.lift()
        self.window2_3_frame.maxsize(width=WINDOW2_2_1_WIDETH, height=WINDOW2_2_1_HEIGHT)
        self.window2_3_frame.minsize(width=WINDOW2_2_1_WIDETH, height=WINDOW2_2_1_HEIGHT)
        self.window2_3_frame.title(WINDOW2_2_1_TITEL)
        self.frame['bg'] = COLOR_WINDOW
        self.window2_3_frame['bg'] = COLOR_WINDOW

        if(self.hasMade == False):
            self.label0_1.grid(row=0, column=0)
            self.label0_3.grid(row=0, column=1)
            self.label0_4.grid(row=0, column=2)

            self.label0_5.grid(row=0, column=3)

            self.label0_1.grid(row=0, column=4)
            self.label0_3.grid(row=0, column=5)
            self.label0_4.grid(row=0, column=6)


            self.label1_1.grid(row=1, column=0)
            self.label1_2.grid(row=1, column=1)
        
        if(portAddressRelationships[1] != None):
            self.entry1_1['state'] = 'normal'
            self.entry1_1['readonlybackground'] = '#adff2f'
            self.entry1_1['fg'] = '#000000'
            self.entry1_1.delete(0, tkinter.END)
            self.entry1_1.insert(0,portAddressRelationships[1])
            self.entry1_1['state'] ='readonly'
        else:
            self.entry1_1['state'] = 'normal'
            self.entry1_1['readonlybackground'] = '#ff0000'
            self.entry1_1['fg'] = '#ffffff'
            self.entry1_1.delete(0, tkinter.END)
            self.entry1_1.insert(0,'使用しない')
            self.entry1_1['state'] ='readonly'

        if(self.hasMade == False):
            self.entry1_1.grid(row=1, column=2)

            self.label1_3.grid(row=1, column=3)

            self.label1_4.grid(row=1, column=4)
        
        if(portAddressRelationships[11] != None):
            self.entry1_2['state'] = 'normal'
            self.entry1_2['readonlybackground'] = '#adff2f'
            self.entry1_2['fg'] = '#000000'
            self.entry1_2.delete(0, tkinter.END)
            self.entry1_2.insert(0,portAddressRelationships[11])
            self.entry1_2['state'] ='readonly'
        else:
            self.entry1_2['state'] = 'normal'
            self.entry1_2['readonlybackground'] = '#ff0000'
            self.entry1_2['fg'] = '#ffffff'
            self.entry1_2.delete(0, tkinter.END)
            self.entry1_2.insert(0,'使用しない')
            self.entry1_2['state'] ='readonly'

        if(self.hasMade == False):
            self.label1_5.grid(row=1, column=5)
            self.entry1_2.grid(row=1, column=6)


            self.label2_1.grid(row=2, column=0)
            self.label2_2.grid(row=2, column=1)
        
        if(portAddressRelationships[2] != None):
            self.entry2_1['state'] = 'normal'
            self.entry2_1['readonlybackground'] = '#adff2f'
            self.entry2_1['fg'] = '#000000'
            self.entry2_1.delete(0, tkinter.END)
            self.entry2_1.insert(0,portAddressRelationships[2])
            self.entry2_1['state'] ='readonly'
        else:
            self.entry2_1['state'] = 'normal'
            self.entry2_1['readonlybackground'] = '#ff0000'
            self.entry2_1['fg'] = '#ffffff'
            self.entry2_1.delete(0, tkinter.END)
            self.entry2_1.insert(0,'使用しない')
            self.entry2_1['state'] ='readonly'
        
        if(self.hasMade == False):
            self.entry2_1.grid(row=2, column=2)

            self.label2_3.grid(row=2, column=3)
            
            self.label2_4.grid(row=2, column=4)
        
        if(portAddressRelationships[12] != None):
            self.entry2_2['state'] = 'normal'
            self.entry2_2['readonlybackground'] = '#adff2f'
            self.entry2_2['fg'] = '#000000'
            self.entry2_2.delete(0, tkinter.END)
            self.entry2_2.insert(0,portAddressRelationships[12])
            self.entry2_2['state'] ='readonly'
        else:
            self.entry2_2['state'] = 'normal'
            self.entry2_2['readonlybackground'] = '#ff0000'
            self.entry2_2['fg'] = '#ffffff'
            self.entry2_2.delete(0, tkinter.END)
            self.entry2_2.insert(0,'使用しない')
            self.entry2_2['state'] ='readonly'

        if(self.hasMade == False):
            self.label2_5.grid(row=2, column=5)
            self.entry2_2.grid(row=2, column=6)


            self.label3_1.grid(row=3, column=0)
            self.label3_2.grid(row=3, column=1)

        if(portAddressRelationships[3] != None):
            self.entry3_1['state'] = 'normal'
            self.entry3_1['readonlybackground'] = '#adff2f'
            self.entry3_1['fg'] = '#000000'
            self.entry3_1.delete(0, tkinter.END)
            self.entry3_1.insert(0,portAddressRelationships[3])
            self.entry3_1['state'] ='readonly'
        else:
            self.entry3_1['state'] = 'normal'
            self.entry3_1['readonlybackground'] = '#ff0000'
            self.entry3_1['fg'] = '#ffffff'
            self.entry3_1.delete(0, tkinter.END)
            self.entry3_1.insert(0,'使用しない')
            self.entry3_1['state'] ='readonly'

        if(self.hasMade == False):
            self.entry3_1.grid(row=3, column=2)

            self.label3_3.grid(row=3, column=3)
            
            self.label3_4.grid(row=3, column=4)
        
        if(portAddressRelationships[13] != None):
            self.entry3_2['state'] = 'normal'
            self.entry3_2['readonlybackground'] = '#adff2f'
            self.entry3_2['fg'] = '#000000'
            self.entry3_2.delete(0, tkinter.END)
            self.entry3_2.insert(0,portAddressRelationships[13])
            self.entry3_2['state'] ='readonly'
        else:
            self.entry3_2['state'] = 'normal'
            self.entry3_2['readonlybackground'] = '#ff0000'
            self.entry3_2['fg'] = '#ffffff'
            self.entry3_2.delete(0, tkinter.END)
            self.entry3_2.insert(0,'使用しない')
            self.entry3_2['state'] ='readonly'

        if(self.hasMade == False):
            self.label3_5.grid(row=3, column=5)
            self.entry3_2.grid(row=3, column=6)


            self.label4_1.grid(row=4, column=0)
            self.label4_2.grid(row=4, column=1)
        
        if(portAddressRelationships[4] != None):
            self.entry4_1['state'] = 'normal'
            self.entry4_1['readonlybackground'] = '#adff2f'
            self.entry4_1['fg'] = '#000000'
            self.entry4_1.delete(0, tkinter.END)
            self.entry4_1.insert(0,portAddressRelationships[4])
            self.entry4_1['state'] ='readonly'
        else:
            self.entry4_1['state'] = 'normal'
            self.entry4_1['readonlybackground'] = '#ff0000'
            self.entry4_1['fg'] = '#ffffff'
            self.entry4_1.delete(0, tkinter.END)
            self.entry4_1.insert(0,'使用しない')
            self.entry4_1['state'] ='readonly'

        if(self.hasMade == False):
            self.entry4_1.grid(row=4, column=2)

            self.label4_3.grid(row=4, column=3)
            
            self.label4_4.grid(row=4, column=4)
        
        if(portAddressRelationships[14] != None):
            self.entry4_2['state'] = 'normal'
            self.entry4_2['readonlybackground'] = '#adff2f'
            self.entry4_2['fg'] = '#000000'
            self.entry4_2.delete(0, tkinter.END)
            self.entry4_2.insert(0,portAddressRelationships[14])
            self.entry4_2['state'] ='readonly'
        else:
            self.entry4_2['state'] = 'normal'
            self.entry4_2['readonlybackground'] = '#ff0000'
            self.entry4_2['fg'] = '#ffffff'
            self.entry4_2.delete(0, tkinter.END)
            self.entry4_2.insert(0,'使用しない')
            self.entry4_2['state'] ='readonly'

        if(self.hasMade == False):
            self.label4_5.grid(row=4, column=5)
            self.entry4_2.grid(row=4, column=6)


            self.label5_1.grid(row=5, column=0)
            self.label5_2.grid(row=5, column=1)
        
        if(portAddressRelationships[5] != None):
            self.entry5_1['state'] = 'normal'
            self.entry5_1['readonlybackground'] = '#adff2f'
            self.entry5_1['fg'] = '#000000'
            self.entry5_1.delete(0, tkinter.END)
            self.entry5_1.insert(0,portAddressRelationships[5])
            self.entry5_1['state'] ='readonly'
        else:
            self.entry5_1['state'] = 'normal'
            self.entry5_1['readonlybackground'] = '#ff0000'
            self.entry5_1['fg'] = '#ffffff'
            self.entry5_1.delete(0, tkinter.END)
            self.entry5_1.insert(0,'使用しない')
            self.entry5_1['state'] ='readonly'
        
        if(self.hasMade == False):
            self.entry5_1.grid(row=5, column=2)

            self.label5_3.grid(row=5, column=3)
            
            self.label5_4.grid(row=5, column=4)
        
        if(portAddressRelationships[15] != None):
            self.entry5_2['state'] = 'normal'
            self.entry5_2['readonlybackground'] = '#adff2f'
            self.entry5_2['fg'] = '#000000'
            self.entry5_2.delete(0, tkinter.END)
            self.entry5_2.insert(0,portAddressRelationships[15])
            self.entry5_2['state'] ='readonly'
        else:
            self.entry5_2['state'] = 'normal'
            self.entry5_2['readonlybackground'] = '#ff0000'
            self.entry5_2['fg'] = '#ffffff'
            self.entry5_2.delete(0, tkinter.END)
            self.entry5_2.insert(0,'使用しない')
            self.entry5_2['state'] ='readonly'

        if(self.hasMade == False):
            self.label5_5.grid(row=5, column=5)
            self.entry5_2.grid(row=5, column=6)


            self.label6_1.grid(row=6, column=0)
            self.label6_2.grid(row=6, column=1)
        
        if(portAddressRelationships[6] != None):
            self.entry6_1['state'] = 'normal'
            self.entry6_1['readonlybackground'] = '#adff2f'
            self.entry6_1['fg'] = '#000000'
            self.entry6_1.delete(0, tkinter.END)
            self.entry6_1.insert(0,portAddressRelationships[6])
            self.entry6_1['state'] ='readonly'
        else:
            self.entry6_1['state'] = 'normal'
            self.entry6_1['readonlybackground'] = '#ff0000'
            self.entry6_1['fg'] = '#ffffff'
            self.entry6_1.delete(0, tkinter.END)
            self.entry6_1.insert(0,'使用しない')
            self.entry6_1['state'] ='readonly'

        if(self.hasMade == False):
            self.entry6_1.grid(row=6, column=2)

            self.label6_3.grid(row=6, column=3)
            
            self.label6_4.grid(row=6, column=4)
        
        if(portAddressRelationships[16] != None):
            self.entry6_2['state'] = 'normal'
            self.entry6_2['readonlybackground'] = '#adff2f'
            self.entry6_2['fg'] = '#000000'
            self.entry6_2.delete(0, tkinter.END)
            self.entry6_2.insert(0,portAddressRelationships[16])
            self.entry6_2['state'] ='readonly'
        else:
            self.entry6_2['state'] = 'normal'
            self.entry6_2['readonlybackground'] = '#ff0000'
            self.entry6_2['fg'] = '#ffffff'
            self.entry6_2.delete(0, tkinter.END)
            self.entry6_2.insert(0,'使用しない')
            self.entry6_2['state'] ='readonly'

        if(self.hasMade == False):
            self.label6_5.grid(row=6, column=5)
            self.entry6_2.grid(row=6, column=6)


            self.label7_1.grid(row=7, column=0)
            self.label7_2.grid(row=7, column=1)
        
        if(portAddressRelationships[7] != None):
            self.entry7_1['state'] = 'normal'
            self.entry7_1['readonlybackground'] = '#adff2f'
            self.entry7_1['fg'] = '#000000'
            self.entry7_1.delete(0, tkinter.END)
            self.entry7_1.insert(0,portAddressRelationships[7])
            self.entry7_1['state'] ='readonly'
        else:
            self.entry7_1['state'] = 'normal'
            self.entry7_1['readonlybackground'] = '#ff0000'
            self.entry7_1['fg'] = '#ffffff'
            self.entry7_1.delete(0, tkinter.END)
            self.entry7_1.insert(0,'使用しない')
            self.entry7_1['state'] ='readonly'

        if(self.hasMade == False):
            self.entry7_1.grid(row=7, column=2)

            self.label7_3.grid(row=7, column=3)
            
            self.label7_4.grid(row=7, column=4)
        
        if(portAddressRelationships[17] != None):
            self.entry7_2['state'] = 'normal'
            self.entry7_2['readonlybackground'] = '#adff2f'
            self.entry7_2['fg'] = '#000000'
            self.entry7_2.delete(0, tkinter.END)
            self.entry7_2.insert(0,portAddressRelationships[17])
            self.entry7_2['state'] ='readonly'
        else:
            self.entry7_2['state'] = 'normal'
            self.entry7_2['readonlybackground'] = '#ff0000'
            self.entry7_2['fg'] = '#ffffff'
            self.entry7_2.delete(0, tkinter.END)
            self.entry7_2.insert(0,'使用しない')
            self.entry7_2['state'] ='readonly'

        if(self.hasMade == False):
            self.label7_5.grid(row=7, column=5)
            self.entry7_2.grid(row=7, column=6)


            self.label8_1.grid(row=8, column=0)
            self.label8_2.grid(row=8, column=1)
        
        if(portAddressRelationships[8] != None):
            self.entry8_1['state'] = 'normal'
            self.entry8_1['readonlybackground'] = '#adff2f'
            self.entry8_1['fg'] = '#000000'
            self.entry8_1.delete(0, tkinter.END)
            self.entry8_1.insert(0,portAddressRelationships[8])
            self.entry8_1['state'] ='readonly'
        else:
            self.entry8_1['state'] = 'normal'
            self.entry8_1['readonlybackground'] = '#ff0000'
            self.entry8_1['fg'] = '#ffffff'
            self.entry8_1.delete(0, tkinter.END)
            self.entry8_1.insert(0,'使用しない')
            self.entry8_1['state'] ='readonly'

        if(self.hasMade == False):
            self.entry8_1.grid(row=8, column=2)

            self.label8_3.grid(row=8, column=3)
            
            self.label8_4.grid(row=8, column=4)
        
        if(portAddressRelationships[18] != None):
            self.entry8_2['state'] = 'normal'
            self.entry8_2['readonlybackground'] = '#adff2f'
            self.entry8_2['fg'] = '#000000'
            self.entry8_2.delete(0, tkinter.END)
            self.entry8_2.insert(0,portAddressRelationships[18])
            self.entry8_2['state'] ='readonly'
        else:
            self.entry8_2['state'] = 'normal'
            self.entry8_2['readonlybackground'] = '#ff0000'
            self.entry8_2['fg'] = '#ffffff'
            self.entry8_2.delete(0, tkinter.END)
            self.entry8_2.insert(0,'使用しない')
            self.entry8_2['state'] ='readonly'

        if(self.hasMade == False):
            self.label8_5.grid(row=8, column=5)
            self.entry8_2.grid(row=8, column=6)


            self.label9_1.grid(row=9, column=0)
            self.label9_2.grid(row=9, column=1)
        
        if(portAddressRelationships[9] != None):
            self.entry9_1['state'] = 'normal'
            self.entry9_1['readonlybackground'] = '#adff2f'
            self.entry9_1['fg'] = '#000000'
            self.entry9_1.delete(0, tkinter.END)
            self.entry9_1.insert(0,portAddressRelationships[9])
            self.entry9_1['state'] ='readonly'
        else:
            self.entry9_1['state'] = 'normal'
            self.entry9_1['readonlybackground'] = '#ff0000'
            self.entry9_1['fg'] = '#ffffff'
            self.entry9_1.delete(0, tkinter.END)
            self.entry9_1.insert(0,'使用しない')
            self.entry9_1['state'] ='readonly'

        if(self.hasMade == False):
            self.entry9_1.grid(row=9, column=2)

            self.label9_3.grid(row=9, column=3)
            
            self.label9_4.grid(row=9, column=4)
        
        if(portAddressRelationships[19] != None):
            self.entry9_2['state'] = 'normal'
            self.entry9_2['readonlybackground'] = '#adff2f'
            self.entry9_2['fg'] = '#000000'
            self.entry9_2.delete(0, tkinter.END)
            self.entry9_2.insert(0,portAddressRelationships[19])
            self.entry9_2['state'] ='readonly'
        else:
            self.entry9_2['state'] = 'normal'
            self.entry9_2['readonlybackground'] = '#ff0000'
            self.entry9_2['fg'] = '#ffffff'
            self.entry9_2.delete(0, tkinter.END)
            self.entry9_2.insert(0,'使用しない')
            self.entry9_2['state'] ='readonly'

        if(self.hasMade == False):
            self.label9_5.grid(row=9, column=5)
            self.entry9_2.grid(row=9, column=6)


            self.label10_1.grid(row=10, column=0)
            self.label10_2.grid(row=10, column=1)
        
        if(portAddressRelationships[10] != None):
            self.entry10_1['state'] = 'normal'
            self.entry10_1['readonlybackground'] = '#adff2f'
            self.entry10_1['fg'] = '#000000'
            self.entry10_1.delete(0, tkinter.END)
            self.entry10_1.insert(0,portAddressRelationships[10])
            self.entry10_1['state'] ='readonly'
        else:
            self.entry10_1['state'] = 'normal'
            self.entry10_1['readonlybackground'] = '#ff0000'
            self.entry10_1['fg'] = '#ffffff'
            self.entry10_1.delete(0, tkinter.END)
            self.entry10_1.insert(0,'使用しない')
            self.entry10_1['state'] ='readonly'
        
        if(self.hasMade == False):
            self.entry10_1.grid(row=10, column=2)

            self.label10_3.grid(row=10, column=3)
            
            self.label10_4.grid(row=10, column=4)

        if(portAddressRelationships[20] != None):
            self.entry10_2['state'] = 'normal'
            self.entry10_2['readonlybackground'] = '#adff2f'
            self.entry10_2['fg'] = '#000000'
            self.entry10_2.delete(0, tkinter.END)
            self.entry10_2.insert(0,portAddressRelationships[20])
            self.entry10_2['state'] ='readonly'
        else:
            self.entry10_2['state'] = 'normal'
            self.entry10_2['readonlybackground'] = '#ff0000'
            self.entry10_2['fg'] = '#ffffff'
            self.entry10_2.delete(0, tkinter.END)
            self.entry10_2.insert(0,'使用しない')
            self.entry10_2['state'] ='readonly'
        
        if(self.hasMade == False):
            self.label10_5.grid(row=10, column=5)
            self.entry10_2.grid(row=10, column=6)

            self.button1.grid(row=11, column=6)
        
        self.hasMade = True
    
    def setWindow1Widgets(self):
        mainWindow.listbox1_1['state'] = "normal"
        mainWindow.listbox1_2['state'] = "normal"
        mainWindow.listbox1_3['state'] = "normal"
        mainWindow.listbox1_4['state'] = "normal"
        mainWindow.listbox1_5['state'] = "normal"
        mainWindow.listbox1_6['state'] = "normal"
        
        mainWindow.listbox2_1['state'] = "normal"
        mainWindow.listbox2_2['state'] = "normal"
        mainWindow.listbox2_3['state'] = "normal"
        mainWindow.listbox2_4['state'] = "normal"
        mainWindow.listbox2_5['state'] = "normal"
        mainWindow.listbox2_6['state'] = "normal"
        
        mainWindow.listbox3_1['state'] = "normal"
        mainWindow.listbox3_2['state'] = "normal"
        mainWindow.listbox3_3['state'] = "normal"
        mainWindow.listbox3_4['state'] = "normal"
        mainWindow.listbox3_5['state'] = "normal"
        mainWindow.listbox3_6['state'] = "normal"
        
        mainWindow.listbox4_1['state'] = "normal"
        mainWindow.listbox4_2['state'] = "normal"
        mainWindow.listbox4_3['state'] = "normal"
        mainWindow.listbox4_4['state'] = "normal"
        mainWindow.listbox4_5['state'] = "normal"
        mainWindow.listbox4_6['state'] = "normal"
        
        mainWindow.listbox5_1['state'] = "normal"
        mainWindow.listbox5_2['state'] = "normal"
        mainWindow.listbox5_3['state'] = "normal"
        mainWindow.listbox5_4['state'] = "normal"
        mainWindow.listbox5_5['state'] = "normal"
        mainWindow.listbox5_6['state'] = "normal"
        
        mainWindow.listbox6_1['state'] = "normal"
        mainWindow.listbox6_2['state'] = "normal"
        mainWindow.listbox6_3['state'] = "normal"
        mainWindow.listbox6_4['state'] = "normal"
        mainWindow.listbox6_5['state'] = "normal"
        mainWindow.listbox6_6['state'] = "normal"
        
        mainWindow.listbox7_1['state'] = "normal"
        mainWindow.listbox7_2['state'] = "normal"
        mainWindow.listbox7_3['state'] = "normal"
        mainWindow.listbox7_4['state'] = "normal"
        mainWindow.listbox7_5['state'] = "normal"
        mainWindow.listbox7_6['state'] = "normal"
        
        mainWindow.listbox8_1['state'] = "normal"
        mainWindow.listbox8_2['state'] = "normal"
        mainWindow.listbox8_3['state'] = "normal"
        mainWindow.listbox8_4['state'] = "normal"
        mainWindow.listbox8_5['state'] = "normal"
        mainWindow.listbox8_6['state'] = "normal"
        
        mainWindow.listbox9_1['state'] = "normal"
        mainWindow.listbox9_2['state'] = "normal"
        mainWindow.listbox9_3['state'] = "normal"
        mainWindow.listbox9_4['state'] = "normal"
        mainWindow.listbox9_5['state'] = "normal"
        mainWindow.listbox9_6['state'] = "normal"
        
        mainWindow.listbox10_1['state'] = "normal"
        mainWindow.listbox10_2['state'] = "normal"
        mainWindow.listbox10_3['state'] = "normal"
        mainWindow.listbox10_4['state'] = "normal"
        mainWindow.listbox10_5['state'] = "normal"
        mainWindow.listbox10_6['state'] = "normal"

        mainWindow.listboxA_1['state'] = "normal"
        mainWindow.buttonA_2['state'] = "normal"
        mainWindow.buttonA_3['state'] = "normal"
        mainWindow.buttonA_4['state'] = "disable"
        mainWindow.buttonA_5['state'] = "disable"

        if(portAddressRelationships[1] == None):
            mainWindow.entry1_1['state'] = "normal"
            mainWindow.entry1_1.delete(0, tkinter.END)
            mainWindow.entry1_1.insert(tkinter.END, "使用しない")
            mainWindow.entry1_1['fg'] = "#000000"
            mainWindow.entry1_1['state'] = "disable"
        else:
            mainWindow.entry1_1['state'] = "normal"
            mainWindow.entry1_1.delete(0, tkinter.END)
            mainWindow.entry1_1.insert(tkinter.END, str(portAddressRelationships[1]))
            mainWindow.entry1_1['fg'] = "#000000"
            mainWindow.entry1_1['readonlybackground'] = "#ffd900"
            mainWindow.entry1_1['state'] = "readonly"
        if(portAddressRelationships[2] == None):
            mainWindow.entry2_1['state'] = "normal"
            mainWindow.entry2_1.delete(0, tkinter.END)
            mainWindow.entry2_1.insert(tkinter.END, "使用しない")
            mainWindow.entry2_1['fg'] = "#000000"
            mainWindow.entry2_1['state'] = "disable"
        else:
            mainWindow.entry2_1['state'] = "normal"
            mainWindow.entry2_1.delete(0, tkinter.END)
            mainWindow.entry2_1.insert(tkinter.END, str(portAddressRelationships[2]))
            mainWindow.entry2_1['fg'] = "#000000"
            mainWindow.entry2_1['readonlybackground'] = "#ffd900"
            mainWindow.entry2_1['state'] = "readonly"
        if(portAddressRelationships[3] == None):
            mainWindow.entry3_1['state'] = "normal"
            mainWindow.entry3_1.delete(0, tkinter.END)
            mainWindow.entry3_1.insert(tkinter.END, "使用しない")
            mainWindow.entry3_1['fg'] = "#000000"
            mainWindow.entry3_1['state'] = "disable"
        else:
            mainWindow.entry3_1['state'] = "normal"
            mainWindow.entry3_1.delete(0, tkinter.END)
            mainWindow.entry3_1.insert(tkinter.END, str(portAddressRelationships[3]))
            mainWindow.entry3_1['fg'] = "#000000"
            mainWindow.entry3_1['readonlybackground'] = "#ffd900"
            mainWindow.entry3_1['state'] = "readonly"
        if(portAddressRelationships[4] == None):
            mainWindow.entry4_1['state'] = "normal"
            mainWindow.entry4_1.delete(0, tkinter.END)
            mainWindow.entry4_1.insert(tkinter.END, "使用しない")
            mainWindow.entry4_1['fg'] = "#000000"
            mainWindow.entry4_1['state'] = "disable"
        else:
            mainWindow.entry4_1['state'] = "normal"
            mainWindow.entry4_1.delete(0, tkinter.END)
            mainWindow.entry4_1.insert(tkinter.END, str(portAddressRelationships[4]))
            mainWindow.entry4_1['fg'] = "#000000"
            mainWindow.entry4_1['readonlybackground'] = "#ffd900"
            mainWindow.entry4_1['state'] = "readonly"
        if(portAddressRelationships[5] == None):
            mainWindow.entry5_1['state'] = "normal"
            mainWindow.entry5_1.delete(0, tkinter.END)
            mainWindow.entry5_1.insert(tkinter.END, "使用しない")
            mainWindow.entry5_1['fg'] = "#000000"
            mainWindow.entry5_1['state'] = "disable"
        else:
            mainWindow.entry5_1['state'] = "normal"
            mainWindow.entry5_1.delete(0, tkinter.END)
            mainWindow.entry5_1.insert(tkinter.END, str(portAddressRelationships[5]))
            mainWindow.entry5_1['fg'] = "#000000"
            mainWindow.entry5_1['readonlybackground'] = "#ffd900"
            mainWindow.entry5_1['state'] = "readonly"
        if(portAddressRelationships[6] == None):
            mainWindow.entry6_1['state'] = "normal"
            mainWindow.entry6_1.delete(0, tkinter.END)
            mainWindow.entry6_1.insert(tkinter.END, "使用しない")
            mainWindow.entry6_1['fg'] = "#000000"
            mainWindow.entry6_1['state'] = "disable"
        else:
            mainWindow.entry6_1['state'] = "normal"
            mainWindow.entry6_1.delete(0, tkinter.END)
            mainWindow.entry6_1.insert(tkinter.END, str(portAddressRelationships[6]))
            mainWindow.entry6_1['fg'] = "#000000"
            mainWindow.entry6_1['readonlybackground'] = "#ffd900"
            mainWindow.entry6_1['state'] = "readonly"
        if(portAddressRelationships[7] == None):
            mainWindow.entry7_1['state'] = "normal"
            mainWindow.entry7_1.delete(0, tkinter.END)
            mainWindow.entry7_1.insert(tkinter.END, "使用しない")
            mainWindow.entry7_1['fg'] = "#000000"
            mainWindow.entry7_1['state'] = "disable"
        else:
            mainWindow.entry7_1['state'] = "normal"
            mainWindow.entry7_1.delete(0, tkinter.END)
            mainWindow.entry7_1.insert(tkinter.END, str(portAddressRelationships[7]))
            mainWindow.entry7_1['fg'] = "#000000"
            mainWindow.entry7_1['readonlybackground'] = "#ffd900"
            mainWindow.entry7_1['state'] = "readonly"
        if(portAddressRelationships[8] == None):
            mainWindow.entry8_1['state'] = "normal"
            mainWindow.entry8_1.delete(0, tkinter.END)
            mainWindow.entry8_1.insert(tkinter.END, "使用しない")
            mainWindow.entry8_1['fg'] = "#000000"
            mainWindow.entry8_1['state'] = "disable"
        else:
            mainWindow.entry8_1['state'] = "normal"
            mainWindow.entry8_1.delete(0, tkinter.END)
            mainWindow.entry8_1.insert(tkinter.END, str(portAddressRelationships[8]))
            mainWindow.entry8_1['fg'] = "#000000"
            mainWindow.entry8_1['readonlybackground'] = "#ffd900"
            mainWindow.entry8_1['state'] = "readonly"
        if(portAddressRelationships[9] == None):
            mainWindow.entry9_1['state'] = "normal"
            mainWindow.entry9_1.delete(0, tkinter.END)
            mainWindow.entry9_1.insert(tkinter.END, "使用しない")
            mainWindow.entry9_1['fg'] = "#000000"
            mainWindow.entry9_1['state'] = "disable"
        else:
            mainWindow.entry9_1['state'] = "normal"
            mainWindow.entry9_1.delete(0, tkinter.END)
            mainWindow.entry9_1.insert(tkinter.END, str(portAddressRelationships[9]))
            mainWindow.entry9_1['fg'] = "#000000"
            mainWindow.entry9_1['readonlybackground'] = "#ffd900"
            mainWindow.entry9_1['state'] = "readonly"
        if(portAddressRelationships[10] == None):
            mainWindow.entry10_1['state'] = "normal"
            mainWindow.entry10_1.delete(0, tkinter.END)
            mainWindow.entry10_1.insert(tkinter.END, "使用しない")
            mainWindow.entry10_1['fg'] = "#000000"
            mainWindow.entry10_1['state'] = "disable"
        else:
            mainWindow.entry10_1['state'] = "normal"
            mainWindow.entry10_1.delete(0, tkinter.END)
            mainWindow.entry10_1.insert(tkinter.END, str(portAddressRelationships[10]))
            mainWindow.entry10_1['fg'] = "#000000"
            mainWindow.entry10_1['readonlybackground'] = "#ffd900"
            mainWindow.entry10_1['state'] = "readonly"
            

        if(portAddressRelationships[11] == None):
            mainWindow.entry1_2['state'] = "normal"
            mainWindow.entry1_2.delete(0, tkinter.END)
            mainWindow.entry1_2.insert(tkinter.END, "使用しない")
            mainWindow.entry1_2['fg'] = "#000000"
            mainWindow.entry1_2['state'] = "disable"
        else:
            mainWindow.entry1_2['state'] = "normal"
            mainWindow.entry1_2.delete(0, tkinter.END)
            mainWindow.entry1_2.insert(tkinter.END, str(portAddressRelationships[11]))
            mainWindow.entry1_2['fg'] = "#000000"
            mainWindow.entry1_2['readonlybackground'] = "#ffd900"
            mainWindow.entry1_2['state'] = "readonly"
        if(portAddressRelationships[12] == None):
            mainWindow.entry2_2['state'] = "normal"
            mainWindow.entry2_2.delete(0, tkinter.END)
            mainWindow.entry2_2.insert(tkinter.END, "使用しない")
            mainWindow.entry2_2['fg'] = "#000000"
            mainWindow.entry2_2['state'] = "disable"
        else:
            mainWindow.entry2_2['state'] = "normal"
            mainWindow.entry2_2.delete(0, tkinter.END)
            mainWindow.entry2_2.insert(tkinter.END, str(portAddressRelationships[12]))
            mainWindow.entry2_2['fg'] = "#000000"
            mainWindow.entry2_2['readonlybackground'] = "#ffd900"
            mainWindow.entry2_2['state'] = "readonly"
        if(portAddressRelationships[13] == None):
            mainWindow.entry3_2['state'] = "normal"
            mainWindow.entry3_2.delete(0, tkinter.END)
            mainWindow.entry3_2.insert(tkinter.END, "使用しない")
            mainWindow.entry3_2['fg'] = "#000000"
            mainWindow.entry3_2['state'] = "disable"
        else:
            mainWindow.entry3_2['state'] = "normal"
            mainWindow.entry3_2.delete(0, tkinter.END)
            mainWindow.entry3_2.insert(tkinter.END, str(portAddressRelationships[13]))
            mainWindow.entry3_2['fg'] = "#000000"
            mainWindow.entry3_2['readonlybackground'] = "#ffd900"
            mainWindow.entry3_2['state'] = "readonly"
        if(portAddressRelationships[14] == None):
            mainWindow.entry4_2['state'] = "normal"
            mainWindow.entry4_2.delete(0, tkinter.END)
            mainWindow.entry4_2.insert(tkinter.END, "使用しない")
            mainWindow.entry4_2['fg'] = "#000000"
            mainWindow.entry4_2['state'] = "disable"
        else:
            mainWindow.entry4_2['state'] = "normal"
            mainWindow.entry4_2.delete(0, tkinter.END)
            mainWindow.entry4_2.insert(tkinter.END, str(portAddressRelationships[14]))
            mainWindow.entry4_2['fg'] = "#000000"
            mainWindow.entry4_2['readonlybackground'] = "#ffd900"
            mainWindow.entry4_2['state'] = "readonly"
        if(portAddressRelationships[15] == None):
            mainWindow.entry5_2['state'] = "normal"
            mainWindow.entry5_2.delete(0, tkinter.END)
            mainWindow.entry5_2.insert(tkinter.END, "使用しない")
            mainWindow.entry5_2['fg'] = "#000000"
            mainWindow.entry5_2['state'] = "disable"
        else:
            mainWindow.entry5_2['state'] = "normal"
            mainWindow.entry5_2.delete(0, tkinter.END)
            mainWindow.entry5_2.insert(tkinter.END, str(portAddressRelationships[15]))
            mainWindow.entry5_2['fg'] = "#000000"
            mainWindow.entry5_2['readonlybackground'] = "#ffd900"
            mainWindow.entry5_2['state'] = "readonly"
        if(portAddressRelationships[16] == None):
            mainWindow.entry6_2['state'] = "normal"
            mainWindow.entry6_2.delete(0, tkinter.END)
            mainWindow.entry6_2.insert(tkinter.END, "使用しない")
            mainWindow.entry6_2['fg'] = "#000000"
            mainWindow.entry6_2['state'] = "disable"
        else:
            mainWindow.entry6_2['state'] = "normal"
            mainWindow.entry6_2.delete(0, tkinter.END)
            mainWindow.entry6_2.insert(tkinter.END, str(portAddressRelationships[16]))
            mainWindow.entry6_2['fg'] = "#000000"
            mainWindow.entry6_2['readonlybackground'] = "#ffd900"
            mainWindow.entry6_2['state'] = "readonly"
        if(portAddressRelationships[17] == None):
            mainWindow.entry7_2['state'] = "normal"
            mainWindow.entry7_2.delete(0, tkinter.END)
            mainWindow.entry7_2.insert(tkinter.END, "使用しない")
            mainWindow.entry7_2['fg'] = "#000000"
            mainWindow.entry7_2['state'] = "disable"
        else:
            mainWindow.entry7_2['state'] = "normal"
            mainWindow.entry7_2.delete(0, tkinter.END)
            mainWindow.entry7_2.insert(tkinter.END, str(portAddressRelationships[17]))
            mainWindow.entry7_2['fg'] = "#000000"
            mainWindow.entry7_2['readonlybackground'] = "#ffd900"
            mainWindow.entry7_2['state'] = "readonly"
        if(portAddressRelationships[18] == None):
            mainWindow.entry8_2['state'] = "normal"
            mainWindow.entry8_2.delete(0, tkinter.END)
            mainWindow.entry8_2.insert(tkinter.END, "使用しない")
            mainWindow.entry8_2['fg'] = "#000000"
            mainWindow.entry8_2['state'] = "disable"
        else:
            mainWindow.entry8_2['state'] = "normal"
            mainWindow.entry8_2.delete(0, tkinter.END)
            mainWindow.entry8_2.insert(tkinter.END, str(portAddressRelationships[18]))
            mainWindow.entry8_2['fg'] = "#000000"
            mainWindow.entry8_2['readonlybackground'] = "#ffd900"
            mainWindow.entry8_2['state'] = "readonly"
        if(portAddressRelationships[19] == None):
            mainWindow.entry9_2['state'] = "normal"
            mainWindow.entry9_2.delete(0, tkinter.END)
            mainWindow.entry9_2.insert(tkinter.END, "使用しない")
            mainWindow.entry9_2['fg'] = "#000000"
            mainWindow.entry9_2['state'] = "disable"
        else:
            mainWindow.entry9_2['state'] = "normal"
            mainWindow.entry9_2.delete(0, tkinter.END)
            mainWindow.entry9_2.insert(tkinter.END, str(portAddressRelationships[19]))
            mainWindow.entry9_2['fg'] = "#000000"
            mainWindow.entry9_2['readonlybackground'] = "#ffd900"
            mainWindow.entry9_2['state'] = "readonly"
        if(portAddressRelationships[20] == None):
            mainWindow.entry10_2['state'] = "normal"
            mainWindow.entry10_2.delete(0, tkinter.END)
            mainWindow.entry10_2.insert(tkinter.END, "使用しない")
            mainWindow.entry10_2['fg'] = "#000000"
            mainWindow.entry10_2['state'] = "disable"
        else:
            mainWindow.entry10_2['state'] = "normal"
            mainWindow.entry10_2.delete(0, tkinter.END)
            mainWindow.entry10_2.insert(tkinter.END, str(portAddressRelationships[20]))
            mainWindow.entry10_2['fg'] = "#000000"
            mainWindow.entry10_2['readonlybackground'] = "#ffd900"
            mainWindow.entry10_2['state'] = "readonly"
    
    def quitWindow(self):
        self.setWindow1Widgets()
        self.window2_3_frame.withdraw()

#==============↑↑window2_3_関係(ここまで)↑↑===============


#==============↓↓serial関係(ここから)↓↓=============== #TODOserial関係
class systemSerial:
    def startSerial(self):
        
        _portStartCondition:bool = [False] * 21

        for _i in range(1, 21, 1):
            if(portAddressRelationships[_i] != None):
                _portStartCondition[_i] = programsys.addressProgram[_i]._serial.begin()

                mainWindow.logPrint(_i, _portStartCondition[_i], "start communication")

        mainWindow.logPrint(0, True, "start all comunications")
            
#==============↑↑serial関係(ここまで)↑↑===============


#==============↓↓UserProgram関係(ここから)↓↓=============== #TODOUserProgram関係
class userPrograms:
    def startUserProgram(self):
        self.addressProgram = [ addMain.program(),
                                add1.program(portAddressRelationships[1]),
                                add2.program(portAddressRelationships[2]),
                                add3.program(portAddressRelationships[3]),
                                add4.program(portAddressRelationships[4]),
                                add5.program(portAddressRelationships[5]),
                                add6.program(portAddressRelationships[6]),
                                add7.program(portAddressRelationships[7]),
                                add8.program(portAddressRelationships[8]),
                                add9.program(portAddressRelationships[9]),
                                add10.program(portAddressRelationships[10]),
                                add11.program(portAddressRelationships[11]),
                                add12.program(portAddressRelationships[12]),
                                add13.program(portAddressRelationships[13]),
                                add14.program(portAddressRelationships[14]),
                                add15.program(portAddressRelationships[15]),
                                add16.program(portAddressRelationships[16]),
                                add17.program(portAddressRelationships[17]),
                                add18.program(portAddressRelationships[18]),
                                add19.program(portAddressRelationships[19]),
                                add20.program(portAddressRelationships[20])
                              ]
        
        self.addressThread = [  threading.Thread(target=self._userProgram),
                                threading.Thread(target=self._address1Program),
                                threading.Thread(target=self._address2Program),
                                threading.Thread(target=self._address3Program),
                                threading.Thread(target=self._address4Program),
                                threading.Thread(target=self._address5Program),
                                threading.Thread(target=self._address6Program),
                                threading.Thread(target=self._address7Program),
                                threading.Thread(target=self._address8Program),
                                threading.Thread(target=self._address9Program),
                                threading.Thread(target=self._address10Program),
                                threading.Thread(target=self._address11Program),
                                threading.Thread(target=self._address12Program),
                                threading.Thread(target=self._address13Program),
                                threading.Thread(target=self._address14Program),
                                threading.Thread(target=self._address15Program),
                                threading.Thread(target=self._address16Program),
                                threading.Thread(target=self._address17Program),
                                threading.Thread(target=self._address18Program),
                                threading.Thread(target=self._address19Program),
                                threading.Thread(target=self._address20Program),
                              ]
        
        for _i in range(1, 21, 1):
            if (portAddressRelationships[_i] != None):
                self.addressThread[_i].start()
                mainWindow.logPrint(_i, True, "start thread")
            
        self.addressThread[0].start()
        mainWindow.logPrint(0, True, "start user program thread")    
        
        mainWindow.logPrint(0, True, "start all thread")


    def _address1Program(self):
        self.addressProgram[1]._setup()
        
        while Ditel_DROS_Kernel.threadCondition:
            self.addressProgram[1]._loop()
            time.sleep(0.01)

    def _address2Program(self):
        self.addressProgram[2]._setup()
        
        while Ditel_DROS_Kernel.threadCondition:
            self.addressProgram[2]._loop()
            time.sleep(0.01)

    def _address3Program(self):
        self.addressProgram[3]._setup()
        
        while Ditel_DROS_Kernel.threadCondition:
            self.addressProgram[3]._loop()
            time.sleep(0.01)

    def _address4Program(self):
        self.addressProgram[4]._setup()
        
        while Ditel_DROS_Kernel.threadCondition:
            self.addressProgram[4]._loop()
            time.sleep(0.01)

    def _address5Program(self):
        self.addressProgram[5]._setup()
        
        while Ditel_DROS_Kernel.threadCondition:
            self.addressProgram[5]._loop()
            time.sleep(0.01)

    def _address6Program(self):
        self.addressProgram[6]._setup()
        
        while Ditel_DROS_Kernel.threadCondition:
            self.addressProgram[6]._loop()
            time.sleep(0.01)

    def _address7Program(self):
        self.addressProgram[7]._setup()
        
        while Ditel_DROS_Kernel.threadCondition:
            self.addressProgram[7]._loop()
            time.sleep(0.01)

    def _address8Program(self):
        self.addressProgram[8]._setup()
        
        while Ditel_DROS_Kernel.threadCondition:
            self.addressProgram[8]._loop()
            time.sleep(0.01)

    def _address9Program(self):
        self.addressProgram[9]._setup()
        
        while Ditel_DROS_Kernel.threadCondition:
            self.addressProgram[9]._loop()
            time.sleep(0.01)

    def _address10Program(self):
        self.addressProgram[10]._setup()
        
        while Ditel_DROS_Kernel.threadCondition:
            self.addressProgram[10]._loop()
            time.sleep(0.01)

    
    def _address11Program(self):
        self.addressProgram[11]._setup()
        
        while Ditel_DROS_Kernel.threadCondition:
            self.addressProgram[11]._loop()
            time.sleep(0.01)

    def _address12Program(self):
        self.addressProgram[12]._setup()
        
        while Ditel_DROS_Kernel.threadCondition:
            self.addressProgram[12]._loop()
            time.sleep(0.01)

    def _address13Program(self):
        self.addressProgram[13]._setup()
        
        while Ditel_DROS_Kernel.threadCondition:
            self.addressProgram[13]._loop()
            time.sleep(0.01)

    def _address14Program(self):
        self.addressProgram[14]._setup()
        
        while Ditel_DROS_Kernel.threadCondition:
            self.addressProgram[14]._loop()
            time.sleep(0.01)

    def _address15Program(self):
        self.addressProgram[15]._setup()
        
        while Ditel_DROS_Kernel.threadCondition:
            self.addressProgram[15]._loop()
            time.sleep(0.01)

    def _address16Program(self):
        self.addressProgram[16]._setup()
        
        while Ditel_DROS_Kernel.threadCondition:
            self.addressProgram[16]._loop()
            time.sleep(0.01)

    def _address17Program(self):
        self.addressProgram[17]._setup()
        
        while Ditel_DROS_Kernel.threadCondition:
            self.addressProgram[17]._loop()
            time.sleep(0.01)

    def _address18Program(self):
        self.addressProgram[18]._setup()
        
        while Ditel_DROS_Kernel.threadCondition:
            self.addressProgram[18]._loop()
            time.sleep(0.01)

    def _address19Program(self):
        self.addressProgram[19]._setup()
        
        while Ditel_DROS_Kernel.threadCondition:
            self.addressProgram[19]._loop()
            time.sleep(0.01)

    def _address20Program(self):
        self.addressProgram[20]._setup()
        
        while Ditel_DROS_Kernel.threadCondition:
            self.addressProgram[20]._loop()
            time.sleep(0.01)

    def _userProgram(self):
        self.addressProgram[0]._setup()

        while Ditel_DROS_Kernel.threadCondition:
            self.addressProgram[0]._loop()
            time.sleep(0.01)
        
#==============↑↑UserProgram関係(ここまで)↑↑===============


#==============↓↓bypass関係(ここから)↓↓=============== #TODObypass関係
class _bypass:
    def __init__(self):
        self._bypassThread = threading.Thread(target=self._bypassSetRead)

    def _bypassSetRead(self):
        while Ditel_DROS_Kernel.threadCondition:
            for _i in range(1, 21, 1):
                if(portAddressRelationships[_i] != None):
                    try:
                        Ditel_System_Bypass.bypass[_i].readData = programsys.addressProgram[_i]._serial.read()
                        Ditel_System_Bypass.bypass[_i].avaiableData = programsys.addressProgram[_i]._serial.avaiable()
                    except:
                        pass
                    
                    try:
                        if(Ditel_System_Bypass.bypass[_i].requestSendData == True):
                            programsys.addressProgram[_i]._serial.send(Ditel_System_Bypass.bypass[_i].sendData)
                            Ditel_System_Bypass.bypass[_i].requestSendData = False
                    except:
                        pass
                    
            time.sleep(0.001)

    def _bypassStart(self):
        self._bypassThread.start()

#==============↑↑bypass関係(ここまで)↑↑===============


#==============↓↓emergency関係(ここから)↓↓=============== #TODOemergency関係
class _emergency:
    def __init__(self):
        self.emergencySendData:int = [HEAD_WORD, COMMAND_DECLARE_EMERGENCY, NO_SEND_DATA, NO_SEND_DATA, NO_SEND_DATA, NO_SEND_DATA]
        self.emergencySendResult:str = None
        self._emergencyThread = threading.Thread(target=self._stateRead)

    def _stateRead(self):
        while Ditel_DROS_Kernel.threadCondition:
            time.sleep(0.001)
            if(Ditel_DROS_Kernel.addressWhereSendEmergency != 0):
                break
        
        if ((Ditel_DROS_Kernel.addressWhereSendEmergency != 0) and Ditel_DROS_Kernel.threadCondition):
            for _i in range(1, 21, 1):
                try:
                    if(Ditel_DROS_Kernel.addressWhereSendEmergency != _i):
                        if(programsys.addressProgram[_i]._serial.send(self.emergencySendData)):
                            self.emergencySendResult = "orange"
                        else:
                            self.emergencySendResult = "#ff0000"
                    else:
                        self.emergencySendResult = "orange"
                    
                    if(self.emergencySendResult == "orange"):
                        mainWindow.logPrint(_i, True, "send1 of emergency declaration")
                    elif(self.emergencySendResult == "#ff0000"):
                        mainWindow.logPrint(_i, False, "send2 of emergency declaration")

                except:
                    mainWindow.logPrint(_i, False, "send3 of emergency declaration")
                    self.emergencySendResult = "#ff0000"
                
                match _i:
                    case 1:
                        mainWindow.entry1_1['readonlybackground'] = self.emergencySendResult
                    case 2:
                        mainWindow.entry2_1['readonlybackground'] = self.emergencySendResult
                    case 3:
                        mainWindow.entry3_1['readonlybackground'] = self.emergencySendResult
                    case 4:
                        mainWindow.entry4_1['readonlybackground'] = self.emergencySendResult
                    case 5:
                        mainWindow.entry5_1['readonlybackground'] = self.emergencySendResult
                    case 6:
                        mainWindow.entry6_1['readonlybackground'] = self.emergencySendResult
                    case 7:
                        mainWindow.entry7_1['readonlybackground'] = self.emergencySendResult
                    case 8:
                        mainWindow.entry8_1['readonlybackground'] = self.emergencySendResult
                    case 9:
                        mainWindow.entry9_1['readonlybackground'] = self.emergencySendResult
                    case 10:
                        mainWindow.entry10_1['readonlybackground'] = self.emergencySendResult
                    case 11:
                        mainWindow.entry1_2['readonlybackground'] = self.emergencySendResult
                    case 12:
                        mainWindow.entry2_2['readonlybackground'] = self.emergencySendResult
                    case 13:
                        mainWindow.entry3_2['readonlybackground'] = self.emergencySendResult
                    case 14:
                        mainWindow.entry4_2['readonlybackground'] = self.emergencySendResult
                    case 15:
                        mainWindow.entry5_2['readonlybackground'] = self.emergencySendResult
                    case 16:
                        mainWindow.entry6_2['readonlybackground'] = self.emergencySendResult
                    case 17:
                        mainWindow.entry7_2['readonlybackground'] = self.emergencySendResult
                    case 18:
                        mainWindow.entry8_2['readonlybackground'] = self.emergencySendResult
                    case 19:
                        mainWindow.entry9_2['readonlybackground'] = self.emergencySendResult
                    case 20:
                        mainWindow.entry10_2['readonlybackground'] = self.emergencySendResult

            mainWindow.logPrint(0, True, "start main emergency program")
            programsys.addressProgram[0]._emergencyProgram()
            
    def _startStateRead(self):
        self._emergencyThread.start()

#==============↑↑emergency関係(ここまで)↑↑===============

mainWindow = window1_Contents()

portAddressSettingWindow = window2_Contents()

portAddressAutoSettingWindow = window2_1_Contens()

portAddressManualSettingWindow = window2_2_Contents()
portAddressSettingCheckWindow = window2_3_Contens()

serialsys = systemSerial()
programsys = userPrograms()
bypasssys = _bypass()
emergencysys = _emergency()

print('[  OK  ] start DROS  |  version : ' + VERSION)

mainWindow.startWindow()
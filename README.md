# Ditel Robot Operating System
<img height="250" alt="SCR-20230502-nedr" src="https://github.com/Ditel252/Ditel_DROS/assets/144299935/45f37016-6d3d-4a88-886d-9e7ff3ba8dc7">

## 概要
Ditel Robot Operating System (以降DROS)はシリアル通信を用いた複数マイコン操縦ソフトです.


## 使用する前に
DROSではMaster側及びSlave側でライブラリを使用しているため, それぞれ使用する前にしなければならないことがあります. 使用する前に下記の手順に従ってソフトの構成を行ってください.<br>
※本説明文ではプログラムの作成にVisual Studio Codeを使用していることを前提としています.
1. ソフトの入手<br>
    [DROSの配布場所](https://github.com/Ditel252/Ditel_DROS)にアクセスして`CODE`>`Download Zip`をクリックして最新版のDROSをダウンロードしてください.
1. .zipの展開<br>
    Ctrl+Alt+Tを押しターミナルを開き, 以下のコマンドを実行してください.<br>
    `$ cd ~/ダウンロード`<br>
    `$ ls Ditel_DROS-master.zip`<br>
    上記のコマンドを実行したあと`Ditel_DROS-master.zip`が表示されることを確認してください.<br>
    `$ unzip Ditel_DROS-master.zip`<br>
    `$ cd Ditel_DROS-master`<br>
    上記のコマンドを実行して.zipを展開して展開したディレクトリ内に移動してください. <br>
    ※以降このディレクトリの場所を`$DROS`と表記します.<br>
1. Master側の構成<br>
    DROSのMaster側のソフトはpython言語で構成されているため, ソフトを動かすためには予めpython及びいくつかのライブラリーをインストールする必要があります.以下の手順に沿って必要なソフトのインストールを行ってください.<br>
    `$ cd $DROS/Master`<br>
    `$ chmod +x Ditel_DROS_Configuratio_Program.sh`<br>
    `$ ./Ditel_DROS_Configuratio_Program.sh`<br>
    上記のコマンドを実行してください. 処理が終了したことを確認したら<br>
    `$ python3 Ditel_DROS.py`<br>
    を実行し, 正常に動作することを確認してください.<br>
1. Slave側の構成<br>
    Platform ioのHomeに移動し`New Project`を選択して使用するマイコンを選択してください. ここで`Framework`では必ず`Arduino`を選択してください.<br>
    `Project Wizard`が終了したら再びPlatform ioのHomeに移動し, 左のメニューバーから`Libraries`を選択し`Search libraries`の欄に`STM32duino FreeRTOS`と入力しEnterキーを押して, 一番上に出できたライブラリを選択し"Add to Project"で作成したプロジェクトにライブラリを追加してください.<br>
    上記の手順が終了したら, 作成したプロジェクトディレクトリに移動し, `src`という名前のディレクトリを削除し, `$DROS/Slave`にある`src`ディレクトリをコピーしてきて, 作成したプロジェクトディレクトリに貼り付けてください.<br>
    以上の手順が終了したら, Buildを実行して, 正常にコンパイルできることを確認してください.<br>

## DROSの使用方法
### Master側
#### <span style="font-size:10pt;">ソフトウィンドウの操作方法</span>
<details>
<summary>説明</summary>
※最初に下記のコマンドを実行して, Master側のプログラムがあるディレクトリに移動してください.<br>

`$ cd $HOME/Master`<br><br>
DORSのMaster側のソフトは以下のコマンド<br>
`$ python3 Ditel_DROS.py`<br>
を実行することで起動することができます.<br>
起動すると次のようなウィンドウが開きます.<br>
<img height="250" alt="SCR-20230502-nedr" src="https://github.com/Ditel252/Ditel_DROS/assets/144299935/ef43bf51-a855-490f-979b-4271baf9f4a3"><br>
ここでMaster側の操作は下の5つのボタンのみで行います.<br>
<img height="200" alt="SCR-20230502-nedr" src="https://github.com/Ditel252/Ditel_DROS/assets/144299935/052594f3-0634-4329-9eeb-43f42a118605"><br>
通信開始までの処理は以下の手順を踏むことで実行できます.
1. 通信を行うマイコンの設定<br>
    まず最初にマイコンのアドレスを設定します.<br>
    <img height="200" alt="SCR-20230502-nedr" src="https://github.com/Ditel252/Ditel_DROS/assets/144299935/052594f3-0634-4329-9eeb-43f42a118605"><br>
    ポート設定を選択すると,下のようなウィンドウが表示されます.<br>
    <img height="200" alt="SCR-20230502-nedr" src="https://github.com/Ditel252/Ditel_DROS/assets/144299935/02c01c58-9e57-464c-9fca-a84c010cb386"><br>
    ※ここでは"自動で設定する"方を選択した場合の操作方法のみ説明します.<br>
    "自動で設定する"を選択してください. すると下のようなウィンドウが表示されるので"完了"を選択してください.<br>
    <img height="350" alt="SCR-20230502-nedr" src="https://github.com/Ditel252/Ditel_DROS/assets/144299935/04f042e2-0a60-4d1c-ab5d-5b0c9dabbecf"><br>
    すると, 以下のようなウィンドウが表示されます.<br>
    <img height="350" alt="SCR-20230502-nedr" src="https://github.com/Ditel252/Ditel_DROS/assets/144299935/c923d24c-3b15-4238-9a9e-088a3c62c5da"><br>
    ここで"アドレス 1:"などは繋がれているマイコンに設定されたアドレス番号を表しており, 使用するポートはそれぞれのマイコンがどのポートを使用しているかを表しています.<br>
    アドレスとポートの組み合わせを確認したら"完了"を選択してください.<br>
    <img height="350" alt="SCR-20230502-nedr" src="https://github.com/Ditel252/Ditel_DROS/assets/144299935/1e849335-98f7-4c00-a0fd-4a2d7ff53284"><br>
    するとウィンドウが閉じられ, 最初のウィンドウのみが表示されます. 上の画像からもわかるとおり, 先程設定したアドレスは使用するポートが表示されているのに対して, 設定されていないアドレスについては"使用しない"という表示がされています.<br>
    以上で通信を行うマイコンの設定は完了です.<br><br>
1. 通信の開始<br>
    <img height="200" alt="SCR-20230502-nedr" src="https://github.com/Ditel252/Ditel_DROS/assets/144299935/69b03ad2-9882-47c1-b6c8-7281f58b832a"><br>
    操作ボタンを見ると上の画像のように"終了"が使用できなくなっている代わりに"ポート設定の確認", "通信開始"が使用できるようになっています.<br>
    ここで"ポート設定"は"1. 通信を行うマイコンの設定"と同様の処理を行う機能で, "ポート設定の確認"は下のウィンドウを表示する機能です.<br>
    <img height="350" alt="SCR-20230502-nedr" src="https://github.com/Ditel252/Ditel_DROS/assets/144299935/c923d24c-3b15-4238-9a9e-088a3c62c5da"><br>
    対して"通信開始"は通信を開始する機能です.これを選択すると,下のウィンドウが表示されます.<br>
    <img height="200" alt="SCR-20230502-nedr" src="https://github.com/Ditel252/Ditel_DROS/assets/144299935/7a16c813-b07b-4202-9b12-0a71287c3983"><br>
    ここで"Yes"を選択した瞬間に各マイコンに通信開始のコマンドが送信され, "User_Programs"ディレクトリ内のプログラムの処理が開始します.<br>
    "YES"を選択すると, 上の画像のウィンドウが閉じ, 下の画像のように最初のウィンドウのみが表示されます.<br>
    <img height="350" alt="SCR-20230502-nedr" src="https://github.com/Ditel252/Ditel_DROS/assets/144299935/29140717-8541-498b-9a6c-5d965025f86c"><br>
    使用しているアドレスの部分を拡大してみると下の写真のようになります.<br>
    <img height="350" alt="SCR-20230502-nedr" src="https://github.com/Ditel252/Ditel_DROS/assets/144299935/6356bf27-12b3-46f7-9732-dca3d2d21bfe"><br>
    ここで"アドレスのRX"はパソコン側が受信したデータの内容, "アドレスのTX"はパソコン側が送信したデータの内容, "アドレスのログ"はそれぞれのアドレスで行われた処理のログを表しています.<br>
1. 通信の終了<br>
    通信を開始すると"操作ボタン"は下の画像のように"通信終了"のみを選択できるようになります.<br>
    <img height="200" alt="SCR-20230502-nedr" src="https://github.com/Ditel252/Ditel_DROS/assets/144299935/45c1b968-7334-4d14-8099-5bee5d45ee98"><br>
    "通信終了"を選択すると, 下のウィンドウが表示されます.<br>
    <img height="200" alt="SCR-20230502-nedr" src="https://github.com/Ditel252/Ditel_DROS/assets/144299935/dd121530-ff36-4fc5-afb4-76f81c9743fd"><br>
    ここで"Yes"を選択した瞬間に各マイコンに通信終了のコマンドが送信され, "User_Programs"ディレクトリ内のプログラムの処理が停止します.<br>
    "YES"を選択すると, 上の画像のウィンドウが閉じ, 下の画像のように最初のウィンドウのみが表示されます.<br>
    <img height="350" alt="SCR-20230502-nedr" src="https://github.com/Ditel252/Ditel_DROS/assets/144299935/b07e5176-fcda-4a14-bade-023eb6092571"><br>
    上の画像のように"全体のログ"に`[  OK  ] finish all thread stopping`の表示があれば通信処理の終了は正常に実行されています.<br>
    ※もし`[  OK  ] finish all thread stopping`の表示がなければDROSがクラッシュしている可能性があるため, ターミナルを閉じ強制的にDROSを停止させてください.<br>
1. DROSの終了<br>
    <img height="200" alt="SCR-20230502-nedr" src="https://github.com/Ditel252/Ditel_DROS/assets/144299935/fcce2633-1d65-48cb-9478-744aa994c11c"><br>
    "3. 通信の終了"の操作を適切に実行すると上の画像のように"操作ボタン"は"終了"のみ選択できるようになります.<br>
    ここで"終了"を選択する, もしくはウィンドウの閉じるボタンをクリックすることでDROSを終了することができます.
</details>

### Slave側

## Master関数一覧
### _serial.系列
各アドレスのファイル内ではそのアドレスに対して下記の関数を使用することが可能です.
|関数名|仮引数|返り値|返り値の説明|
|------|------|------|------|
|`send()`|"bytes型のリスト"|"bool型"|送信が成功したか|
|`sendCommand()`|"bytes型の変数"|"bool型"|送信が成功したか|
|`sendInt()`|"bytes型の変数","int型の変数"|"bool型"|送信が成功したか|
|`read()`|(なし)|"bytes型のリスト"|Slaveから受信した要素数6のリスト|
|`readCommand()`|(なし)|"bytes型"|Slaveから受信したコマンド|
|`readInt()`|(なし)|"int型のリスト"|Slaveから受信したコマンドとint型のデータ|
|`avaiable()`|(なし)|"bool型"|Slaveから受信されたデータがあるか|
|`stateOfEmergency()`|(なし)|"bool型"|異常事態が宣言されているか|
|`convertToInt()`|"bytes型のリスト|"int型のリスト"|readInt()で読み取ったデータに変換|
|`logPrint()`|"bool型の変数","str型の変数"|(なし)|アドレスのログに文字列を表示する|
|`unconditional()`|(なし)|"bool型"|無条件ループが許可されているか|

<br>

#### <span style="font-size:14pt;">_serial.send()</span>
<details>
<summary>説明</summary>

仮引数に入力された要素数6のbytes型のリストを送信します.<br>
|内容|説明|
|----|----|
|仮引数|要素数6のbytes型のリスト|
|返り値|送信に成功したか|

例)
```
sendData:bytes = [HEAD_WORD, 100, 150, 151, 152, 153]

evaluation:bool = _serial.send(sendData)

if evaluation:
    print("送信に成功しました")
else:
    print("送信に失敗しました")
```
</details>
<br>

####  <span style="font-size:14pt;">_serial.sendCommand()</span>
<details>
<summary>説明</summary>

仮引数に入力されたコマンドを送信します.
|内容|説明|
|----|----|
|仮引数|bytes型の変数|
|返り値|送信に成功したか|

※送信できるコマンドは0~200までの数と下記の定数のみです.
|定数名|コマンド内容|
|------|------------|
|`COMMAND_COMMUNICATION_END`|通信を終了することを宣言する|
|`COMMAND_DECLARE_EMERGENCY`|異常事態が発生したことを宣言する|

例)
```
sendData:bytes = 150

evaluation:bool = _serial.send(sendData)

if evaluation:
    print("送信に成功しました")
else:
    print("送信に失敗しました")
```
</details>
<br>

####  <span style="font-size:14pt;">_serial.sendInt()</span>
<details>
<summary>説明</summary>

仮引数に入力されたコマンドとint型の変数を送信します.
|内容|説明|
|----|----|
|仮引数|"送信したいコマンド","送信したいint型の変数"|
|返り値|送信に成功したか|

※送信できるコマンドは0~200までの数と下記の定数のみです.
|定数名|コマンド内容|
|------|------------|
|`COMMAND_COMMUNICATION_END`|通信を終了することを宣言する|
|`COMMAND_DECLARE_EMERGENCY`|異常事態が発生したことを宣言する|

※送信できるint型のデータは-1,600,000,000から1,600,000,000までの数のみです.

例)
```
sendCommandData:bytes = 150
sendIntData:int = 1023

evaluation:bool = _serial.sendInt(sendCommandData, sendIntData)

if evaluation:
    print("送信に成功しました")
else:
    print("送信に失敗しました")
```
</details>
<br>

####  <span style="font-size:14pt;">_serial.read()</span>
<details>
<summary>説明</summary>

Masterが受信したデータを要素数6のbytes型のリストに格納します.
|内容|説明|
|----|----|
|仮引数|(なし)|
|返り値|受信したデータ|

例)
```
readData:bytes = [None]*6

while(_serial.avaiable() == False):
    pass

readData = _serial.read()

print("受信しました!")

for i in range(0, 6, 1):
    print("要素" + str(i + 1) + ": " + str(readData[i]))
```
</details>
<br>

####  <span style="font-size:14pt;">_serial.readCommand()</span>
<details>
<summary>説明</summary>
Masterが受信したデータをコマンドのみbytes型の変数に格納します.

|内容|説明|
|----|----|
|仮引数|(なし)|
|返り値|受信したデータ|

例)
```
readData:bytes = None

while(!_serial.avaiable() == False):
    pass

readData = _serial.readCommand()

print("受信しました!")
print("コマンド: " + str(readData))
```
</details>
<br>

####  <span style="font-size:14pt;">_serial.readInt()</span>
<details>
<summary>説明</summary>

Masterが受信したデータをコマンドとint型のデータのみ, 要素数2のint型のリストに格納します.

※要素1のデータはコマンド, 要素2のデータはint型のデータです.

|内容|説明|
|----|----|
|仮引数|(なし)|
|返り値|受信したデータ|

例)
```
readData:int = [None]*2

while(!_serial.avaiable()):
    pass

readData = _serial.readInt()

print("受信しました!")
print("コマンド: " + str(readData[0]))
print("データ: " + str(readData[1]))
```
</details>
<br>

####  <span style="font-size:14pt;">_serial.avaiable()</span>
<details>
<summary>説明</summary>

まだuserが読み取っていないMasterが受信したデータある場合, Trueを返します.

※一度この関数を実行するか, _serial.read(), _serial.readCommand(), _serial.readInt()のいずれかの関数が実行された場合, 新たなデータを受信しない限り,返り値はFalseになります.

|内容|説明|
|----|----|
|仮引数|(なし)|
|返り値|まだuserが読み取っていないMasterが受信したデータがあるか|

例)
```
while(_serial.unconditional()):
    if(_serial.avaiable()):
        print("新たなデータを受信しました!")
    else:
        print("新たに受信されたデータはありません.")

    time.sleep(1)
```
</details>
<br>

####  <span style="font-size:14pt;">_serial.stateOfEmergency()</span>
<details>
<summary>説明</summary>

異常事態が宣言されている場合, Trueを返します.

|内容|説明|
|----|----|
|仮引数|(なし)|
|返り値|異常事態が宣言されているか|

例)
```
while(_serial.unconditional()):
    if(_serial.stateOfEmergency()):
        print("異常事態が宣言されています!!")
    else:
        print("異常事態は宣言されていません")
    
    time.sleep(1)
```
</details>
<br>

####  <span style="font-size:14pt;">_serial.convertToInt()</span>
<details>
<summary>説明</summary>

_serial.read()で格納したデータを_serial.readInt()で格納したデータと同様の形に変換します.

※要素1のデータはコマンド, 要素2のデータはint型のデータです.

|内容|説明|
|----|----|
|仮引数|要素数6のbytes型のリスト|
|返り値|_serial.readInt()の返り値と同様|

例)
```
readData:bytes = [None]*6

while(!_serial.avaiable()):
    pass

readData = _serial.read()

if(readData[1] == 100):
    print("受信したデータはint型のデータです")

    readIntData:int = _serial.convertToInt(readData)

    print("コマンド: " + str(readIntData[0]))
    print("データ: " + str(readIntData[1]))
```
※例はコマンド100はint型のデータ送信するコマンドであると言うことを予め決めていると仮定しています.
</details>
<br>

####  <span style="font-size:14pt;">_serial.logPrint()</span>
<details>
<summary>説明</summary>

アドレスのログに,仮引数に入力された文字列を表示します.

|内容|説明|
|----|----|
|仮引数|bool型の変数と文字列|
|返り値|(なし)|

例)
```
sendData:bytes = [HEAD_WORD, 100, 150, 151, 152, 153]

evaluation:bool = _serial.send(sendData)

_serial.logPrint(evaluation, "送信しました!!")
```
</details>
<br>

####  <span style="font-size:14pt;">_serial.unconditional()</span>
<details>
<summary>説明</summary>

無限ループを使用する際に`while True:`の`True`の代わりに使用します.

※`while True:`を使用した場合通信を正常に終了できなくなる可能性があるため注意してください.

|内容|説明|
|----|----|
|仮引数|(なし)|
|返り値|無条件ループが許可されているか|

例)
```
while _serial.unconditional():
    print("Hello World!!")

    time.sleep(1)
```
</details>

### bypass[].系列
各アドレスのファイル内において指定したアドレスに対して以下の関数を使用することが可能です.

`bypass[]`の`[]`内に関数を実行したいアドレスのアドレス番号を入力してください

例)
```
bypass[2].sendCommand(200)
```

※以降, 関数を実行したいアドレスの番号は`targetAddress`に書き換えています.

|関数名|仮引数|返り値|返り値の説明|
|------|------|------|------|
|`send()`|"bytes型のリスト"|(なし)||
|`sendCommand()`|"bytes型の変数"|(なし)||
|`sendInt()`|"bytes型の変数","int型の変数"|"bool型"|送信が可能であるか|
|`read()`|(なし)|"bytes型のリスト"|Slaveから受信した要素数6のリスト|
|`readCommand()`|(なし)|"bytes型"|Slaveから受信したコマンド|
|`readInt()`|(なし)|"int型のリスト"|Slaveから受信したコマンドとint型のデータ|
|`avaiable()`|(なし)|"bool型"|Slaveから受信されたデータがあるか|
|`convertToInt()`|"bytes型のリスト|"int型のリスト"|readInt()で読み取ったデータに変換|

<br>

####  <span style="font-size:14pt;">bypass[targetAddress].send()</span>
<details>
<summary>説明</summary>

仮引数に入力された要素数6のbytes型のリストを送信します.

※この関数の使用は対象アドレス内の関数と競合する可能性があるため推奨しません.

|内容|説明|
|----|----|
|仮引数|要素数6のbytes型のリスト|
|返り値|(なし)|

例)
```
sendData:bytes = [HEAD_WORD, 100, 150, 151, 152, 153]

bypass[targetAddress].send(sendData)

print("送信しました")
```
</details>
<br>

####  <span style="font-size:14pt;">bypass[targetAddress].sendCommand()</span>
<details>
<summary>説明</summary>

仮引数に入力されたコマンドを送信します.

※この関数の使用は対象アドレス内の関数と競合する可能性があるため推奨しません.

|内容|説明|
|----|----|
|仮引数|bytes型の変数|
|返り値|(なし)|

※送信できるコマンドは0~200までの数と下記の定数のみです.
|定数名|コマンド内容|
|------|------------|
|`COMMAND_COMMUNICATION_END`|通信を終了することを宣言する|
|`COMMAND_DECLARE_EMERGENCY`|異常事態が発生したことを宣言する|

例)
```
sendData:bytes = 150

bypass[targetAddress].send(sendData)

print("送信しました")
```
</details>
<br>

####  <span style="font-size:14pt;">bypass[targetAddress].sendInt()</span>
<details>
<summary>説明</summary>

仮引数に入力されたコマンドとint型の変数を送信します.

※この関数の使用は対象アドレス内の関数と競合する可能性があるため推奨しません.

|内容|説明|
|----|----|
|仮引数|"送信したいコマンド","送信したいint型の変数"|
|返り値|送信が可能であるか|

※送信できるコマンドは0~200までの数と下記の定数のみです.
|定数名|コマンド内容|
|------|------------|
|`COMMAND_COMMUNICATION_END`|通信を終了することを宣言する|
|`COMMAND_DECLARE_EMERGENCY`|異常事態が発生したことを宣言する|

※送信できるint型のデータは-1,600,000,000から1,600,000,000までの数のみです.

例)
```
sendCommandData:bytes = 150
sendIntData:int = 1023

evaluation:bool = bypass[targetAddress].sendInt(sendCommandData, sendIntData)

if evaluation:
    print("送信は可能です")
else:
    print("送信は不可能です")
```
</details>
<br>

####  <span style="font-size:14pt;">bypass[targetAddress].read()</span>
<details>
<summary>説明</summary>

Masterが受信したデータを要素数6のbytes型のリストに格納します.
|内容|説明|
|----|----|
|仮引数|(なし)|
|返り値|受信したデータ|

例)
```
readData:bytes = [None]*6

while(bypass[targetAddress].avaiable() == False):
    pass

readData = bypass[targetAddress].read()

print("受信しました!")

for i in range(0, 6, 1):
    print("要素" + str(i + 1) + ": " + str(readData[i]))
```
</details>
<br>

####  <span style="font-size:14pt;">bypass[targetAddress].readCommand()</span>
<details>
<summary>説明</summary>

Masterが受信したデータをコマンドのみbytes型の変数に格納します.

|内容|説明|
|----|----|
|仮引数|(なし)|
|返り値|受信したデータ|

例)
```
readData:bytes = None

while(!bypass[targetAddress].avaiable() == False):
    pass

readData = bypass[targetAddress].readCommand()

print("受信しました!")
print("コマンド: " + str(readData))
```
</details>
<br>

####  <span style="font-size:14pt;">bypass[targetAddress].readInt()</span>
<details>
<summary>説明</summary>

Masterが受信したデータをコマンドとint型のデータのみ, 要素数2のint型のリストに格納します.

※要素1のデータはコマンド, 要素2のデータはint型のデータです.

|内容|説明|
|----|----|
|仮引数|(なし)|
|返り値|受信したデータ|

例)
```
readData:int = [None]*2

while(!bypass[targetAddress].avaiable()):
    pass

readData = bypass[targetAddress].readInt()

print("受信しました!")
print("コマンド: " + str(readData[0]))
print("データ: " + str(readData[1]))
```
</details>
<br>

####  <span style="font-size:14pt;">bypass[targetAddress].avaiable()</span>
<details>
<summary>説明</summary>

まだuserが読み取っていないMasterが受信したデータある場合, Trueを返します.

※一度この関数を実行するか, bypass[targetAddress].read(), bypass[targetAddress].readCommand(), bypass[targetAddress].readInt()のいずれかの関数が実行された場合, 新たなデータを受信しない限り,返り値はFalseになります.

|内容|説明|
|----|----|
|仮引数|(なし)|
|返り値|まだuserが読み取っていないMasterが受信したデータがあるか|

例)
```
while(bypass[targetAddress].unconditional()):
    if(bypass[targetAddress].avaiable()):
        print("新たなデータを受信しました!")
    else:
        print("新たに受信されたデータはありません.")

    time.sleep(1)
```
</details>
<br>

####  <span style="font-size:14pt;">bypass[targetAddress].convertToInt()</span>
<details>
<summary>説明</summary>

bypass[targetAddress].read()で格納したデータをbypass[targetAddress].readInt()で格納したデータと同様の形に変換します.

※要素1のデータはコマンド, 要素2のデータはint型のデータです.

|内容|説明|
|----|----|
|仮引数|要素数6のbytes型のリスト|
|返り値|bypass[targetAddress].readInt()の返り値と同様|

例)
```
readData:bytes = [None]*6

while(!bypass[targetAddress].avaiable()):
    pass

readData = bypass[targetAddress].read()

if(readData[1] == 100):
    print("受信したデータはint型のデータです")

    readIntData:int = bypass[targetAddress].convertToInt(readData)

    print("コマンド: " + str(readIntData[0]))
    print("データ: " + str(readIntData[1]))
```
※例はコマンド100はint型のデータ送信するコマンドであると言うことを予め決めていると仮定しています.
</details>

## Slave関数一覧
Slaveにおいては下記の関数を使用することが可能です.
|関数名|仮引数|返り値|返り値の説明|
|------|------|------|------|
|`send()`|"uint8_t型の配列"|"bool型"|送信が成功したか|
|`sendCommand()`|"uint8_t型の変数"|"bool型"|送信が成功したか|
|`sendInt()`|"uint8_t型の変数","int型の変数"|"bool型"|送信が成功したか|
|`read()`|(なし)|"uint8_t型のポインタ"|Slaveから受信した要素数6のリスト|
|`readCommand()`|(なし)|"uint8_t型"|Slaveから受信したコマンド|
|`readInt()`|(なし)|"int型のポインタ"|Slaveから受信したコマンドとint型のデータ|
|`avaiable()`|(なし)|"bool型"|Slaveから受信されたデータがあるか|
|`started()`|(なし)|"bool型"|Masterにおいて通信が開始されたか|
|`stateOfEmergency()`|(なし)|"bool型"|異常事態が宣言されているか|
|`convertToInt()`|"uint8_t型の配列|"int型のポインタ"|readInt()で読み取ったデータに変換|

<br>

####  <span style="font-size:14pt;">_serial.send()</span>
<details>
<summary>説明</summary>

仮引数に入力された要素数6のbytes型のリストを送信します.<br>
|内容|説明|
|----|----|
|仮引数|要素数6のuint8_t型の配列|
|返り値|送信に成功したか|

例)<br>
送信に失敗した場合`LED_PIN`に接続されたLEDを点滅させる.
```
uint8_t sendData = {HEAD_WORD, 100, 150, 151, 152, 153};

bool evaluation = _serial.send(sendData);

if(evaluation == false){
    while(true){
        digitalWrite(LED_PIN, HIGH);
        delay(200);
        digitalWrite(LED_PIN, LOW);
        delay(200);
    }
}
```
</details>
<br>

####  <span style="font-size:14pt;">_serial.sendCommand()</span>
<details>
<summary>説明</summary>

仮引数に入力されたコマンドを送信します.
|内容|説明|
|----|----|
|仮引数|uint8_t型の変数|
|返り値|送信に成功したか|

※送信できるコマンドは0~200までの数と下記の定数のみです.
|定数名|コマンド内容|
|------|------------|
|`COMMAND_COMMUNICATION_END`|通信を終了することを宣言する|
|`COMMAND_DECLARE_EMERGENCY`|異常事態が発生したことを宣言する|

例)<br>
送信に失敗した場合`LED_PIN`に接続されたLEDを点滅させる.
```
uint8_t sendData = 150;

bool evaluation = _serial.send(sendData);

if(evaluation == false){
    while(true){
        digitalWrite(LED_PIN, HIGH);
        delay(200);
        digitalWrite(LED_PIN, LOW);
        delay(200);
    }
}
```
</details>
<br>

####  <span style="font-size:14pt;">_serial.sendInt()</span>
<details>
<summary>説明</summary>

仮引数に入力されたコマンドとint型の変数を送信します.
|内容|説明|
|----|----|
|仮引数|"送信したいコマンド","送信したいint型の変数"|
|返り値|送信に成功したか|

※送信できるコマンドは0~200までの数と下記の定数のみです.
|定数名|コマンド内容|
|------|------------|
|`COMMAND_COMMUNICATION_END`|通信を終了することを宣言する|
|`COMMAND_DECLARE_EMERGENCY`|異常事態が発生したことを宣言する|

※送信できるint型のデータは-1,600,000,000から1,600,000,000までの数のみです.

例)<br>
送信に失敗した場合`LED_PIN`に接続されたLEDを点滅させる.
```
uint8_t sendCommandData = 150;
int sendIntData = 1023;

bool evaluation = _serial.sendInt(sendCommandData, sendIntData);

if(evaluation == false){
    while(true){
        digitalWrite(LED_PIN, HIGH);
        delay(200);
        digitalWrite(LED_PIN, LOW);
        delay(200);
    }
}
```
</details>
<br>

####  <span style="font-size:14pt;">_serial.read()</span>
<details>
<summary>説明</summary>

Slaveが受信したデータを要素数6のbytes型のリストに格納します.
|内容|説明|
|----|----|
|仮引数|(なし)|
|返り値|受信したデータ|

例)<br>
受信したデータの内容が`{HEAD_WORD, 150, 151, 152, 153, 154}`の場合`LED_PIN`に接続されたLEDを点滅させる.
```
uint8_t *readData;

while(_serial.avaiable() == false)
    ;

readData = _serial.read();

if(*readData == HEAD_WORD && *(readData + 1) == 150 && *(readData + 2) == 151 && *(readData + 3) == 152 && *(readData + 4) == 153 && *(readData + 5) == 154){
    while(true){
        digitalWrite(LED_PIN, HIGH);
        delay(200);
        digitalWrite(LED_PIN, LOW);
        delay(200);
    }
}
```
</details>
<br>

####  <span style="font-size:14pt;">_serial.readCommand()</span>
<details>
<summary>説明</summary>

Slaveが受信したデータをコマンドのみuint8_t型の変数に格納します.

|内容|説明|
|----|----|
|仮引数|(なし)|
|返り値|受信したデータ|

例)<br>
受信したデータの内容が`150`の場合`LED_PIN`に接続されたLEDを点滅させる.
```
uint8_t readData;

while(!_serial.avaiable() == false)
    ;

readData = _serial.readCommand();

if(readData == 150){
    while(true){
        digitalWrite(LED_PIN, HIGH);
        delay(200);
        digitalWrite(LED_PIN, LOW);
        delay(200);
    }
}
```
</details>
<br>

####  <span style="font-size:14pt;">_serial.readInt()</span>
<details>
<summary>説明</summary>

Slaveが受信したデータをコマンドとint型のデータのみ, 要素数2のint型のリストに格納します.

※要素1のデータはコマンド, 要素2のデータはint型のデータです.

|内容|説明|
|----|----|
|仮引数|(なし)|
|返り値|受信したデータ|

例)<br>
受信したコマンドが`150`かつデータが`1023`の場合`LED_PIN`に接続されたLEDを点滅させる.
```
int *readData;

while(!_serial.avaiable())
    ;

readData = _serial.readInt();

if(*readData == 150 && *(readData + 1) == 1023){
    while(true){
        digitalWrite(LED_PIN, HIGH);
        delay(200);
        digitalWrite(LED_PIN, LOW);
        delay(200);
    }
}
```
</details>
<br>

####  <span style="font-size:14pt;">_serial.avaiable()</span>
<details>
<summary>説明</summary>

まだuserが読み取っていないMasterが受信したデータある場合, Trueを返します.

※一度この関数を実行するか, _serial.read(), _serial.readCommand(), _serial.readInt()のいずれかの関数が実行された場合, 新たなデータを受信しない限り,返り値はfalseになります.

|内容|説明|
|----|----|
|仮引数|(なし)|
|返り値|まだuserが読み取っていないMasterが受信したデータがあるか|

例)<br>
受信したデータが存在する場合`LED_PIN`に接続されたLEDを点灯させる.
```
while(true)
{
    if(_serial.avaiable())
        digitalWrite(LED_PIN, HIGH);
    else:
        digitalWrite(LED_PIN, LOW);

    delay(200);
}
```
</details>
<br>

####  <span style="font-size:14pt;">_serial.started()</span>
<details>
<summary>説明</summary>

Master側の通信が開始された場合, Trueを返します.

|内容|説明|
|----|----|
|仮引数|(なし)|
|返り値|Master側の通信が開始されたか|

例)
Master側で通信が開始された場合`LED_PIN`に接続されたLEDを点灯させる.
```
digitalWrite(LED_PIN, LOW);

while(!_serial.started() == false)
    ;

digitalWrite(LED_PIN, HIGH);
```
</details>
<br>

####  <span style="font-size:14pt;">_serial.stateOfEmergency()</span>
<details>
<summary>説明</summary>

異常事態が宣言されている場合, Trueを返します.

|内容|説明|
|----|----|
|仮引数|(なし)|
|返り値|異常事態が宣言されているか|

例)<br>
異常事態が宣言された場合`LED_PIN`に接続されたLEDを点灯させる.
```
while(true)
{
    if(_serial.stateOfEmergency())
        digitalWrite(LED_PIN, HIGH);
    else:
        digitalWrite(LED_PIN, LOW);

    delay(200);
}
```
</details>
<br>

####  <span style="font-size:14pt;">_serial.convertToInt()</span>
<details>
<summary>説明</summary>

_serial.read()で格納したデータを_serial.readInt()で格納したデータと同様の形に変換します.

※要素1のデータはコマンド, 要素2のデータはint型のデータです.

|内容|説明|
|----|----|
|仮引数|要素数6のuint8_t型のポインタ|
|返り値|_serial.readInt()の返り値と同様|

例)<br>
受信したコマンドが`150`かつ変換したデータが`1023`の場合`LED_PIN`に接続されたLEDを点滅させる.
```
uint8_t *readData;
int *readIntData;

while(!_serial.avaiable())
    ;

readData = _serial.read();

if(*(readData + 1) == 150){
    readIntData = _serial.convertToInt(readData);

    if(*(readIntData + 1) == 1023){
        while(true){
            digitalWrite(LED_PIN, HIGH);
            delay(200);
            digitalWrite(LED_PIN, LOW);
            delay(200);
        }
    }
}
```
※例はコマンド100はint型のデータ送信するコマンドであるということを予め決めていると仮定しています.
</details>
#!/bin/bash

terminalMessage () {
    if [ $1 == True ];then
        echo "[  OK  ] :" $2
    elif [ $1 == False ];then
        echo "[FAILED] :" $2
    fi
}

echo -n "Do you want to run DROS configuration program? (y/n) :"
read ANS

if [ $ANS == "y" ];then
    sudo apt-get update
    if [ $? -eq 0 ];then
        terminalMessage True "OS update"
    else
        terminalMessage False "OS upadte"
        exit 1
    fi

    sudo apt-get install python3.11
    if [ $? -eq 0 ];then
        terminalMessage True "Install python3.11"
    else
        terminalMessage False "Install python3.11"
        exit 1
    fi
    
    sudo apt-get install python3-pip
    if [ $? -eq 0 ];then
        terminalMessage True "Install pip"
    else
        terminalMessage False "Install pip"
        exit 1
    fi

    sudo apt-get install python3-tk
    if [ $? -eq 0 ];then
        terminalMessage True "Install tkinter"
    else
        terminalMessage False "Install tkinter"
        exit 1
    fi

    pip3 install glob2
    if [ $? -eq 0 ];then
        terminalMessage True "Install glob"
    else
        terminalMessage False "Install glob"
        exit 1
    fi

    pip3 install pyserial
    if [ $? -eq 0 ];then
        terminalMessage True "Install pyserial"
    else
        terminalMessage False "Install pyserial"
        exit 1
    fi

    terminalMessage True "Finish all DROS configuration program"

    exit 0
fi

exit 2
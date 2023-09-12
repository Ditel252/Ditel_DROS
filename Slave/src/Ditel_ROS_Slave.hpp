/*=======================================
<Ditel Robot Operating System Slave>

変更禁止
=======================================*/

#include <Arduino.h>

#define ADDRESS 1


#define HEAD_WORD 254
#define NO_SEND_DATA 252

#define COMMAND_CHECK_ADDRESS       200
#define COMMAND_COMMUNICATION_BEGIN 201
#define COMMAND_COMMUNICATION_END   202
#define COMMAND_DECLARE_EMERGENCY   203

#define MEMORY_SIZE_SERIAL_TASK 128
#define MEMORY_SIZE_USER_PROGRAM_TASK 128

#define _serial _userSerial

class Ditel_serial{
private:

public:
    uint8_t _sysReadData[6] = {0};

    bool _sysAvaiable =     false;
    bool _sysStarted =      false;
    bool _sysEmergency =    false;

    void sendCommand(uint8_t _sendCommandContents){
        char sendCommandContents[7];

        sendCommandContents[0] = HEAD_WORD;
        sendCommandContents[1] = _sendCommandContents + 1;
        sendCommandContents[2] = NO_SEND_DATA + 1;
        sendCommandContents[3] = NO_SEND_DATA + 1;
        sendCommandContents[4] = NO_SEND_DATA + 1;
        sendCommandContents[5] = NO_SEND_DATA + 1;
        sendCommandContents[6] = '\0';

        Serial.println(sendCommandContents);
    }

    void send(uint8_t *_sendDataContents)
    {
        char sendDataContents[7];

        for (int _i = 0; _i < 6; _i++)
            sendDataContents[_i] = _sendDataContents[_i] + 1;

        sendDataContents[6] = '\0';

        Serial.println(sendDataContents);
    }

    bool sendInt(uint8_t _sendCommand_Int, int _sendInt){
        uint8_t _sendData_Int[6] = {0};

        _sendData_Int[0] = HEAD_WORD;
        _sendData_Int[1] = _sendCommand_Int;

        _sendData_Int[2] = (int)(_sendInt / (252 * 252 * 252) + 1);
        _sendInt -= _sendData_Int[2] * 252 * 252 * 252 - 1;

        _sendData_Int[3] = (int)(_sendInt / (252 * 252) + 1);
        _sendInt -= _sendData_Int[3] * 252 * 252 - 1;

        _sendData_Int[4] = (int)(_sendInt / (252) + 1);
        _sendInt -= _sendData_Int[4] * 252 - 1;

        _sendData_Int[5] = (int)(_sendInt + 1);
        _sendInt -= _sendData_Int[5] - 1;

        if(_sendInt != 0){
            return false;
        }

        send(_sendData_Int);

        return true;
    }

    bool started(){
        return _sysStarted;
    }

    bool avaiable(){
        if(_sysAvaiable == true){
            _sysAvaiable = false;

            return true;
        }else{
            return false;
        }
    }

    uint8_t *read(){
        return _sysReadData;
    }

    uint8_t readCommand(){
        return _sysReadData[1];
    }

    int *readInt(){
        int _readInt;
        int *_sysReadInt;

        *_sysReadInt = _sysReadData[1];

        *(_sysReadInt + 1) = _sysReadData[2] * 252 * 252 * 252 + _sysReadData[3] * 252 * 252 + _sysReadData[4] * 252 + _sysReadData[5];

        return _sysReadInt;
    }

    uint8_t stateOfEmergency(){
        return _sysEmergency;
    }
};

Ditel_serial _userSerial;
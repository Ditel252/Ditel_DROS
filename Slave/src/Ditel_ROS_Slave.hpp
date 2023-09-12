/*=======================================
<Ditel Robot Operating System Slave>

変更禁止
=======================================*/

#include <Arduino.h>

#define ADDRESS 1


#define HEAD_WORD 254
#define NO_SEND_DATA 253

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

    void sendCommand(uint _sendCommandContents){
        char sendCommandContents[7];

        sendCommandContents[0] = HEAD_WORD;
        sendCommandContents[1] = _sendCommandContents;
        sendCommandContents[2] = NO_SEND_DATA;
        sendCommandContents[3] = NO_SEND_DATA;
        sendCommandContents[4] = NO_SEND_DATA;
        sendCommandContents[5] = NO_SEND_DATA;
        sendCommandContents[6] = '\0';

        Serial.println(sendCommandContents);
    }

    void send(uint8_t *_sendDataContents)
    {
        char sendDataContents[7];

        for (int _i = 0; _i < 6; _i++)
            sendDataContents[_i] = _sendDataContents[_i];

        sendDataContents[6] = '\0';

        Serial.println(sendDataContents);
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

    uint8_t stateOfEmergency(){
        return _sysEmergency;
    }
};

Ditel_serial _userSerial;
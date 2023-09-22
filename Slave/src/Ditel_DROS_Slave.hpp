/*=======================================
<Ditel Robot Operating System Slave>

変更禁止
=======================================*/

#include <Arduino.h>
#include <STM32FreeRTOS.h>

#define ADDRESS 1

#define HEAD_WORD 254
#define NO_SEND_DATA 242
#define INT_UNIT_MAX 241
#define COMMUNICATION_BASE_VALUE 11

#define COMMAND_CHECK_ADDRESS 200
#define COMMAND_COMMUNICATION_BEGIN 201
#define COMMAND_COMMUNICATION_END 202
#define COMMAND_DECLARE_EMERGENCY 203

#define MEMORY_SIZE_SERIAL_READ_TASK 128
#define MEMORY_SIZE_USER_PROGRAM_TASK 128

#define CONTINUOUS_SEND_BUFFER_TIME 50

#define SEND_INT_MAX 1600000000
#define SEND_INT_MIN -1600000000
#define SEND_INT_BASE 1600000000

#define _serial _userSerial

class Ditel_serial
{
private:
public:
    uint8_t _sysReadData[6] = {0};

    bool _sysAvaiable = false;
    bool _sysStarted = false;
    bool _sysEmergency = false;
    bool _sysUartCanUse = false;

    bool send(uint8_t *_sendDataContents)
    {

        char sendDataContents[7];

        sendDataContents[0] = _sendDataContents[0];

        for (int _i = 1; _i < 6; _i++)
        {
            if (_sendDataContents[_i] >= HEAD_WORD)
                return false;
            sendDataContents[_i] = _sendDataContents[_i] + COMMUNICATION_BASE_VALUE;
        }

        sendDataContents[6] = '\0';

        while (_sysUartCanUse == false)
            vTaskDelay(10 / portTICK_RATE_MS);

        Serial.println(sendDataContents);

        if (_sendDataContents[1] == COMMAND_DECLARE_EMERGENCY)
            _sysEmergency = true;

        vTaskDelay(CONTINUOUS_SEND_BUFFER_TIME / portTICK_RATE_MS);

        return true;
    }

    bool sendCommand(uint8_t _sendCommandContents)
    {
        uint8_t sendCommandContents[6];

        sendCommandContents[0] = HEAD_WORD;
        sendCommandContents[1] = _sendCommandContents;
        sendCommandContents[2] = NO_SEND_DATA;
        sendCommandContents[3] = NO_SEND_DATA;
        sendCommandContents[4] = NO_SEND_DATA;
        sendCommandContents[5] = NO_SEND_DATA;

        return send(sendCommandContents);
    }

    bool sendInt(uint8_t _sendCommand_Int, int _sendInt)
    {
        signed long int _IntData;

        uint8_t _sendData_Int[6] = {0};

        if (_sendInt > SEND_INT_MAX || _sendInt < SEND_INT_MIN)
            return false;

        _IntData = _sendInt;

        _IntData += SEND_INT_BASE;
        
        _sendData_Int[0] = HEAD_WORD;
        _sendData_Int[1] = _sendCommand_Int;

        _sendData_Int[2] = (int)(_IntData / (INT_UNIT_MAX * INT_UNIT_MAX * INT_UNIT_MAX));
        _IntData -= _sendData_Int[2] * INT_UNIT_MAX * INT_UNIT_MAX * INT_UNIT_MAX;

        _sendData_Int[3] = (int)(_IntData / (INT_UNIT_MAX * INT_UNIT_MAX));
        _IntData -= _sendData_Int[3] * INT_UNIT_MAX * INT_UNIT_MAX;

        _sendData_Int[4] = (int)(_IntData / (INT_UNIT_MAX));
        _IntData -= _sendData_Int[4] * INT_UNIT_MAX;

        _sendData_Int[5] = (int)(_IntData);
        _IntData -= _sendData_Int[5];

        return send(_sendData_Int);
    }

    bool started()
    {
        vTaskDelay(10 / portTICK_RATE_MS);

        if (_sysStarted == true)
        {
            vTaskDelay(50 / portTICK_RATE_MS);
            return true;
        }

        return false;
    }

    bool avaiable()
    {
        vTaskDelay(10 / portTICK_RATE_MS);

        if (_sysAvaiable == true)
        {
            _sysAvaiable = false;

            return true;
        }
        else
        {
            return false;
        }
    }

    uint8_t *read()
    {
        _sysAvaiable = false;
        return _sysReadData;
    }

    uint8_t readCommand()
    {
        _sysAvaiable = false;
        return _sysReadData[1];
    }

    int *readInt()
    {
        _sysAvaiable = false;
        int _readInt;
        int *_sysReadInt;
        signed long int _sysIntData;

        *_sysReadInt = _sysReadData[1];
        
        _sysIntData = _sysReadData[2] * INT_UNIT_MAX * INT_UNIT_MAX * INT_UNIT_MAX + _sysReadData[3] * INT_UNIT_MAX * INT_UNIT_MAX + _sysReadData[4] * INT_UNIT_MAX + _sysReadData[5];

        _sysIntData -= SEND_INT_BASE;

        *(_sysReadInt + 1) = _sysIntData;

        return _sysReadInt;
    }

    uint8_t stateOfEmergency()
    {
        return _sysEmergency;
    }
};

Ditel_serial _userSerial;
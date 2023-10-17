/*=======================================
<Ditel Robot Operating System Slave>

version : 1.1.38
許可された箇所以外変更禁止
=======================================*/

#include <Arduino.h>
#include <STM32FreeRTOS.h>

#define ADDRESS 1 //(変更可)アドレスを設定する

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

bool _readDataIsReturnData = false;

class Ditel_serial
{
private:
    int _returnDataTime = 0;
    uint8_t _returnData[6];
    bool _lastAvaiable = false;

    uint8_t *_result_read;
    uint8_t _sysResultData_read[6];

    int *_result_readInt;
    int _sysResultData_readInt[2];
    signed long int _sysResultLongIntData_readInt;

    int *_result_convertToInt;
    int _sysResultData_convertToInt[2];
    signed long int _sysResultLongIntData_convertToInt;

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

        _lastAvaiable = _sysAvaiable;
        _sysAvaiable = false;

        Serial.println(sendDataContents);

        if (_sendDataContents[1] == COMMAND_DECLARE_EMERGENCY)
            _sysEmergency = true;

        _readDataIsReturnData = true;

        _returnDataTime = 0;

        while (_sysAvaiable == false)
        {
            if (_returnDataTime >= 30)
                break;

            vTaskDelay(10 / portTICK_RATE_MS);
            _returnDataTime++;
        }

        if (_returnDataTime < 30)
        {
            _returnData[0] = *(_sysReadData + 0);
            _returnData[1] = *(_sysReadData + 1);
            _returnData[2] = *(_sysReadData + 2);
            _returnData[3] = *(_sysReadData + 3);
            _returnData[4] = *(_sysReadData + 4);
            _returnData[5] = *(_sysReadData + 5);

            _readDataIsReturnData = false;

            if ((*_sendDataContents == _returnData[0]) && ((*(_sendDataContents + 1) + 10) == _returnData[1]) && (*(_sendDataContents + 2) == _returnData[2]) && (*(_sendDataContents + 3) == _returnData[3]) && (*(_sendDataContents + 4) == _returnData[4]) && (*(_sendDataContents + 5) == _returnData[5]))
            {
                _readDataIsReturnData = false;
                _sysAvaiable = _lastAvaiable;

                vTaskDelay(CONTINUOUS_SEND_BUFFER_TIME / portTICK_RATE_MS);

                return true;
            }
            else
            {
                _readDataIsReturnData = false;
                _sysAvaiable = _lastAvaiable;

                vTaskDelay(CONTINUOUS_SEND_BUFFER_TIME / portTICK_RATE_MS);

                return false;
            }
        }
        else
        {
            _readDataIsReturnData = false;
            _sysAvaiable = _lastAvaiable;

            vTaskDelay(CONTINUOUS_SEND_BUFFER_TIME / portTICK_RATE_MS);

            return false;
        }
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

            if (_readDataIsReturnData == false)
                return true;
            else
                return false;
        }
        else
        {
            return false;
        }
    }

    uint8_t *read()
    {
        _sysAvaiable = false;

        if (_readDataIsReturnData == false)
        {
            _sysResultData_read[0] = *(_sysReadData + 0);
            _sysResultData_read[1] = *(_sysReadData + 1);
            _sysResultData_read[2] = *(_sysReadData + 2);
            _sysResultData_read[3] = *(_sysReadData + 3);
            _sysResultData_read[4] = *(_sysReadData + 4);
            _sysResultData_read[5] = *(_sysReadData + 5);
        }

        _result_read = &_sysResultData_read[0];

        return _result_read;
    }

    uint8_t readCommand()
    {
        _sysAvaiable = false;
        return _sysReadData[1];
    }

    int *readInt()
    {
        _sysAvaiable = false;

        _sysResultData_readInt[0] = _sysReadData[1];

        _sysResultLongIntData_readInt = _sysReadData[2] * INT_UNIT_MAX * INT_UNIT_MAX * INT_UNIT_MAX + _sysReadData[3] * INT_UNIT_MAX * INT_UNIT_MAX + _sysReadData[4] * INT_UNIT_MAX + _sysReadData[5];
        _sysResultLongIntData_readInt -= SEND_INT_BASE;

        _sysResultData_readInt[1] = _sysResultLongIntData_readInt;

        _result_readInt = &_sysResultData_readInt[0];

        return _result_readInt;
    }

    uint8_t stateOfEmergency()
    {
        return _sysEmergency;
    }

    int *convertToInt(uint8_t *_convertData)
    {
        _sysResultLongIntData_convertToInt = *(_convertData + 2) * INT_UNIT_MAX * INT_UNIT_MAX * INT_UNIT_MAX + *(_convertData + 3) * INT_UNIT_MAX * INT_UNIT_MAX + *(_convertData + 4) * INT_UNIT_MAX + *(_convertData + 5);
        _sysResultLongIntData_convertToInt -= SEND_INT_BASE;

        _sysResultData_convertToInt[0] = *(_convertData + 1);
        _sysResultData_convertToInt[1] = _sysResultLongIntData_convertToInt;

        _result_convertToInt = &_sysResultData_convertToInt[0];

        return _result_convertToInt;
    }
};

Ditel_serial _userSerial;
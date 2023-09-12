/*=======================================
<Ditel Robot Operating System Slave>

変更禁止
=======================================*/

#include <Arduino.h>
#include "User_main.hpp"
#include <STM32FreeRTOS.h>

void serialTask(void *pvParameters);
void userProgramTask(void *pvParameters);

class systemSerial
{
private:
  uint8_t sysSerialReadData[6] = {0};
  uint8_t sysSerialSendData[6] = {0};

public:
  void setupProcess()
  {
    Serial.begin(115200);

    pinMode(D13, OUTPUT);

    while (true)
    {
      sysSerialReadData[0] = Serial.read();

      if (sysSerialReadData[0] == HEAD_WORD)
      {
        for (int _i = 1; _i < 6; _i++)
        {
          vTaskDelay(3 / portTICK_RATE_MS);
          sysSerialReadData[_i] = Serial.read() - 1;
        }

        if (sysSerialReadData[1] == COMMAND_CHECK_ADDRESS)
        {
          sysSerialSendData[0] = HEAD_WORD;
          sysSerialSendData[1] = COMMAND_CHECK_ADDRESS;
          sysSerialSendData[2] = ADDRESS;
          sysSerialSendData[3] = NO_SEND_DATA;
          sysSerialSendData[4] = NO_SEND_DATA;
          sysSerialSendData[5] = NO_SEND_DATA;

          _serial.send(sysSerialSendData);
        }
        else if (sysSerialReadData[1] == COMMAND_COMMUNICATION_BEGIN)
        {
          sysSerialSendData[0] = sysSerialReadData[0];
          sysSerialSendData[1] = sysSerialReadData[1] + 10;

          for (int _i = 2; _i < 6; _i++)
            sysSerialSendData[_i] = sysSerialReadData[_i];

          _serial.send(sysSerialSendData);
          _userSerial._sysStarted = true;

          break;
        }
      }

      vTaskDelay(1 / portTICK_RATE_MS);
    }
  }

  void systemRead()
  {
    sysSerialReadData[0] = Serial.read();

    if (sysSerialReadData[0] == HEAD_WORD)
    {
      for (int _i = 1; _i < 6; _i++)
      {
        vTaskDelay(3 / portTICK_RATE_MS);
        sysSerialReadData[_i] = Serial.read() - 1;
      }

      if(sysSerialReadData[0] == HEAD_WORD){
        _serial._sysAvaiable = true;

        _serial._sysReadData[0] = sysSerialReadData[0];
        for(int _i = 1; _i < 6; _i++)
          _serial._sysReadData[_i] = sysSerialReadData[_i];
        
        if(sysSerialReadData[1] == COMMAND_COMMUNICATION_END)
          _userSerial._sysStarted = false;
        else if(sysSerialReadData[1] == COMMAND_DECLARE_EMERGENCY)
          _userSerial._sysEmergency = true;

        sysSerialReadData[1] += 10;
        _serial.send(sysSerialReadData);
      }
    }

    vTaskDelay(1 / portTICK_RATE_MS);
  }
};

systemSerial serialsys;

void setup()
{
  xTaskCreate(serialTask, "Task for serial", MEMORY_SIZE_SERIAL_TASK, NULL, 2, NULL);
  xTaskCreate(userProgramTask, "Task for user program", MEMORY_SIZE_USER_PROGRAM_TASK, NULL, 1, NULL);

  vTaskStartScheduler();
}

void loop()
{
}

uint8_t serialReadData[6] = {0};

void serialTask(void *pvParameters)
{
  serialsys.setupProcess();

  while (true)
  {
    serialsys.systemRead();
  }
}

void userProgramTask(void *pvParameters)
{
  _setup();

  while (true)
  {
    _loop();
  }
}

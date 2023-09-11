#include <Arduino.h>
#include "User_main.hpp"
#include <STM32FreeRTOS.h>

Ditel_Serial serialx;

void serialTask(void *pvParameters);
void userProgramTask(void *pvParameters);

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
  Serial.begin(115200);

  pinMode(D13, OUTPUT);

  while (true)
  {
    serialReadData[0] = Serial.read();

    if (serialReadData[0] == 254)
      Serial.println("ON");
    else if (serialReadData[0] == 100)
      Serial.println("OFF");
    
    vTaskDelay(1/portTICK_RATE_MS);
  }
}

void userProgramTask(void *pvParameters)
{
  _setup();

  while(true){
    _loop();
  }
}

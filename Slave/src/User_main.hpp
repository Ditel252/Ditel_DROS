/*=======================================
<Ditel Robot Operating System Slave>

version : 1.1.0
ユーザーはここにプラグラムを書く
=======================================*/

#include "Ditel_ROS_Slave.hpp"

void _setup()
{
    pinMode(D13, OUTPUT);

    digitalWrite(D13, LOW);
}

void _loop()
{
}

# IoT
物联网项目

1、硬件使用NodeMcu开发板（ESP8266芯片）和传感器；

2、使用micropython固件；

3、场景使用HASS平台；

4、使用HASS自带的mqttserver做消息传递。

![思维导图](https://flywen.github.io/1.png)


NodeMcu(ESP8266)部分：

1、安装esptool，刷micropython(https://github.com/micropython)固件

$pip install esptool
$esptool.py --port xxx erase_flash
$esptool.py --port xxx --b...

2、使用终端工具连接NodeMcu

Mac自带的screen连接后无法输入，改用securecrt连接

连接后按板上的res键进入python shell

3、使用webrepl连接开发板，可上传代码文件

https://github.com/micropython/webrepl

4、micropython使用mqtt

下载https://github.com/micropython/micropython-lib/blob/master/umqtt.simple/umqtt/simple.py

使用webrepl上传至开发板

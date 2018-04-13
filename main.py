import network
import time
from machine import Pin
from simple import MQTTClient
import dht

SSID = "Otec_wuhan"
PASSWD = "Otec8888"
#SSID = "FlyWen_saloon"
#PASSWD = "13006371878"

def connect_net():
    net = network.WLAN(network.STA_IF)
    net.active(True)
    if net.isconnected():
        print("network is ok...")
    else:
        print("Ready...")
        net.connect(SSID, PASSWD)
        print("network is %s" % SSID)

connect_net()

def do_dht():
    ht = dht.DHT11(Pin(2))
    ht.measure()
    ht_h = str(ht.humidity())
    ht_t = str(ht.temperature())
    return ht_h, ht_t

#h, t = do_dht() 
#print("humidity is %s,temprature is %s" % (h, t))

def send_mq():
    h, t = do_dht()
    print("h=%s,t=%s"%(h,t))
    m = MQTTClient('nodemcu', '192.168.1.112')
    m.connect()
    m.publish('hh', h)
    time.sleep(0.2)
    m.publish('tt', t)
    m.disconnect()

while True:
    time.sleep(5)
    send_mq()

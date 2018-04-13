import network

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
        net.connect(SSID, PASSWD)

connect_net()

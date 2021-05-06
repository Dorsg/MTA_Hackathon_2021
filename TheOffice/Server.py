from PodSixNet.Channel import Channel
from PodSixNet.Server import Server
import time

class ClientChannel(Channel):

    def Network(self, data):
        print(data)

    def Network_myaction(self, data):
        print("myaction:", data)

class MyServer(Server):
    channelClass = ClientChannel

    def Connected(self, channel, addr):
            print('new connection:', channel)

myserver = MyServer()

while True:

    myserver.Pump()
    time.sleep(0.0001)






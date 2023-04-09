#!/usr/bin/env python
# -*- coding: utf-8 -*-

#client.connect(('192.168.3.24', 6688))

import socket
import threading
import time
def getip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    a = s.getsockname()[0]
    s.close()
    return a
ipconfig = open('./ip.txt','r').read()
ip_port = (ipconfig,6666)

sk=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sk.connect(ip_port)
gtip = getip()
def js():
    while 1:
        date=sk.recv(1024)#接受信息
        d = date.decode('utf-8')
        fg = d.split(sep=':')
        #print(fg)
        if fg[0] != gtip:
            open('./wz.txt', 'w', encoding='UTF-8').write(fg[1])
            print(d)
            time.sleep(0.2)

sw=threading.Thread(target=js)
sw.setDaemon(1)
sw.start()
while True:
    date = gtip+':'+open('./wzxx.txt','r',encoding='UTF-8').read()
    time.sleep(0.2)
    sk.send(date.encode(encoding='utf-8'))
    if date=='exit':
        break
sk.close#结束连接
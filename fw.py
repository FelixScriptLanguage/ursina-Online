# -*- coding: utf-8 -*-
import socket
import threading
def getip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    a = s.getsockname()[0]
    s.close()
    return a
bjip = getip()
print('我的ip:'+bjip)
print()
ip_port = (bjip,6666)
sk=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sk.bind(ip_port)
sk.listen(1)
yh=[]
def fs(msg):
    for i in yh:
        try:
            i.send(msg.encode('utf-8'))
        except Exception as e:
            pass
        else:
            pass
def js(sed,dree):
    while 1:
        date=sed.recv(1024).decode('utf-8')#接受信息
        if date=='exit':
            sed.close#结束连接
            break
        msg=str(date)
        #print(msg)
        fs(msg)
def work():
    while 1:
        try:
            #print('等待用户连接')
            sed,dree=sk.accept()
            yh.append(sed)
            #加入提示
            msg='有用户加入:'+str(dree)+'  目前有'+str(len(yh))+'用户在线'
            print(msg)
            #fs(msg)
            #sed.send('欢迎来到在线聊天室（目前支持10人同时聊天）'.encode('utf-8'))
            js(sed,dree)
        except Exception as e:
            #print('错误:',e)
            pass
        else:
            pass
        #退出提示
        yh.remove(sed)
        msg='有用户退出:'+str(dree)+'  目前有'+str(len(yh))+'用户在线'
        print(msg)
        #fs(msg)
dxc=[]
if __name__ == "__main__":
    for i in range(10):
        dxc.append(threading.Thread(target=work))
    for i in dxc:
        i.setDaemon(1)
        i.start()
    for i in dxc:
        i.join()
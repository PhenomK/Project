from socket import *
import os
import struct
ADDR = ('172.16.41.66',8989)
BUFSIZE = 1024
filename = '12345.docx'
FILEINFO_SIZE=struct.calcsize('128s32sI8s')
tcpCliSock = socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(ADDR)
fhead=struct.pack('128s11I',filename,0,0,0,0,0,0,0,0,os.stat(filename).st_size,0,0)
tcpCliSock.send(fhead)
fp = open(filename,'rb')
while 1:
    filedata = fp.read(BUFSIZE)
    if not filedata: break
    tcpCliSock.send(filedata)
print ("文件传送完毕，正在断开连接...")
fp.close()
tcpCliSock.close()
print ("连接已关闭...")
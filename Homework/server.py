from socket import *
import struct
ADDR = ('172.16.41.66',8989)
BUFSIZE = 1024
FILEINFO_SIZE=struct.calcsize('128s32sI8s')
tcpSrvSock = socket(AF_INET,SOCK_STREAM)
tcpSrvSock.bind(ADDR)
tcpSrvSock.listen(True)
print ("等待连接...")
conn,addr = tcpSrvSock.accept()
print ("客户端已连接—> "),addr
fhead = conn.recv(FILEINFO_SIZE)
filename,temp1,filesize,temp2=struct.unpack('128s32sI8s',fhead)
#print filename,temp1,filesize,temp2
print (filename,len(filename),type(filename))
print (filesize)
filename = 'new_'+filename.strip('\00') #...
fp = open(filename,'wb')
restsize = filesize
print ("正在接收文件... "),
while 1:
    if restsize > BUFSIZE:
        filedata = conn.recv(BUFSIZE)
    else:
        filedata = conn.recv(restsize)
    if not filedata: break
    fp.write(filedata)
    restsize = restsize-len(filedata)
    if restsize == 0:
     break
print ("接收文件完毕，正在断开连接...")
fp.close()
conn.close()
tcpSrvSock.close()
print ("连接已关闭...")
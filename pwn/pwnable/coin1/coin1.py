# coding: utf-8
from socket import*
import random
import time
HOST='0.0.0.0'
PORT=9007
#����socket����
client=socket(AF_INET,SOCK_STREAM)
#AF_INET��ʾ��ʹ�ñ�׼��ipv4��ַ��������
#SOCK_STREAM˵������һ��TCP�ͻ���
    
client.connect((HOST,PORT))#����
data = client.recv(1024)
time.sleep(4)
for i in range(100):
    data = client.recv(1024)#��������
    int_cnt=data.find('N=')+2 #int_cnt�����ҵ�N,C
    N=0
    C=0
    while True:     
        N+=int(data[int_cnt])
        int_cnt+=1
        if data[int_cnt]==' ':
            break
        N*=10
    int_cnt=data.find('C=')+2
    while True:     
        C+=int(data[int_cnt])
        int_cnt+=1
        if data[int_cnt]<'0' :
            break
        if data[int_cnt]>'9' :
            break
        C*=10
    print 'get N=%d'%N,'get C=%d'%C#��ӡN,C
    left=0
    right=N-1
    mid=(left+right)/2#����
    for i in xrange(C):#C��ѯ�� 
        str_ask=[str(n) for n in xrange(left,mid+1)]
        str_ask=" ".join(str_ask)#����Ҫѯ�ʵ�Ӳ��
        client.send(str_ask+"\n")#��������
        str_weight=client.recv(1024)#��������
        str_weight.split("\n")
        int_weight=int(str_weight)
        print "int_weight = ",int_weight,"l=%d mid=%d r=%d"%(left,mid,right)
        if int_weight!=((mid-left+1)*10):
            right=mid
            mid=(right+left)/2
        else:
            left=mid+1
            mid=(left+right)/2
    client.send(str(mid)+"\n")
    ans=client.recv(1024)
    print "ans=",ans
ans=client.recv(1024)#flag
print "ans=%s"%ans    
client.close()

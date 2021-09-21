import socket
import cv2
import os

sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('YOURLAPTOPNAMEHERE', 1234))

while True:
    msg=sock.recv(1024).decode()
    if msg=='Capture':
        break
    
cam=cv2.VideoCapture(0)
ret, frame=cam.read()
cv2.destroyAllWindows()
cv2.imwrite('frame.png', frame)
cam.release()

bytes=open('frame.png', 'rb').read()
i=0
n=0

while True:
    sock.send(bytes[i:i+40960000])
    i+=40960000
    n+=1
    if n==4:
       sock.send(bytes[i:])
       break

os.remove('frame.png')

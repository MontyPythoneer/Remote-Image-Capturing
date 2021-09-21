import socket

start=input('Start? ')

sections=""

sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((socket.gethostname(), 1234))

n=0

while True:
    sock.listen()
    try:
        client, address=sock.accept()
    except:
        pass
    client.send("Capture".encode())
    image=client.recv(40960000)
    sock.settimeout(0.01)
    sections+=str(image)
    n+=1
    if n==4:
        break
    
rewrite=open('Retrieved.png', 'wb')
rewrite.write(eval(sections))
rewrite.close()

    
    

    


    

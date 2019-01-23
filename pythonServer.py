import datetime
import socket
import sys
import time

s = socket.socket()         # Create a socket object
host = sys.argv[1]      # Get local machine name
port = 6006                 # Reserve a port for your service.
s.bind((host, port))        # Bind to the port
print(host)
s.listen(5)                 # Now wait for client connection.

while True:
    c, address = s.accept()  # Establish connection with client.
    print('Got connection from', address)  # run algorithm
    data = c.recv(1024)
    c.send(b'1')
    if data:
        print("receiving text", data)
        text = c.recv(1024)
        print(text)
        c.send(b'2')

    data = c.recv(1024)
    c.send(b'3')
    if data:
        fileName = datetime.datetime.now().strftime("%I_%M_%B_%d_%Y")
        audioFile = open(fileName + ".wav", 'wb')
        print("receiving audio", data)
        audio = c.recv(1024)
        while audio:
            audioFile.write(audio)
            audio = c.recv(1024)
        audioFile.close()
    c.close()
    time.sleep(2)
    c, address = s.accept()  # Establish connection with client.
    print('Got connection from', address)  # run algorithm
    print("done receiving")
    c.send(b'hihihi4.')
    #call algorithm
    #c.send(b'1') #send label
                               # Close the connection
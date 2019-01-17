import socket               # Import socket module
import datetime

s = socket.socket()         # Create a socket object
host = '192.168.1.109' # Get local machine name
port = 5000                # Reserve a port for your service.
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
        c.send(b'1')

    data = c.recv(1024)
    c.send(b'1')
    if data:
        print("receiving audio", data)
        audio = c.recv(1024)
        fileName = datetime.datetime.now().strftime("%I_%M_%B_%d_%Y")
        audioFile = open(fileName + ".wav", 'wb')
        while audio:
            audioFile.write(audio)
            audio = c.recv(1024)
        print("done receiving")
        audioFile.close()
    c.send(b'Done receiving') #send label back
    #call algorithm
    #c.send(b'1') #send label
    c.close()                           # Close the connection
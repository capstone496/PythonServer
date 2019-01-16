import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = '100.65.196.219' # Get local machine name
port = 5000                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port
print(host)
s.listen(5)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   print ('Got connection from', addr)
   c.send(b'Thank you for connecting')
   c.close()                # Close the connection
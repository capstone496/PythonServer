import datetime
import socket
import sys
import time

from serve_prediction import predict, get_tensors_for_prediction, spectrogram, graph_file, LABELS

s = socket.socket()         # Create a socket object
host = sys.argv[1]          # Get local machine name
port = 6300                 # Reserve a port for your service.

s.bind((host, port))        # Bind to the port
print(host)
s.listen(5)                 # Now wait for client connection.

graph, image_buffer_input, prediction, keep_prob = get_tensors_for_prediction(graph_file)

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
        audio_filename = datetime.datetime.now().strftime("%I_%M_%B_%d_%Y") + ".wav"

        audio_file = open(audio_filename, 'wb')
        print("receiving audio", data)
        audio = c.recv(1024)

        while audio:
            audio_file.write(audio)
            audio = c.recv(1024)
        audio_file.close()
    c.close()
    time.sleep(2)

    c, address = s.accept()  # Establish connection with client.
    print('Got connection from', address)  # run algorithm

    predicted_emotion = predict(graph,
                                image_buffer_input,
                                prediction,
                                keep_prob,
                                spectrogram(audio_filename))
    print(LABELS[predicted_emotion])
    c.send(LABELS[predicted_emotion])

    c.close()

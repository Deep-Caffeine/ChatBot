import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    #  Wait for next request from client
    message = str(socket.recv())
    print("Received request: %s" % message)

    if message == "exit":
        break

    #  Do some 'work'
    time.sleep(1)

    #  Send reply back to client
    socket.send("World")

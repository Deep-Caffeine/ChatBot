import time
import zmq


def main():
    print("Chatbot 서버 시작 중...")

    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")

    while True:
        message = str(socket.recv())
        print(f"Received request: {message}")

        if message == "exit":
            break

        time.sleep(1)

        socket.send_string("World")


if __name__ == "__main__":
    main()

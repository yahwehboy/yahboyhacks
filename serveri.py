import socket
import threading


def handle_client(client_socket, addr):
    try:
        while True:
            #receive and prints client messages
            request = client_socket.recv(1024).decode("utf-8")
            if request.lower() == "close":
                client_socket.send("CLosed".encode("utf-8"))
                break
            print(f"Received: {request}")
            #convert and send accept response to the client
            response = "accepted"
            client_socket.send(response.encode("utf-8"))
    except Exception as e:
        print(f"Error when handling client: {e}")
    finally:
        client_socket.close()
        print(f"Connection to client ({addr[0]}:{addr[1]}) closed")


def run_serer():
    server_ip = "127.0.0.1" #server hostname
    port = 8000 #server port number
    #create a socket object
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #binds the socket to the host and port
        server.bind((server_ip, port))
        #listening for incoming connections
        server.listen()
        print(f"Listening on {server_ip}:{port}")

        while True:
            #accepts a client connection
            client_socket, addr = server.accept()
            print(f"Accepted connection from {addr[0]}:{addr[1]}")
            #start a new thread to handle the client
            thread = threading.Thread(target=handle_client, args=(client_socket, addr))
            thread.start()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        server.close()

run_serer()
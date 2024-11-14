import socket

def run_client():
    #creating a sockect object
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip = "127.0.0.1" #replace withbthe server ip
    server_port = 8000 #replace with server port number

    #establish connection with server
    client.connect((server_ip, server_port))

    while True:
        #input message and send it to the server
        msg = input("Enter a message: ")
        client.send(msg.encode("utf-8") [:1024])

        #receive message from server
        response = client.recv(1024)
        response = response.decode("utf-8")

        #if server sent us "closed" in payload, we break out of the loop and close the socket
        if response.lower() == "close":
            break
        
        print(f"Received: {response}")

    #close client socket (connection to the server)
    client.close()
    print("Connection to server closed")

run_client()

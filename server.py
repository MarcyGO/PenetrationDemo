import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
# specify the socket family, and the socket types: ipv4, connection based protocol TCP

# 192.162.80.1
host = socket.gethostname()
# specify the port that we'll be listening
port = 444

# bind them to the serversocket
serversocket.bind((host, port))
# set up TCP listener
serversocket.listen(3) # specify how many request to allow

while True:
    # establish the connection
    clientsocket, address = serversocket.accept() # accept the TCP information coming from the client
    print("receive connection from %r" % str(address))
    # create a message
    message = "Thank you for connecting to the server." + "/r/n"
    # let the client know it successfully connects to the server
    clientsocket.send(message.encode('ascii'))
    # close the socket
    clientsocket.close()
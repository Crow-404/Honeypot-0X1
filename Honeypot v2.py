import paramiko (Used for handing SSH connections)
import socket (Manges network communication)
import threading (Allows multiple connections to be handled concurrently by running each connection on a separate thread)

class SSH_Server(paramiko.ServerInterface):
    # create class (SSH_server) to meake server interface like authentication
    def check_auth_password(self, username, password):
        # check auth password (for client authenticate using passowrd)
        print(f"{username}:{password}")
        # for entering (Username & Password)
        return paramiko.AUTH_FAILED  # You can modify this for actual authentication 

    def check_auth_publickey(self, username, key):
        # check auth publickey (for client authenticate using an SSH public key)
        return paramiko.AUTH_FAILED  # Always fails the public key authentication. You can modify this for actual key-based authentication

def handle_connection(client_sock, server_key):
    # Handles SSH connections from clients.
    transport = paramiko.Transport(client_sock)
    # Creates a transport layer for the SSH connection using client socket
    transport.add_server_key(server_key)
    #  Adds the server’s RSA key to the SSH transport layer for encryption and signing purposes
    
    SSH = SSH_Server()  # Create instance of SSH_Server
    try:
        transport.start_server(server=SSH)  #  Starts the SSH server on the transport layer using the SSH_Server instance, handling things like authentication.
    except Exception as e:
        print(f"Failed to start SSH server: {e}")
        # Catches and logs any errors that occur while starting the SSH server, such as issues with the connection.
    finally:
        transport.close()
        # Closes the SSH transport layer to clean up resources after handling the connection.

def main():
    # the entry point for the server
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Creates a TCP socket 
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Allows the reuse the same address/port for binding
    server_sock.bind(('0.0.0.0', 22))
    # Binds the socket to all available network interface (0.0.0.0) = "I use it because it's listening on all network interface" , and port 22 is the default SSH port .
    server_sock.listen(100)
    #  Starts listening for incoming connections with a backlog of 100 pending connections.

    server_key = paramiko.RSAKey.generate(2048)  # Generates a 2048-bit RSA key pair for the SSH server. This is used to authenticate the server to the client.

    while True:
        client_sock, client_addr = server_sock.accept()
        print(f"Connection: {client_addr[0]}:{client_addr[1]}")
        # Blocks and waits for a new client to connect. When a client connects, it returns a new socket (client_sock) and the client's address (client_addr).
        #  Logs the IP address and port number of the connected client for debugging

        # Handle each connection in a new thread
        t = threading.Thread(target=handle_connection, args=(client_sock, server_key))
        # threading.Thread(): Creates a new thread to handle the connection. This prevents the main server loop from blocking while handling a single connection.
        t.start()
        # t.start(): Starts the thread, which will run handle_connection() to manage the client's connection.

if __name__ == "__main__":
    main()
    # This ensures that the main() function is called only when the script is executed directly, not when imported as a module.

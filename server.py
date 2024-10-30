import socket
from DES import decrypt_long

# Pre-shared key (same as on client side)
KEY = '1101001110111010101010110010101010110101110111101010111010110101'  # Example 64-bit key

def start_server():
    # Setting up server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12346))
    server_socket.listen(1)
    print("Server is active and listening on port 12345...")

    # Accept connection from client
    connection, address = server_socket.accept()
    print(f"Connection established with {address}")

    # Receive encrypted message
    encrypted_message = connection.recv(4096).decode()
    print(f"Encrypted Message: {encrypted_message}")

    # Decrypt the received message
    decrypted_message = decrypt_long(encrypted_message, KEY)
    print(f"Decrypted Message: {decrypted_message}")

    # Close the connection
    connection.close()

if __name__ == "__main__":
    start_server()

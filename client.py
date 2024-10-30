import socket
from DES import encrypt_long

# Pre-shared key (same as on server side)
KEY = '1101001110111010101010110010101010110101110111101010111010110101'  # Example 64-bit key

def start_client(message):
    # Set up the client socket to connect to server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    # Encrypt the message before sending
    encrypted_message = encrypt_long(message, KEY)
    client_socket.sendall(encrypted_message.encode())
    print(f"Encrypted Message Sent: {encrypted_message}")

    # Close the connection
    client_socket.close()

if __name__ == "__main__":
    # Message to send (should be >64 bits as per requirements)
    message = '1101001110111010101010110010101010110101110111101010111010110101110100111011101010101011001010101011010111011110101011101011010101101011'
    start_client(message)

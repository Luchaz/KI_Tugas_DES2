import socket
from DES import encrypt_long

# Hardcoded kunci DES yang harus sama di client dan server (64-bit binary string)
KEY = '1101001110111010101010110010101010110101110111101010111010110101'

def start_client(message):
    # Inisialisasi client socket untuk mengirim pesan terenkripsi ke server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 23456))  # Terhubung ke server di port 23456

    # Enkripsi pesan sebelum dikirim
    encrypted_message = encrypt_long(message, KEY)
    client_socket.sendall(encrypted_message.encode())  # Kirim pesan terenkripsi
    print(f"Pesan terenkripsi yang dikirim: {encrypted_message}")
    
    # Tutup koneksi setelah pesan dikirim
    client_socket.close()

if __name__ == "__main__":
    # Pesan yang akan dienkripsi dan dikirim (panjang lebih dari 64 bit sesuai ketentuan tugas)
    message = '1101001110111010101010110010101010110101110111101010111010110101110100111011101010101011001010101011010111011110101011101011010101101011'
    start_client(message)

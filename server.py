import socket
from DES import decrypt_long

# Hardcoded kunci DES yang harus sama di client dan server (64-bit binary string)
KEY = '1101001110111010101010110010101010110101110111101010111010110101'

def start_server():
    # Inisialisasi server socket untuk menerima koneksi
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 23456))  # Menggunakan port 23456
    server_socket.listen(1)  # Server mendengarkan hingga 1 koneksi
    print("Server sedang menunggu koneksi pada port 23456...")

    # Terima koneksi dari client
    conn, addr = server_socket.accept()
    print(f"Koneksi dari: {addr}")
    
    # Menerima pesan terenkripsi dari client
    encrypted_message = conn.recv(4096).decode()  # Menerima hingga 4096 byte
    print(f"Pesan terenkripsi diterima: {encrypted_message}")

    # Dekripsi pesan yang diterima
    decrypted_message = decrypt_long(encrypted_message, KEY)
    print(f"Pesan setelah dekripsi: {decrypted_message}")
    
    # Tutup koneksi setelah selesai
    conn.close()

if __name__ == "__main__":
    start_server()

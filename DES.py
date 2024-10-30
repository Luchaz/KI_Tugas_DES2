import random
from des_table import *

# Fungsi untuk mengubah urutan bit
def permute(block, table):
    permuted_block = []
    for i in table:
        permuted_block.append(block[i - 1])
    return ''.join(permuted_block)

# Fungsi untuk XOR dua string bit
def xor(a, b):
    result = []
    for i in range(len(a)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)

# Fungsi untuk membagi blok menjadi bagian kiri dan kanan
def split_block(block):
    half = len(block) // 2
    left = block[:half]
    right = block[half:]
    return left, right

# Fungsi untuk memperluas blok 32-bit menjadi 48-bit menggunakan tabel ekspansi
def expansion(block):
    return permute(block, E)

# Fungsi substitusi S-box
def sbox_substitution(block):
    output = ''
    for i in range(8):
        section = block[i * 6:(i + 1) * 6]
        row = int(section[0] + section[5], 2)
        col = int(section[1:5], 2)
        output += format(S_BOX[i][row][col], '04b')
    return output

# Implementasi fungsi Feistel
def feistel_function(right, subkey):
    expanded_right = expansion(right)
    xored = xor(expanded_right, subkey)
    substituted = sbox_substitution(xored)
    return permute(substituted, P)

# Key generator
def key_generator():
    key = []
    for _ in range(64):
        key.append(random.choice('01'))
    return ''.join(key)

# Menghasilkan 16 kunci dari kunci awal
def generate_keys(key):
    keys = []
    for _ in range(16):
        keys.append(key[:48])
    return keys

# Fungsi enkripsi utama
def encrypt(plaintext, key):
    # Permutasi awal
    permuted_block = permute(plaintext, IP)
    left, right = split_block(permuted_block)
    keys = generate_keys(key)

    # 16 putaran struktur Feistel
    for i in range(16):
        new_right = xor(left, feistel_function(right, keys[i]))
        left, right = right, new_right

    # Permutasi akhir
    final_block = permute(right + left, FP)
    return final_block

# Fungsi dekripsi utama
def decrypt(ciphertext, key):
    # Permutasi awal
    permuted_block = permute(ciphertext, IP)
    left, right = split_block(permuted_block)
    keys = generate_keys(key)

    # 16 putaran struktur Feistel
    for i in range(15, -1, -1):
        new_right = xor(left, feistel_function(right, keys[i]))
        left, right = right, new_right

    # Permutasi akhir
    final_block = permute(right + left, FP)
    return final_block

def encrypt_long(plaintext, key):
    ciphertext = ''
    # Proses setiap blok 64-bit
    for i in range(0, len(plaintext), 64):
        block = plaintext[i:i + 64]
        # Padding jika blok terakhir kurang dari 64 bit
        if len(block) < 64:
            block = block.ljust(64, '0')
        ciphertext += encrypt(block, key)
    return ciphertext

def decrypt_long(ciphertext, key):
    plaintext = ''
    for i in range(0, len(ciphertext), 64):
        block = ciphertext[i:i + 64]
        plaintext += decrypt(block, key)
    return plaintext.strip('0')  # Menghapus padding

# Penggunaan
plaintext = '1101001110111010101010110010101010110101110111101010111010110101'  # 64 bit
key = key_generator()
print(f"Original Plaintext: {plaintext}")
ciphertext = encrypt(plaintext, key)
print(f"Ciphertext: {ciphertext}")
decrypted_text = decrypt(ciphertext, key)
print(f"Decrypted Plaintext: {decrypted_text}")

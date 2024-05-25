import random
import hashlib
sec_bytes = 32 #lamda

# Функция генератора 32-битных случайных чисел
def generate():
    binary_number = 0
    for i in range(sec_bytes):
        bit = random.randint(0, 1)
        binary_number |= (bit << (sec_bytes - 1 - i))
    return format(binary_number, f'0{sec_bytes}b')

# Вычислить значение XOR двух двоичных чисел
def xor_two_bin(a, b, num_bit):
    return format(int(a, 2) ^ int(b, 2), f'0{num_bit}b')

#PRG
def G(seed):
    hash_output = hashlib.sha256(seed.encode()).hexdigest()
    hash_binary = bin(int(hash_output, 16))[2:].zfill(256)
    return hash_binary[0:3*sec_bytes] #получить первые 3*32 от sha256

#Хеш-фунция H: {0,1}^*->{0,1}^32
def H(*value):
    combined = ''.join(str(v) for v in value)
    hash_output = hashlib.sha256(combined.encode()).hexdigest()
    hash_binary = bin(int(hash_output, 16))[2:].zfill(256)
    return hash_binary[0:sec_bytes]

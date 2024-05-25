from PRG import sec_bytes, generate, xor_two_bin, G
from ring import RingSignature
from rsign import rsign

class Client():
    def __init__(self, ringSig):
        self.p_key, self.s_key = self.genkey()    #Создать свой ключи
        self.ringSig = ringSig
        self.number_ín_ring = self.ringSig.n+1
        self.ringSig.add_client(self.p_key) #Передать открытый ключ

    #Функция для создания свой ключи
    def genkey(self):
        s_key = []
        p_key = []
        for i in range(sec_bytes):
            s_key.append(generate())
            s_key.append(generate())
            p_key.append(xor_two_bin(G(s_key[-1]), G(s_key[-2]), sec_bytes * 3))
        return p_key, s_key
    #Послать сообщение
    def send(self, m):
        r, x = rsign(self.ringSig.p_keys, self.s_key, self.number_ín_ring, m) #Создать подписи
        print(self.ringSig.check(r, x, m)) #Послать на систему

clients = []
ringSig = RingSignature()
for i in range(5):
    c = Client(ringSig)
    clients.append(c)

clients[1].send('hello')
clients[2].send('hello')
ringSig.display_messages()

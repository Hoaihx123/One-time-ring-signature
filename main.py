from models.ring import RingSignature
from models.member import Member
clients = []
ringSig = RingSignature()
for i in range(5):
    c = Member(ringSig)
    clients.append(c)

clients[1].send('Всем привет!')
clients[2].send('Меня зовут Хоай')
clients[0].send('Я люблю криптографию!')
clients[1].send('юююю')

ringSig.display_messages()

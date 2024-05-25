from protocols.rver import rver
from protocols.trace import trace
from datetime import datetime

class RingSignature():
    def __init__(self):
        self.p_keys = []
        self.n = 0
        self.signatures = [] #сохранение старых подписи
        self.messages = []
    def add_member(self, p_key):
        self.p_keys.append(p_key)
        self.n += 1
    def check(self, r, x, m):
        if rver(self.p_keys, r, x, m) == False:
            response = 'Ошибка! Возможно ты не участник группы'
            return response
        for r1, x1 in self.signatures:
            result = trace(self.p_keys, r1, r)
            if result:
                pk = ''.join(result[0])
                response = f'!!!!!{result[1]}-й участник, имеющий открытый ключ:\n{pk}\nподписал много раз!!!!!'
                return response
        response = 'Сообщение успешно отправлено'
        self.signatures.append([r, x])
        self.messages.append(m + ' ' + str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        return response
    def display_messages(self):
        print("-----История активности:-------")
        print('\n'.join(self.messages))
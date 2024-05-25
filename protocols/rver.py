from PRG import sec_bytes, G, H, xor_two_bin
def rver(R, r, x, m):
    c = []
    #рассчитать ci
    for i in range(len(R)):
        c_i = []
        for j in range(sec_bytes):
            if x[i][j] == '0':
                c_i.append(G(r[i][j]))
            else:
                c_i.append(xor_two_bin(G(r[i][j]), R[i][j], 3 * sec_bytes))
        c.append(c_i)
    #XOR всех xi
    z_ = 0
    for i in range(len(R)):
        z_ = z_ ^ int(x[i], 2)
    return format(z_, f'0{sec_bytes}b') == H(R, m, c) #проверить равенство между z_ и Хеш-фунциям
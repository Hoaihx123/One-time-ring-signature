from PRG import generate, sec_bytes, xor_two_bin, G, H

def rsign(R, s_key, signer, m):
    x = []
    r = []
    c = []
    #случайные xi, ri для расчета ci
    for i in range(len(R)):
        if i != signer-1:
            x_i = generate()
            x.append(x_i)
            r_i = []
            c_i = []
            for j in range(sec_bytes):
                x_ij = x_i[j]
                r_ij = generate()
                if x_ij == '0':
                    c_i.append(G(r_ij))
                else:
                    c_i.append(xor_two_bin(G(r_ij), R[i][j], sec_bytes*3))
                r_i.append(r_ij)
            r.append(r_i)
            c.append(c_i)
        else:
            c_i = []
            for i in range(sec_bytes):
                c_i.append(G(s_key[2*i]))
            c.append(c_i)
            x.append(format(0, f'0{sec_bytes}b'))
            r.append(0)
    #рассчитать x_l
    z = H(R, m, c)
    x_l = int(z, 2)
    for i in range(len(R)):
        x_l = x_l^int(x[i], 2)
    x[signer-1] = format(x_l, f'0{sec_bytes}b')
    #рассчитать r_l
    r_l = []
    for i in range(sec_bytes):
        if x[signer-1][i] == '0':
            r_l.append(s_key[i*2])
        else:
            r_l.append(s_key[i*2+1])
    r[signer-1] = r_l
    return r, x
from PRG import sec_bytes, xor_two_bin, G
def trace(R, r1, r2):
    for i in range(len(R)):
        for j in range(sec_bytes):
            if xor_two_bin(G(r1[i][j]), G(r2[i][j]), 3*sec_bytes) == R[i][j]:
                return R[i], i+1
    return 0
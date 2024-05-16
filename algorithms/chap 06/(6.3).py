NO_OF_CHARS = 128

def shift_table(pat):
    m = len(pat)
    tbl = [m] * NO_OF_CHARS
    for i in range(m - 1):
        tbl[ord(pat[i])] = m - 1 - i
    return tbl
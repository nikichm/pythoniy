import hashlib


def karp(s):
    len_s = len(s)
    k = 0
    l = 0
    for j in range(len_s):
        x = 1 + j
        while x <= len_s and len(s[j:x]) != len_s:
            len_ss = s[j:x]
            l += 1
            k -= 1
            h_sub = hashlib.sha1(len_ss.encode('utf-8')).hexdigest()
            i = j
            m = 0
            while i < len(s) - len(len_ss) + 1:
                if h_sub == hashlib.sha1(s[i:i + len(len_ss)].encode('utf-8')).hexdigest():
                    k += 1
                    m += 1
                i += 1
            if m > 1: #убирает неккоректность повторов встречающихся более 1 раза
                l += m - 2
            x += 1
    m = l - k
    return f'Всего подстрок {m}, повторений подстрок {k}'


s_1 = 'ppppp'
print(karp(s_1))
































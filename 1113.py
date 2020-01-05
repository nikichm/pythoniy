import hashlib


def rabin_karp(subs):
    len_sub = len(subs)
    h_sub = hashlib.sha256(subs.encode('utf-8')).hexdigest()
    for i in range(len(subs) - len_sub + 1):
        spam = hashlib.sha256(subs[i:i + len_sub].encode('utf-8')).hexdigest()
        for j in range(len(subs) - len_sub + 1):
            if h_sub == spam:
                return i
    return -1


s_1 = 'Hello World!'
print(rabin_karp(s_1))

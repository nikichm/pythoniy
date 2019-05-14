def function_1 (name, age, city) :
    s = f' {name} , {age} , проживает в {city} '
    return s
a = "Ivan"
b = "23"
c = "Moskow"
print(function_1(a,b,c))

def function_2 (a, b, c) :
    q  = a
    for x in a,b,c:
        if x > q :
            q = x
    return q
a = 8
b = 2
c = 3
print(function_2(a,b,c))

def function_3 (*args) :
    c = max(args, key = len)
    return c
a = function_3("qwer", "wer", "q", "qwerty", "qwwe")
print(a)
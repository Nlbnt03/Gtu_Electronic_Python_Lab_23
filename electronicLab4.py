def problem1(a):
    kume = {"1","2","3","4","5","6","7","8","9","0","J","Q","K"}
    if "K" in a:
        print(True)
    else:
        print(False)

def problem2 (a, b, c, d):
    if (a < b and a < c) and a < d:
        print(a)
    elif (b < a and b < c) and b < d:
        print(b)
    elif (c < a and c < b) and c < d:
        print(c)
    else:
        print(d)

def problem8 (a):
    kume = set()
    for letter in a :
        kume.add(letter)
    if(len(a) != len(kume)):
        print(False)
    else:
        print(True)

def problem4 (r, h, pi = 3.1415):
    result = pi * (r ** 2) * h
    print(result)






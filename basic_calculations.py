def add(y):
    e = y.split(" ")
    t =[]
    for i in e:
        a = int(i)
        t.append(a)
    return sum(t)

def substitution(y):
    e = y.split(" ")
    t =[]
    for i in e:
        a = int(i)
        t.append(a)
    r =0
    for i in range(0,len(t)):
        if i ==0:
           r = t[0]
           continue
        r -= t[i]
    return r

def multiplying(y):
    e = y.split(" ")
    t =[]
    for i in e:
        a = int(i)
        t.append(a)
    r =0
    for i in range(0,len(t)):
        if i ==0:
           r = t[0]
           continue
        r *= t[i]
    return r


def divide(y):
    e = y.split(" ")
    t =[]
    for i in e:
        a = int(i)
        t.append(a)
    r =0
    for i in range(0,len(t)):
        if i ==0:
           r = t[0]
           continue
        r /= t[i]
    return r

def d()


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
print(substitution("1 2 5"))          

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
print(multiplying("2 5"))          


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
print(divide("5 2"))    
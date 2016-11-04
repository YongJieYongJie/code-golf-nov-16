def a(b, c):
    l = len(b)
    r = ''
    for i in range(0, l-1):
        for j in range(0, int(l//c)+1):
            z = i+(c*j)
            if (z < l):
                r += b[z]
                if (len(r) == l):
                    print(r)

a('abcdefghijklmnopqrstuvwxyz', 2)

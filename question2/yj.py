def a(b):
    i = 9
    while i>-100:
        if i == 0:
            i -= 1
            continue
        elif i in b and ((b[b.index(i)-1]) == 0 or (b[b.index(i)+1]) == 0) :
            print( i)
            break
        else:
            i -= 1

a([-11, 0, 0, 0, 0, 0, -12, 10])

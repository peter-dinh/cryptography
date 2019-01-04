def power(x, b, n):
    a = x
    y = 1
    while b > 0:
        if b % 2 != 0:
            y = (y * a) %n
        b = b >> 1
        a = (a * a) % n
    return y
if __name__ == '__main__':
    x = power(7, 21, 100)
    for m in range(30, 2000):
        if power(100, 293, m) == 21:
            print(m)
            break
    print (x)
def gcd(p, q):
    if q == 0:
        return p
    return gcd(q, p % q)

if __name__ == '__main__':
    divisor = gcd(5000000000, 62)
    print(divisor)
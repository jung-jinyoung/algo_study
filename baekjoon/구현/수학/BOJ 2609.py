n, m = map(int, input().split())

# 최대 공약수 구현
def gcd(n, m) : 
    if m == 0:
        return n
    return gcd(m, n % m)

gcd = gcd(n, m)
lcd = n * m // gcd

print(gcd)
print(lcd)
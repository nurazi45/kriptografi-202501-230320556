# Aritmetika Modular dasar
def mod_add(a, b, n): return (a + b) % n
def mod_mul(a, b, n): return (a * b) % n
def mod_exp(a, e, n): return pow(a, e, n)

print("==Aritmetika Modular==")
print("7+5 mod 12 =", mod_add(7, 5, 12))    # 0
print("7*5 mod 12 =", mod_mul(7, 5, 12))    # 11
print("7^128 mod 13 =", mod_exp(7, 128, 13))# 9

# GCD (Euclidean)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print("\n==GCD==")
print("gcd(54, 24) =", gcd(54, 24))         # 6

# Extended Euclidean dan invers
def egcd(a, b):
    if a == 0: return b, 0, 1
    g, x1, y1 = egcd(b % a, a)
    return g, y1 - (b // a) * x1, x1

def modinv(a, n):
    g, x, _ = egcd(a, n)
    return x % n if g == 1 else None

print("\n== Extended Euclidean & Invers Modular==")
print("Invers 3 mod 11 =", modinv(3, 11))   # 4

# Logaritma diskrit kasar
def discrete_log(a, b, n):
    for x in range(n):
        if pow(a, x, n) == b:
            return x

print("\n==Logaritma diskrit ==")
print("3^x ≡ 4 mod 7, x =", discrete_log(3, 4, 7)) # 4

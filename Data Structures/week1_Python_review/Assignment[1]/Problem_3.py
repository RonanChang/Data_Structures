#this is created with Euclid's algorithms

def gcd(a,b):
    while b != 0:
        t = b
        b = a%b
        a = t
    return a

print(gcd(120,18))

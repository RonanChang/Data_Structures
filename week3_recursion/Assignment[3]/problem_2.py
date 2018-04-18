# This method can handle both negative and positive exponents
def Power(x,n):
    if n == 0:
        return 1
    elif n > 0:
        return x * Power(x,n-1)
    else:
        return 1/x * Power(x,n+1)
    

print(Power(2,-4))
print(Power(3,4))

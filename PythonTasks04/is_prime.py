def is_prime (num1):
    for i in range(2,num1):
        if num1%i==0:
            return False
        else:
            return True
print(is_prime(3))
def is_fibonacci(num1): #
    previous=0
    current=1
    next=previous+current
    while(next<=num1):
        if next==num1:
         return True
        previous=current
        current=next
        next=previous+current
    return False
print(is_fibonacci(5))
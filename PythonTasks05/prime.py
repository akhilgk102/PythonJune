numbers=[10,11,12,13,14,20,21]

for number in numbers:

    is_prime=True

    for i in range(2,number):

        if number%i==0:

            is_prime=False

        break

    if is_prime==True:

        print(number)

















# is_prime=True
# for i in range(2,len(numbers)):
#     if numbers[i]%i==0:
#         is_prime=False
#         break
# print(numbers[i])
        
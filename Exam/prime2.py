# num=int(input("Enter the number: ")) #7
# is_prime=True
# for i in range(2,num):
#     if num%i==0:  #7%1==0
#         is_prime=False
#         break
# print(f"{num} is prime" if is_prime==True else f"{num} is not Prime")

# num=int(input("Enter the number: ")) #153
# temp=num
# result=0
# while(num!=0):
#     digit=num%10 #3
#     result=result*10+digit #3
#     num=num//10 #15
# print(f"{temp} is Palindrome" if result==temp else f"{temp} is not Palindrome")

# num=int(input("Enter the number: ")) #5
# fact=1
# for i in range(1,num+1): 
#     fact=fact*i#1*5 5
#     print(fact)

num=int(input("Enter the number: ")) #5
fact=1
while(num>0):
    fact=fact*num #1*5
    num=num-1 #4
print(fact)
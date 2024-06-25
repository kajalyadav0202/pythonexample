
# # example using a variable flag
# # num=int(input("enter the number"))
# # flag=False
# # if num==1:
# #     print(num,"it is not a prime number")
# # elif num>1:
# #     for i in range(2,num):
# #         if (num%i)==0:
# #             flag=True
# #             break
# #     if flag:
# #         print(num,"is not a prime number")
# #     else:
# #         print(num,"is the prime number")    


# # example using a for else statement

# num=int(input("enter the number"))
# if num==1:
#     print("it is not a prime number,num")
# elif num>1:
#     for i in range(2,num):
#         if (num%i)==0:
#           print(num,"it is not a prime number")
#           print(i,"times",num//i,"is",num)
#           break
#     else:
#         print("it is prime number")
# else:
#     print(num,"is not a prime number")


lower=int(input("enter the lower number"))
upper=int(input("enter the  upper number"))
print("prime number between",lower,"and",upper,"are")
for num in range(lower,upper+1):
    if num>=1:
        for i in  range(2,num):
            if (num%i)==0:
                break
            else:
                print(num)

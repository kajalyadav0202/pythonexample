# # # # # # # # # num=int(input("enter the value of number"))
# # # # # # # # # f=1
# # # # # # # # # while num>0:
# # # # # # # # #      f=f*num
# # # # # # # # #      num=num-1
# # # # # # # # # print("facorial is",f)

# # # # # # # # # # num=int(input("enter the value"))
# # # # # # # # # # f=1
# # # # # # # # # # if num<0:
# # # # # # # # # #     print("sorry factorial does not exist")
# # # # # # # # # # elif num==0:
# # # # # # # # # #     print("factorial of 0 is : 1")
# # # # # # # # # # else:
# # # # # # # # # #     for i in range(1,num+1):
# # # # # # # # # #         f=f*i
# # # # # # # # # #     print("factorial of ",num,"is",f)


# # # # # # # # num=int(input("enter the number"))
# # # # # # # # for i in range(1,11):
# # # # # # # #   print(num*i)


# # # # # # # print("checking armstrong number")
# # # # # # # num=int(input("enter the number"))
# # # # # # # sum=0
# # # # # # # temp=num
# # # # # # # while temp>0:
# # # # # # #     digit=temp%10
# # # # # # #     sum+=digit**3
# # # # # # #     temp//=10
# # # # # # # if num==sum:
# # # # # # #     print("it is an armstrong number")
# # # # # # # else:
# # # # # # #     print("it is not the armstrong number")


# # # # # num=int(input("enter the number"))
# # # # # sum=0
# # # # # temp=num
# # # # # for num in range(400,600):
# # # # #     digit=temp%10
# # # # #     sum+=digit**3
# # # # #     temp//=10
# # # # # if num==sum:
# # # # #     print("it is an armstrong number")
# # # # # else:
# # # # #     print("it is not a armstrong nmber")

# # # # lower=int(input("enter the number"))
# # # # upper=int(input("enter the number"))
# # # # for num in range(lower,upper+1):
# # # #     order=len(str(num))
# # # #     sum=0
# # # #     temp=num
# # # #     while temp>0:
# # # #         digit=temp%10
# # # #         sum+=digit**order
# # # #         temp//=10
# # # #     if num==sum:
# # # #         print(num)


# # # num=int(input("enter the vlaue of number"))
# # # if num<0:
# # #     print("enter the positive number")
# # # else:
# # #     sum=0
# # #     while num>0:
# # #         sum+=num
# # #         num-=1
# # #     print(sum)


# # num=int(input("enter the value of number"))
# # sum=0
# # for num in range(1,num + 1):
# #             sum+=num
# #             num-=1
# # print(sum)

# terms=int(input("enter the terms"))
# result=list(map(lambda x: 2** x , range(terms)))
# for i in range( terms):
#     print("2 raised to power ",i,"is",result[i])

lower=int(input("enter the value of lower number"))
upper=int(input("enter the value of upper number"))
result=list(map(lambda x: 3** x,range(lower-1,upper+1 )))
for i in range(lower-1,upper+1):
    print(" 3 raised to power",i,"is" ,result[i])

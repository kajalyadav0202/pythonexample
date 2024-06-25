# # num=int(input("enter the value of number"))
# # if num<0:
# #     print("number is negative")
# # elif num==0:
# #     print("number is zero")
# # else:
# #     print("number is positive")


# year=int(input("enter the year"))
# if (year%400==0)and(year%100==0):
#     print("year is a leap year")
# elif(year%4==0)and(year%100!=0):
#     print("year is laep year")
# else:
#     print("year is not a leap year")

num1=int(input("enter the value of number one"))
num2=int(input("enter the value of the number two"))
num3=int(input("enter the value of the number three"))
if (num1>num2)and(num1>num3):
    largest=num1
elif(num2>num1)and(num2>num3):
    largest=num2
else:
    largest=num3
print("the largest number among the three is:",largest)
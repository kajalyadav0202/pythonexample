# # # # # # # # # # #  x=2
# # # # # # # # # # #  y=3
# # # # # # # # # # # z=x+y
# # # # # # # # # # #  print("ans is ",z)

# # # # # # # # # # # a=6
# # # # # # # # # # # b=7
# # # # # # # # # # # area =a*b
# # # # # # # # # # # print("area of rectangle is",area)

# # # # # # # # # # # r=8
# # # # # # # # # # # area=r*3.14*r
# # # # # # # # # # # print("area of circle",area)

# # # # # # # # # # # a,b,c=12,3,4
# # # # # # # # # # # volume=a*b*c
# # # # # # # # # # # print("volume of cuboid",volume)

# # # # # # # # # # a=int(input("enter a"))
# # # # # # # # # # b=int(input("enter b"))
# # # # # # # # # # c=a+b
# # # # # # # # # # print("ans is ",c)

# # # # # # # # # p=int(input("enter p"))
# # # # # # # # # r=float(input("enter r"))
# # # # # # # # # n=int(input("enter n"))
# # # # # # # # # SI=(p*r*n)/100
# # # # # # # # # print("answer is ",SI)

# # # # # # # # maths=int(input("enter maths"))
# # # # # # # # english=int(input("enter english"))
# # # # # # # # physics=int(input("enter physics"))
# # # # # # # # chemistry=int(input("enter chemistry"))
# # # # # # # # biology=int(input("enter biology"))
# # # # # # # # totalmarks = maths + english + physics + chemistry + biology
# # # # # # # # percentage = totalmarks*100/500
# # # # # # # # print("ans is",totalmarks)
# # # # # # # # print("result is",percentage)

# # # # # # # N=124
# # # # # # # d3=N%10
# # # # # # # N=N//10
# # # # # # # d2=N%10
# # # # # # # N=N//10
# # # # # # # d1=N%10
# # # # # # # result=d1*d2*d3
# # # # # # # print("ans is",result)

# # # # # # N=14567
# # # # # # N=N//100
# # # # # # d2=N%10
# # # # # # N=N//100
# # # # # # d1=N%100
# # # # # # print("ans is",d1*d2)

# # # # # N=1539478
# # # # # d3=N%10
# # # # # N=N//1000
# # # # # d2=N%10
# # # # # N=N//100
# # # # # d1=N%10
# # # # # print("ans is",d1*d2*d3)


# # # # a=45
# # # # b=9
# # # # print(a<<b) 

# # # gst=0
# # # al=int(input("enter the annual income"))
# # # if al>700000:
# # #     gst=(al*18)/100


# # # print("annual income is ",al)
# # # print("gst is ",gst)

# # a=int(input("enter the value of a"))
# # b=int(input("enter the value of b"))
# # if a>b:
# #     print("a is greater")
# # else:
# #     print("b is greater")
 
# a=int(input("enter the value of a"))
# if a%2==0:
#     print("a is even")
# else:
#     print(" a is odd")

per=int(input("enter the percentage of students"))
if(per>90):
    print("grade is A+")
elif(per>85):
    print("grade is A")
elif(per>80):
    print("grade is B+")
elif(per>75):
    print("grade is B")
else:
    print("grade is c")